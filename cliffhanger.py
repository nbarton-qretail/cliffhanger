import time
import pygame
import numpy as np
from gamecard import Questionbox, Responsebox, Answerimg
from wall import Wall
from character import Character
from random import uniform



questions = [
    {
    "question": "Pick and number between 1 and 20",
    "answer": 13
    },
    {
    "question": "Pick another number between 1 and 20",
    "answer": 7
    }
]

pygame.init()

win_width= 1920
win_height= 1080

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Cliffhanger")
win.fill((255,255,255))

# Init game board and character
wall = Wall()
char = Character()
answerimg = Answerimg()

# Load yodelling



def redrawGameWindow(vector_points):
    # Draw background
    win.fill((255,255,255))
    # Draw Cliffhanger Wall
    win.blit(wall.img, (0,0))

    # Draw Question
    win.blit(question_box.text, question_box.textRect)
    
    # Draw inputbox
    # Blit the text.
    win.blit(response_box.txt_surface(), (response_box.input_box.x+5, response_box.input_box.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(win, response_box.color, response_box.input_box, 2, 5)

    # Draw character
    win.blit(char.img, (vector_points))
    pygame.display.update()

def answer_evaluator(response, question):
    answer = question['answer']
    evaluated_answer = abs(answer - response)
    if evaluated_answer == 0:
        print("Correct")
        win.blit(answerimg.tick_img, ((win.get_width()//2) - (answerimg.tick_img_width//2), (win.get_height()//2) - (answerimg.tick_img_height//2)))
        # TODO: Play ding
        pygame.display.update()
        pygame.time.wait(1000)
    else:
        # cross and bzz sound
        print("Wrong")
        win.blit(answerimg.cross_img, ((win.get_width()//2) - (answerimg.cross_img_width//2), (win.get_height()//2) - (answerimg.cross_img_height//2)))
        # TODO: Play bzzz
        pygame.display.update()
        pygame.time.wait(1000)
    return evaluated_answer

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



for question in questions:

    question_box = Questionbox(question['question'], wall.img_width)
    char.set_to_start()
    wall.generate_step_vector_points(char.x_offset, char.y_offset)
    response_box = Responsebox(win_width, wall.img_width)
    run = True
    moves = 0
    redrawGameWindow(char.curr)

    while run:

        events = pygame.event.get()
        if len(events) > 0:
            evaluate_event(events)
            
        if response_box.text != '' and char.animate == True:
            # Evaluate response
            contestant_response = int(response_box.text)
            moves = answer_evaluator(contestant_response, question)

        if len(wall.vectors) == 0:
            # run = False
            break

        if char.animate == True:
            pygame.mixer.music.load("yodel.mp3")        
            pygame.mixer.music.play(loops=-1)
            
            while moves > 0:
                if len(wall.vectors) == 0:
                    # Player looses
                    break

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
            pygame.mixer.music.stop()

            if moves == 0:
                response_box.text = ''
                redrawGameWindow(char.curr)
                char.animate = False
            
            if len(wall.vectors) == 0:
                char.set_to_start()


pygame.quit()