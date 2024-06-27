from sys import exit
import pygame
import asyncio
import setup
from game import Game
from kitties import Kitty
 
pygame.init()

# Game window:
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kitten Invaders")

# Game clock:
clock = pygame.time.Clock()

# Current game instance:
game = Game(screen, screen_width, screen_height)

# Background:
starfield_surf = pygame.Surface((screen_width, screen_height))
starfield_surf.fill((0, 0, 25))
setup.generate_starfield(starfield_surf, screen_width, screen_height - 50)

# Ground surface:    
ground_surf = pygame.Surface((screen_width, 50))
ground_surf.fill((64, 64, 64))
ground_rect = ground_surf.get_rect(bottomleft = (0, screen_height))

async def main():
    
    # Timers:
    enemy_timer = pygame.USEREVENT + 1
    enemy_spawn_rate = 2000
    pygame.time.set_timer(enemy_timer, enemy_spawn_rate)
    spawn_rate_decreaser = 200

    spawn_increase_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(spawn_increase_timer, 5000)

    drop_timer = pygame.USEREVENT + 3
    drop_rate = 5000
    pygame.time.set_timer(drop_timer, drop_rate)
        
    game_running = False
    game_paused = False

    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
                
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if not game_running:
                            if game.dead:
                                game.reset()
                                
                            game_running = True
                    
                    if event.key == pygame.K_p:
                        if game_running:
                            if game_paused:
                                game_paused = False
                            else:
                                game_paused = True
                            
            if game_running and not game_paused:
                
                if event.type == enemy_timer:
                    game.kitties.add(Kitty(screen_width, screen_height))
                    
                if event.type == spawn_increase_timer:
                    if enemy_spawn_rate <= 100:
                        enemy_spawn_rate = (2000 - spawn_rate_decreaser)
                        pygame.time.set_timer(enemy_timer, enemy_spawn_rate)
                        if spawn_rate_decreaser < 1800:
                            spawn_rate_decreaser += 200
                        print(enemy_spawn_rate)
                        print(spawn_rate_decreaser)    
                    else:
                        enemy_spawn_rate -= 100
                        pygame.time.set_timer(enemy_timer, enemy_spawn_rate)
                
                if event.type == drop_timer:
                    game.kitty_drop()
        
        # Draw background and ground:    
        screen.blit(starfield_surf, (0, 0))
        screen.blit(ground_surf, ground_rect)
        
        if game.dead:
            game_running = False
            game.game_over()
        
        elif game_running and not game_paused:
            game.run()
            
        elif game_running and game_paused:
            game.pause()

        else:
            game.start()
            
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)
            
asyncio.run(main())