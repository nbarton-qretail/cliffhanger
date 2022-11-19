import pygame

class Responsebox:
    def __init__(self):
        self.font = pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(1280 + 100, 100, 140, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''

    def txt_surface(self):
        return self.font.render(self.text, True, self.color)
    
    def set_colour(self):
        self.color_active if self.active else self.color_inactive
    
    