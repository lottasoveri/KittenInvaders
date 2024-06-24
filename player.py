import pygame
from ammo import Bolt

class Player(pygame.sprite.Sprite):
    def __init__(self, coords, max_x, speed):
        super().__init__()
        self.image = pygame.image.load("images/cannon.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = coords)
        self.speed = speed
        self.max_x = max_x
        self.loaded = True
        
        self.bolts = pygame.sprite.Group()
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            if self.rect.right <= self.max_x:
                self.rect.x += self.speed
                
        if keys[pygame.K_SPACE]:
            if self.loaded:
                self.shoot()
                self.loaded = False
        if not keys[pygame.K_SPACE]:
            self.loaded = True
            
    def shoot(self):
        self.bolts.add(Bolt("player", 5, self.rect.midtop, self.rect.bottom+50))
                
    def update(self):
        self.get_input()
        self.bolts.update()
        