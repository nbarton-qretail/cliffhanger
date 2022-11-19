import time
import pygame
import numpy as np
from gamecard import Responsebox
from wall import Wall
from character import Character
from random import uniform




game_params = {
    "question": "How much does Woolworths spend on Secondary Freight?",
    "answer": 10
}

pygame.init()

win_width= 1920
win_height= 1080

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Cliffhanger")
win.fill((255,255,255))

# Init wall
wall = Wall()

# Init Character
char = Character()

# Generate the steps the Character will take up the wall using the characters offset
wall.generate_step_vector_points(char.x_offset, char.y_offset)

# object pos start
char.curr = wall.vectors.pop(0)

response_box = Responsebox()

def redrawGameWindow(vector_points):
    # draw background
    win.fill((255,255,255))
    win.blit(wall.img, (0,0))
    # draw inputbox
    
    # Blit the text.
    win.blit(response_box.txt_surface(), (response_box.input_box.x+5, response_box.input_box.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(win, response_box.color, response_box.input_box, 2, 5)

    # draw character
    win.blit(char.img, (vector_points))
    pygame.display.update()

def answer_evaluator(response, game_params):
    answer = game_params['answer']
    return abs(answer - response)

def evaluate_event(events):
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if response_box.input_box.collidepoint(event.pos):
                # Toggle the active variable.
                response_box.active = True
            else:
                response_box.active = False
            # Change the current color of the input box.
            response_box.set_colour()
        if event.type == pygame.KEYDOWN:
            if response_box.active:
                if event.key == pygame.K_RETURN:
                    print(response_box.text)
                    # response_box.text = ''
                    char.animate = True
                elif event.key == pygame.K_BACKSPACE:
                    response_box.text = response_box.text[:-1]
                elif event.key in [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_KP0,pygame.K_KP1,pygame.K_KP2,pygame.K_KP3,pygame.K_KP4,pygame.K_KP5,pygame.K_KP6,pygame.K_KP7,pygame.K_KP8,pygame.K_KP9,pygame.K_KP_PERIOD,pygame.K_PERIOD]:
                    response_box.text += event.unicode
                    redrawGameWindow(char.curr)
    return 

def gen_coords(x1, y1, x2, y2, n):
    x_points = list(np.linspace(x1, x2, n))
    y_points = list(np.linspace(y1, y2, n))
    vectors=[]
    for i in range(n):
            vectors.append((int(x_points[i]), int(y_points[i])))
    return vectors


redrawGameWindow(char.curr)
run = True
moves = 0

while run:

    events = pygame.event.get()
    if len(events) > 0:
        evaluate_event(events)
        
    if response_box.text != '' and char.animate != True:
        # Evaluate response
        contestant_response = int(response_box.text)
        moves = answer_evaluator(contestant_response, game_params)

    if len(wall.vectors) == 0:
        run = False

    if moves > 0 and char.animate == True:
        
        finish = wall.vectors.pop(0)
        vector_points = gen_coords(char.curr[0], char.curr[1], finish[0], finish[1], 50)

        while len(vector_points) > 0:
            if len(vector_points) == 1:
                next_point = finish
                vector_points=[]
            else:
                next_point = vector_points.pop(0)
            char.curr = next_point
            redrawGameWindow(next_point)
        moves -= 1

    elif moves == 0:
        response_box.text = ''
        redrawGameWindow(char.curr)
        char.animate = False

pygame.quit()