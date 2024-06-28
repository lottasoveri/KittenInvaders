from sys import exit
import pygame
import asyncio
import setup
import screens
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
    spawn_rate = 2000    
    spawn_rate_decreaser = 200
    bomb_drop_rate = 5000
        
    spawn_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_timer, spawn_rate)

    spawn_increase_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(spawn_increase_timer, 5000)

    bomb_drop_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(bomb_drop_timer, bomb_drop_rate)
        
    game_running = False
    game_paused = False
    show_help = False
    show_hiscores = False
    show_settings = False
    
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            
            # Keyboard setup:    
            if event.type == pygame.KEYDOWN:
                
                    # Enter:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if not game_running:
                            if game.over:
                                game.reset()
                                spawn_rate = 2000
                                spawn_rate_decreaser = 200
                                bomb_drop_rate = 5000
                                pygame.time.set_timer(spawn_timer, spawn_rate)
                                pygame.time.set_timer(spawn_increase_timer, 5000)
                                pygame.time.set_timer(bomb_drop_timer, bomb_drop_rate)
                            game_running = True

                    # B:
                    if event.key == pygame.K_b:
                        if not game_running:
                            show_help = False
                            show_settings = False
                            show_hiscores = False

                    # H:
                    if event.key == pygame.K_h:
                        if not game_running:
                            show_help = True
                            show_settings = False
                            show_hiscores = False

                    # L:
                    if event.key == pygame.K_l:
                        if not game_running:
                            show_help = False
                            show_settings = False
                            show_hiscores = True

                    # P:
                    if event.key == pygame.K_p:
                        if game_running:
                            if game_paused:
                                game_paused = False
                            else:
                                game_paused = True

                    # S:
                    if event.key == pygame.K_s:
                        if not game_running:
                            show_help = False
                            show_settings = True
                            show_hiscores = False
                            
            # Timers setup:                
            if game_running and not game_paused:

                # Spawn enemy:
                if event.type == spawn_timer:
                    game.kitties.add(Kitty(screen_width, screen_height))

                # Increase enemy spawn rate:
                if event.type == spawn_increase_timer:
                    if spawn_rate <= 100:
                        spawn_rate = (2000 - spawn_rate_decreaser)
                        pygame.time.set_timer(spawn_timer, spawn_rate)
                        if spawn_rate_decreaser < 1800:
                            spawn_rate_decreaser += 200
                        print(spawn_rate)               # TESTING
                        print(spawn_rate_decreaser)     # TESTING
                    else:
                        spawn_rate -= 100
                        pygame.time.set_timer(spawn_timer, spawn_rate)

                # Enemy projectile spawn:
                if event.type == bomb_drop_timer:
                    game.kitty_drop()

        # Draw background and ground:    
        screen.blit(starfield_surf, (0, 0))
        screen.blit(ground_surf, ground_rect)

        # Game over:
        if game.over:
            game_running = False
            screens.display_game_over(screen, screen_width, screen_height)
            
        # Run game:
        elif game_running and not game_paused:
            game.run()

        # Game paused:
        elif game_running and game_paused:
            screens.display_pause(screen, screen_width, screen_height)

        # Show hi-scores:
        elif show_hiscores:
            screens.display_hiscores(screen, screen_width, screen_height)

        # Show help:
        elif show_help:
            screens.display_help(screen, screen_width, screen_height)

        # Show settings:
        elif show_settings:
            screens.display_settings(screen, screen_width, screen_height)

        # Show start-screen:
        else:
            screens.display_start(screen, screen_width, screen_height)

        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)
  
asyncio.run(main())
