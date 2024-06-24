import pygame
from random import choice, randrange

class Kitty(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        kitty = choice(["images/kitty1.png", "images/kitty2.png", "images/kitty3.png"])
        self.image = pygame.image.load(kitty).convert_alpha()
        self.rect = self.image.get_rect(midbottom = (randrange(60, screen_width-60), 0))
        self.max_y = screen_height + 50
        
    def destroy(self):
        if self.rect.y > self.max_y:
            self.kill()
        
    def update(self):
        self.rect.y += 1
        self.destroy()
        