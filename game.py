import pygame
from random import choice
from player import Player
from ammo import Bolt

class Game:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.controls = 1
        
        # Fonts:
        self.font_title = pygame.font.Font("fonts/PixeloidSansBold-PKnYd.ttf", 50)
        self.font_regular = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 30)
        self.font_small = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 20)
        self.font_score = pygame.font.Font("fonts/PixeloidMono-d94EV.ttf", 20)
        
        # Score & health:
        self.score = 0
        self.health = 4
        self.over = False
        
        # Player:
        self.player_sprite = Player((screen_width/2, screen_height-50), screen_width, self.controls)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)
        
        # Kitties:
        self.kitties = pygame.sprite.Group()
        self.kitty_droppings = pygame.sprite.Group()
        
        # Sounds:
        self.kitty_hit_sound = pygame.mixer.Sound("sounds/gulp.ogg")
        self.kitty_hit_sound.set_volume(0.4)
        self.player_hit_sound = pygame.mixer.Sound("sounds/uh-oh.ogg")
        self.player_hit_sound.set_volume(0.7)
        self.game_over_sound = pygame.mixer.Sound("sounds/game-over-arcade-6435.ogg")
        self.sound_on = True
        
    def update_controls(self):
        self.player_sprite = Player((self.screen_width/2, self.screen_height-50), self.screen_width, self.controls)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)
        
    def update_player_sounds(self):
        self.player_sprite = Player((self.screen_width/2, self.screen_height-50), self.screen_width, self.controls)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)
        
    def display_health(self):
        health_x = 25
        if self.health > 0:
            for i in range(self.health - 1):
                health_surf = pygame.image.load("images/heart1.png")
                health_rect = health_surf.get_rect(midleft = (health_x, self.screen_height - 25))
                self.screen.blit(health_surf, health_rect)
                health_x += 35
                i += 1
        if self.health < 4:
            for i in range(3 - (self.health-1)):
                health_surf = pygame.image.load("images/heart2.png")
                health_rect = health_surf.get_rect(midleft = (health_x, self.screen_height - 25))
                self.screen.blit(health_surf, health_rect)
                health_x += 35
                i += 1
    
    def animate_player(self):
        if self.health <= 1:
            self.player_sprite.player_animation()
     
    def display_score(self):
        score_surf = self.font_score.render(f" Score: {self.score} ", False, (0, 0, 51))
        score_rect = score_surf.get_rect(center = (self.screen_width/2, self.screen_height-25))
        pygame.draw.rect(self.screen, (204, 204, 204), score_rect)
        
        self.screen.blit(score_surf, score_rect)
        
    def display_pause_text(self):
        pause_surf = self.font_score.render(" P - Pause ", False, (0, 0, 51))
        pause_rect = pause_surf.get_rect(midright = (self.screen_width - 50, self.screen_height - 25))
        pygame.draw.rect(self.screen, (204, 204, 204), pause_rect)
        
        self.screen.blit(pause_surf, pause_rect)        
        
    def kitty_drop(self):
        if self.kitties.sprites():
            random_kitty = choice(self.kitties.sprites())
            dropping = Bolt("kitty", random_kitty.rect.midbottom, self.screen_height)
            self.kitty_droppings.add(dropping)
            
    def check_collisions(self):
        # Player bolts:
        if self.player.sprite.bolts:
            for bolt in self.player.sprite.bolts:
                if pygame.sprite.spritecollide(bolt, self.kitties, True):
                    if self.sound_on:
                        self.kitty_hit_sound.play()
                    bolt.kill()
                    self.score += 100
                    
        # Kitty droppings:
        if self.kitty_droppings:
            for dropping in self.kitty_droppings:
                if pygame.sprite.spritecollide(dropping, self.player, False):
                    self.health -= 1
                    if self.health <= 0:
                        if self.sound_on:
                            self.game_over_sound.play()
                        self.over = True
                    else:
                        if self.sound_on:
                            self.player_hit_sound.play()
                        dropping.kill()
                if dropping.rect.bottom >= self.screen_height - 50:
                    dropping.kill()
                    
        # Kitties:
        if self.kitties:
            for kitty in self.kitties:
                if pygame.sprite.spritecollide(kitty, self.player, False):
                    if self.sound_on:
                        self.game_over_sound.play()
                    self.over = True
                if kitty.rect.bottom >= self.screen_height - 50:
                    if self.sound_on:
                        self.game_over_sound.play()
                    self.over = True
                  
    def reset(self):
        self.score = 0
        self.health = 4
        self.over = False
        self.player_sprite.rect.x = self.screen_width/2 - 25
        self.player_sprite.image_index = 0
        self.player_sprite.image = self.player_sprite.images[int(self.player_sprite.image_index)]
        pygame.sprite.Group.empty(self.kitties)
        pygame.sprite.Group.empty(self.kitty_droppings)
        pygame.sprite.Group.empty(self.player.sprite.bolts)

    def run(self):
        self.player.update()
        self.kitties.update()
        self.kitty_droppings.update()
        self.check_collisions()
        self.animate_player()
            
        self.player.draw(self.screen)
        self.kitties.draw(self.screen)
        self.player.sprite.bolts.draw(self.screen)
        self.kitty_droppings.draw(self.screen)
        self.display_health()
        self.display_score()
        self.display_pause_text()
        