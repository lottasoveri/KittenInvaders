import pygame
from ammo import Bolt

class Player(pygame.sprite.Sprite):
    def __init__(self, coords, max_x, speed, controls):
        super().__init__()
        image_1 = pygame.image.load("images/cannon1.png").convert_alpha()
        image_2 = pygame.image.load("images/cannon2.png").convert_alpha()
        self.images = [image_1, image_2]
        self.image_index = 0
        self.image = self.images[int(self.image_index)]
        self.rect = self.image.get_rect(midbottom = coords)
        self.coords = coords
        self.max_x = max_x
        self.speed = speed
        self.controls = controls
        self.loaded = True
        
        self.bolts = pygame.sprite.Group()
    
    # User input:    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if self.controls == 1:
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
        else:
            if keys[pygame.K_a]:
                if self.rect.left > 0:
                    self.rect.x -= self.speed
            if keys[pygame.K_d]:
                if self.rect.right <= self.max_x:
                    self.rect.x += self.speed
            if keys[pygame.K_RSHIFT]:
                if self.loaded:
                    self.shoot()
                    self.loaded = False
            if not keys[pygame.K_RSHIFT]:
                self.loaded = True
                
    def player_animation(self):
        self.image_index += 0.05
        if self.image_index >= len(self.images):
            self.image_index = 0
        self.image = self.images[int(self.image_index)]
           
    def shoot(self):
        self.bolts.add(Bolt("player", 5, self.rect.midtop, self.rect.bottom+50))
                
    def update(self):
        self.get_input()
        self.bolts.update()
        