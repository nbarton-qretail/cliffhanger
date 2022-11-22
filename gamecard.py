import pygame

class Questionbox:
    def __init__(self, question, wall_width):
        self.question_text = question
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render(self.question_text, True, pygame.Color('black'))
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (wall_width, 200)

class Responsebox:
    def __init__(self, win_width, wall_width):
        self.font = pygame.font.Font(None, 32)

        width = 140
        left = win_width - ((win_width-wall_width)//2) - (width // 2)
        top = 400
        height = 32
        self.input_box = pygame.Rect(left, top, width, height)

        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''

    def txt_surface(self):
        return self.font.render(self.text, True, self.color)
    
    def set_colour(self):
        self.color_active if self.active else self.color_inactive
    
class Answerimg:
    def __init__(self) -> None:
        self.tick_filepath = "img/tick.png"
        self.tick_img = pygame.image.load(self.tick_filepath)
        self.tick_img = pygame.transform.smoothscale(self.tick_img, size=(800, 800))
        self.tick_img_width = 800
        self.tick_img_height = 800
        
        self.cross_filepath = "img/cross.png"
        self.cross_img = pygame.image.load(self.cross_filepath)
        self.cross_img = pygame.transform.smoothscale(self.cross_img, size=(800, 800))
        self.cross_img_width = 800
        self.cross_img_height = 800