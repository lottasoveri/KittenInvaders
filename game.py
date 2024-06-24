import pygame
from random import choice
from player import Player
from ammo import Bolt

class Game:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Fonts:
        self.font_title = pygame.font.Font("fonts/PixeloidSansBold-PKnYd.ttf", 50)
        self.font_regular = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 30)
        self.font_small = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 20)
        self.font_score = pygame.font.Font("fonts/PixeloidMono-d94EV.ttf", 20)
        
        # Score & health:
        self.score = 0
        self.health = 3
        self.dead = False
        
        # Player:
        self.player_sprite = Player((screen_width/2, screen_height-50), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)
        
        # Kitties:
        self.kitties = pygame.sprite.Group()
        self.kitty_droppings = pygame.sprite.Group()
    
    def display_start(self):
        title_surf = self.font_title.render("Kitten Invaders", False, (156, 156, 156))
        title_rect = title_surf.get_rect(midtop = (self.screen_width/2, self.screen_height/3))
        
        msg_surf = self.font_regular.render(" Push \"Enter\" to play ", False, (0, 0, 25))
        msg_rect = msg_surf.get_rect(midtop = (self.screen_width/2, title_rect.bottom+100))
        pygame.draw.rect(self.screen, (156, 156, 156), msg_rect)        
        
        self.screen.blit(title_surf, title_rect)
        self.screen.blit(msg_surf, msg_rect)
    
    def display_score(self):
        score_surf = self.font_score.render(f" Score: {self.score} ", False, (0, 0, 25))
        score_rect = score_surf.get_rect(center = (self.screen_width/2, self.screen_height-25))
        pygame.draw.rect(self.screen, (156, 156, 156), score_rect)
        
        self.screen.blit(score_surf, score_rect)
        
    def display_pause(self):
        pause_surf = self.font_title.render("Game paused", False, (156, 156, 156))
        pause_rect = pause_surf.get_rect(midtop = (self.screen_width/2, self.screen_height/3))
        
        msg_surf = self.font_regular.render(" Push \"P\" to continue ", False, (0, 0, 25))
        msg_rect = msg_surf.get_rect(midtop = (self.screen_width/2, pause_rect.bottom+100))
        pygame.draw.rect(self.screen, (156, 156, 156), msg_rect)
        
        self.screen.blit(pause_surf, pause_rect)
        self.screen.blit(msg_surf, msg_rect)
        
    def display_game_over(self):
        title_surf = self.font_title.render("Game over!", False, (156, 156, 156))
        title_rect = title_surf.get_rect(midtop = (self.screen_width/2, self.screen_height/3))
        
        msg_surf = self.font_regular.render(" Push \"Enter\" to play again ", False, (0, 0, 25))
        msg_rect = msg_surf.get_rect(midtop = (self.screen_width/2, title_rect.bottom+100))
        pygame.draw.rect(self.screen, (156, 156, 156), msg_rect)        
        
        self.screen.blit(title_surf, title_rect)
        self.screen.blit(msg_surf, msg_rect)
        
    def kitty_drop(self):
        if self.kitties.sprites():
            random_kitty = choice(self.kitties.sprites())
            dropping = Bolt("kitty", 5, random_kitty.rect.midbottom, self.screen_height)
            self.kitty_droppings.add(dropping)
            
    def check_collisions(self):
        # Player bolts:
        if self.player.sprite.bolts:
            for bolt in self.player.sprite.bolts:
                if pygame.sprite.spritecollide(bolt, self.kitties, True):
                    bolt.kill()
                    self.score += 100
                    
        # Kitty droppings:
        if self.kitty_droppings:
            for dropping in self.kitty_droppings:
                if pygame.sprite.spritecollide(dropping, self.player, False):
                    self.health -= 1
                    if self.health <= 0:
                        self.dead = True
                    else:
                        dropping.kill()
                if dropping.rect.bottom >= self.screen_height - 50:
                    dropping.kill()
                    
        # Kitties:
        if self.kitties:
            for kitty in self.kitties:
                if pygame.sprite.spritecollide(kitty, self.player, False):
                    self.dead = True
                if kitty.rect.bottom >= self.screen_height - 50:
                    self.dead = True
                    
    def reset(self):
        self.score = 0
        self.health = 3
        self.dead = False
        self.player_sprite.rect.x = self.screen_width/2 - 34
        pygame.sprite.Group.empty(self.kitties)
        pygame.sprite.Group.empty(self.kitty_droppings)
        pygame.sprite.Group.empty(self.player.sprite.bolts)
                    
    def start(self):
        self.display_start()

    def run(self):
        self.player.update()
        self.kitties.update()
        self.kitty_droppings.update()
        self.check_collisions()
        
        self.player.draw(self.screen)
        self.kitties.draw(self.screen)
        self.player.sprite.bolts.draw(self.screen)
        self.kitty_droppings.draw(self.screen)
        self.display_score()
        
    def pause(self):
        self.display_pause()
        self.display_score()
        
    def game_over(self):
        self.display_game_over()
        self.display_score()
        