import pygame
from random import choice

class Bolt(pygame.sprite.Sprite):
    def __init__(self, type, coords, screen_height):
        super().__init__()
        player_bolt = choice(["images/burger.png", "images/potato.png"])
        kitty_bolt = choice(["images/hairball.png", "images/toy.png"])
        if type == "player":
            self.image = pygame.image.load(player_bolt).convert_alpha()
            speed = 6
        else:
            self.image = pygame.image.load(kitty_bolt).convert_alpha()
            speed = 4
        self.rect = self.image.get_rect(center = coords)
        self.type = type
        self.speed = speed
        self.max_y = screen_height - 50

    def move(self):
        if self.type == "player":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def destroy(self):
        if self.rect.bottom < 0 or self.rect.bottom > self.max_y:
            self.kill()

    def update(self):
        self.move()
        self.destroy()
