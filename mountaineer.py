import pygame
import numpy as np

pygame.init()

win_width= 1280
win_height= 1080

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Mountaineer")

#
bg = pygame.image.load("cliffhanger_wall.png")
char = pygame.image.load("mountaineer.png")

# montaineer is 600x600.  making it 10 times smaller
scale = 7
x_offset = (600-(600 - 435)) // scale
y_offset = (600-(600 - 484)) // scale

# object dims
width = 600 // scale
height = 600 // scale
char = pygame.transform.smoothscale(char, size=(width, height))

start_x = 288
start_y = 651

finish_x = 1048
finish_y = 229

steps = 25

# object pos start
x = start_x - width
y = start_y - height

x_vectors = np.linspace(start_x, finish_x, num=steps)
y_vectors = np.linspace(start_y, finish_y, num=steps)

# flags
step = 0
run = True

def redrawGameWindow():
    # draw background
    win.blit(bg, (0,0))
    # draw character
    win.blit(char, (x,y))
    pygame.display.update()

while run:
    pygame.time.delay(100)
    print(f"{step=}",f"{x=}", f"{y=}")
    x = int(x_vectors[step]-x_offset)
    y = int(y_vectors[step]-y_offset)

    if step == steps:
        run = False

    win.fill((0,0,0))
    redrawGameWindow()
    step+=1

pygame.quit()