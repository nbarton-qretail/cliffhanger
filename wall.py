import pygame
import numpy as np
from PIL import Image


class Wall:
    def __init__(self) -> None:
        self.filepath = "img/cliffhanger_wall.png"
        # get image dimensions
        img = Image.open(self.filepath)
        self.img_width = img.width
        self.img_height = img.height

        # load image to pygame
        self.img = pygame.image.load(self.filepath)

        # 1 pos on the wall
        self.start_x = 309
        self.start_y = 639

        # 25 pos on the wall
        self.finish_x = 1048
        self.finish_y = 229

        self.steps = 25

        self.x_vectors = list(np.linspace(self.start_x, self.finish_x, num=self.steps))
        self.y_vectors = list(np.linspace(self.start_y, self.finish_y, num=self.steps))

    def generate_step_vector_points(self, x_offset, y_offset):
        self.vectors=[]
        for i in range(self.steps):
            self.vectors.append((int(self.x_vectors[i]-x_offset), int(self.y_vectors[i]-y_offset)))
        # Append the point to fall to if all points are used.
        self.vectors.append((1058, 456))
    