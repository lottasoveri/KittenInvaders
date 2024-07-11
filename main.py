from sys import exit
import pygame, asyncio
import setup, screens
from game import Game
from kitties import Kitty
from input_field import InputField
from hiscores import check_highscore, write_hiscores
 
pygame.init()

# Game window:
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kitten Invaders")

# Game clock:
clock = pygame.time.Clock()

# Current game instance:
game = Game(screen, screen_width, screen_height)

# Background:
starfield_surf = pygame.Surface((screen_width, screen_height))
starfield_surf.fill((0, 0, 51))
setup.generate_starfield(starfield_surf, screen_width, screen_height - 50)

# Ground surface:    
ground_surf = pygame.Surface((screen_width, 50))
ground_surf.fill((51, 51, 51))
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
        
    # Name input for high score
    name_input = InputField(250, 35, screen_width, screen_height)
    
    game_running = False
    game_paused = False
    show_help = False
    show_hiscores = False
    show_controls = False
    add_hiscore = False
    
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            
            # Add high score screen:    
            if add_hiscore:
                
                # Player input:
                name_input.handle_events(event)
                                          
                # Keyboard setup:    
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        write_hiscores(name_input.text.strip(), game.score)
                        name_input.clear()
                        add_hiscore = False
                        show_hiscores = True

            else:
                
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
                            show_help = False
                            show_controls = False
                            show_hiscores = False                            
                            game_running = True
                            
                    # Right-shift:
                    if event.key == pygame.K_RSHIFT:
                        if game_running and not game_paused:
                            if game.controls == 2:
                                if game.score > 0:
                                    game.score -= 10
                            
                    # Space:
                    if event.key == pygame.K_SPACE:
                        if game_running and not game_paused:
                            if game.controls == 1:
                                if game.score > 0:
                                    game.score -= 10
                            
                    # 1:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                        if show_controls:
                            game.controls = 1
                            game.update_controls()

                    # 2:
                    if event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                        if show_controls:
                            game.controls = 2
                            game.update_controls()

                    # G:
                    if event.key == pygame.K_g:
                        if not game_running:
                            show_help = False
                            show_controls = True
                            show_hiscores = False
                            
                    # H:
                    if event.key == pygame.K_h:
                        if not game_running:
                            show_help = True
                            show_controls = False
                            show_hiscores = False

                    # M:
                    if event.key == pygame.K_m:
                        if not game_running:
                            show_help = False
                            show_controls = False
                            show_hiscores = False

                    # P:
                    if event.key == pygame.K_p:
                        if game_running:
                            if game_paused:
                                game_paused = False
                            else:
                                game_paused = True

                    # Q:
                    # if event.key == pygame.K_q:
                    #     if not game_running:
                    #         exit()

                    # S:
                    if event.key == pygame.K_s:
                        if not game_running:
                            show_help = False
                            show_controls = False
                            show_hiscores = True
                            
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

        # Run game:
        if game_running and not game_paused and not game.over:
            game.run()

        # Game paused:
        elif game_running and game_paused:
            screens.display_pause(screen, screen_width, screen_height)
            game.display_health()
            game.display_score()
            
        # Show hi-scores:
        elif show_hiscores:
            screens.display_hiscores(screen, screen_width, screen_height)

        # Show help:
        elif show_help:
            screens.display_help(screen, screen_width, screen_height)

        # Show settings:
        elif show_controls:
            screens.display_controls(screen, screen_width, screen_height)
            y_pos = 219
            width = 223
            height = 44
            if game.controls == 1:
                chosen = pygame.rect.Rect(screen_width/4 - 53, y_pos, width, height)
            elif game.controls == 2:
                chosen = pygame.rect.Rect(screen_width/2 + 47, y_pos, width, height)
            pygame.draw.rect(screen, (0, 255, 255), chosen, 2)
            
        # Game over:
        elif game.over:
            game_running = False
            if check_highscore(game.score):
                add_hiscore = True
                screens.display_add_highscore(screen, screen_width, screen_height)
                name_input.draw(screen)
                game.display_score()
            else:
                screens.display_game_over(screen, screen_width, screen_height)
                game.display_score()
            
        # Show start-screen:
        else:
            screens.display_start(screen, screen_width, screen_height)

        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)
  
asyncio.run(main())
