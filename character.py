import pygame
from PIL import Image

class Character:
    def __init__(self) -> None:
        self.filepath = "img/mountaineer.png"
        # get image dimensions
        img = Image.open(self.filepath)
        self.img_width = img.width
        self.img_height = img.height

        self.img = pygame.image.load(self.filepath)
        self.animate = False

        # montaineer is 600x600.  making it 10 times smaller
        scale = 7
        self.x_offset = (self.img_width-(self.img_width - 435)) // scale
        self.y_offset = (self.img_width-(self.img_width - 484)) // scale
        
        # object dims
        self.width = 600 // scale
        self.height = 600 // scale
        self.img = pygame.transform.smoothscale(self.img, size=(self.width, self.height))

    def set_to_start(self):
        """Sets character to Position 0 on the wall"""
        pos_0 = (288, 651)
        self.curr = (pos_0[0]-self.x_offset, pos_0[1]-self.y_offset)