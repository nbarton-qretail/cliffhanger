import pygame

class Character:
    def __init__(self) -> None:
        self.img = pygame.image.load("img/mountaineer.png")
        self.curr = (0,0)
        self.animate = False

        # montaineer is 600x600.  making it 10 times smaller
        scale = 7
        self.x_offset = (600-(600 - 435)) // scale
        self.y_offset = (600-(600 - 484)) // scale

        # object dims
        self.width = 600 // scale
        self.height = 600 // scale
        self.img = pygame.transform.smoothscale(self.img, size=(self.width, self.height))