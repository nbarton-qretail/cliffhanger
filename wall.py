import pygame
import numpy as np

class Wall:
    def __init__(self) -> None:
        self.img = pygame.image.load("img/cliffhanger_wall.png")

        # 0 pos on the wall
        self.start_x = 288
        self.start_y = 651

        # 25 pos on the wall
        self.finish_x = 1048
        self.finish_y = 229

        self.steps = 24

        self.x_vectors = list(np.linspace(self.start_x, self.finish_x, num=self.steps))
        self.y_vectors = list(np.linspace(self.start_y, self.finish_y, num=self.steps))

    def generate_step_vector_points(self, x_offset, y_offset):
        self.vectors=[]
        for i in range(self.steps):
            self.vectors.append((int(self.x_vectors[i]-x_offset), int(self.y_vectors[i]-y_offset)))