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

# Music:
pygame.mixer.music.load("sounds/level-ix-medium.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# Sounds:
shoot_sound = pygame.mixer.Sound("sounds/bottle-pop.ogg")
shoot_sound.set_volume(0.8)

# Async func needed for pygame
async def main():
    
    # TIMERS:
    
    ## Enemy/kitty spawn timer:
    spawn_rate_initial = 2000
    spawn_rate_decreaser = 0
    spawn_rate = spawn_rate_initial - spawn_rate_decreaser
    spawn_timer = pygame.USEREVENT + 1

    ## Spawn rate increase timer:
    spawn_increase_rate = 5000
    spawn_increase_timer = pygame.USEREVENT + 2
    
    ## Enemy/kitty bomb timer:    
    bomb_drop_rate_initial = 5000
    bomb_drop_rate_decreaser = 0
    bomb_drop_rate = bomb_drop_rate_initial - bomb_drop_rate_decreaser
    bomb_drop_timer = pygame.USEREVENT + 3
             
    # Name input field for high score:
    name_input = InputField(250, 35, screen_width, screen_height)
    
    # SWITCHES:
    
    ## Game state swithces:
    game_running = False
    game_paused = False
    
    ## Music and sound effect switches:
    music_on = True
    sound_on = True
    
    ## Game screen switches:
    show_help = False
    show_hiscores = False
    show_controls = False
    show_sounds = False
    add_hiscore = False
    
    # GAME LOOP:
    
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            
            # Add high score screen:    
            if add_hiscore:
                
                ## Player name input field:
                name_input.handle_events(event)
                                          
                ## Keyboard setup:    
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
                                spawn_rate_decreaser = 0
                                spawn_rate = spawn_rate_initial - spawn_rate_decreaser
                                bomb_drop_rate_decreaser = 0
                                bomb_drop_rate = bomb_drop_rate_initial - bomb_drop_rate_decreaser
                                
                            pygame.time.set_timer(spawn_timer, spawn_rate)
                            pygame.time.set_timer(spawn_increase_timer, spawn_increase_rate)
                            pygame.time.set_timer(bomb_drop_timer, bomb_drop_rate)
                            
                            show_help = False
                            show_controls = False
                            show_hiscores = False
                            show_sounds = False   
                            game_running = True
                            
                            # TESTING:
                            print(f"Spawn rate: {spawn_rate}")
                            print(f"Bomb drop rate: {bomb_drop_rate}")
                            
                    # Right-shift:
                    if event.key == pygame.K_RSHIFT:
                        if game_running and not game_paused:
                            if game.controls == 2:
                                if sound_on:
                                    shoot_sound.play()
                                if game.score > 0:
                                    game.score -= 10
                            
                    # Space:
                    if event.key == pygame.K_SPACE:
                        if game_running and not game_paused:
                            if game.controls == 1:
                                if sound_on:
                                    shoot_sound.play()
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
                            show_sounds = False
                            show_hiscores = False
                            
                    # H:
                    if event.key == pygame.K_h:
                        if not game_running:
                            show_help = True
                            show_controls = False
                            show_sounds = False
                            show_hiscores = False

                    # M:
                    if event.key == pygame.K_m:
                        if not game_running:
                            show_help = False
                            show_controls = False
                            show_sounds = False
                            show_hiscores = False

                    # P:
                    if event.key == pygame.K_p:
                        if game_running:
                            if game_paused:
                                '''Loads saved timer values, sets timers and unpauses game'''
                                spawn_rate = spawn_rate_on_pause
                                spawn_rate_decreaser = spawn_rate_decreaser_on_pause
                                pygame.time.set_timer(spawn_timer, spawn_rate)
                                bomb_drop_rate = bomb_drop_rate_on_pause
                                bomb_drop_rate_decreaser = bomb_drop_rate_decreaser_on_pause
                                pygame.time.set_timer(bomb_drop_timer, bomb_drop_rate)
                                game_paused = False
                            else:
                                '''Saves timer values and pauses game'''
                                spawn_rate_on_pause = spawn_rate
                                spawn_rate_decreaser_on_pause = spawn_rate_decreaser
                                bomb_drop_rate_on_pause = bomb_drop_rate
                                bomb_drop_rate_decreaser_on_pause = bomb_drop_rate_decreaser
                                game_paused = True

                    # Q (disabled for deployment on itch.io; in screens.py also):
                    # if event.key == pygame.K_q:
                    #     if not game_running:
                    #         exit()

                    # S:
                    if event.key == pygame.K_s:
                        if not game_running:
                            show_help = False
                            show_controls = False
                            show_sounds = False
                            show_hiscores = True
                            
                    # U:
                    if event.key == pygame.K_u:
                        if not game_running:
                            show_help = False
                            show_controls = False
                            show_sounds = True
                            show_hiscores = False

                    # X:
                    if event.key == pygame.K_x:
                        if show_sounds:
                            sound_on = not sound_on
                            if sound_on:
                                game.sound_on = True
                            else:
                                game.sound_on = False
                                
                    # Z:
                    if event.key == pygame.K_z:
                        if show_sounds:
                            music_on = not music_on
                            if music_on:
                                pygame.mixer.music.play(-1)
                            else:
                                pygame.mixer.music.stop()
                                
            # Timers action:                
            if game_running and not game_paused:

                ## Enemy spawn timer:
                '''Adds a kitty sprite to the kitty sprite group.'''
                if event.type == spawn_timer:
                    game.kitties.add(Kitty(screen_width, screen_height))

                ## Enemy spawn increase timer:
                '''Decreases enemy spawn time by 100 ms.'''
                '''If enemy spawn rate is down to 100 ms, it's reset, 
                starting a new attack wave. At the same time 200 ms is 
                added to the spawn rate decreaser, starting each wave 
                off with more enemies, making the game successively harder.'''
                '''Once the decreaser is up to 1800 ms, enemy spawning is 
                reset to initial values, starting a new series of attack 
                waves. At this time, the time between enemy bombs is decreased 
                by 1000 ms, making the game a bit more challenging.'''
                '''Timers are set with their new values.'''
                if event.type == spawn_increase_timer:
                    if spawn_rate <= 100:
                        if spawn_rate_decreaser < 1800:
                            spawn_rate_decreaser += 200
                        else:
                            spawn_rate_decreaser = 0
                            if bomb_drop_rate > 1000:
                                bomb_drop_rate_decreaser += 1000
                                bomb_drop_rate = bomb_drop_rate_initial - bomb_drop_rate_decreaser
                                pygame.time.set_timer(bomb_drop_timer, bomb_drop_rate)
                        spawn_rate = spawn_rate_initial - spawn_rate_decreaser
                        
                        # TESTING:
                        print(f"Spawn rate: {spawn_rate}")
                        print(f"Bomb drop rate: {bomb_drop_rate}")
                        
                    else:
                        spawn_rate -= 100
                    pygame.time.set_timer(spawn_timer, spawn_rate)

                # Enemy projectile spawn:
                '''Makes a random kitty drop a bomb'''
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
            '''Displays pause screen, player health bar and game score.'''
            screens.display_pause(screen, screen_width, screen_height)
            game.display_health()
            game.display_score()
            
        # Show hi-scores:
        elif show_hiscores:
            screens.display_hiscores(screen, screen_width, screen_height)

        # Show help:
        elif show_help:
            screens.display_help(screen, screen_width, screen_height)

        # Show control settings:
        elif show_controls:
            '''Displays control settings, and draws a rectangle around 
            the selected setting.'''
            screens.display_controls(screen, screen_width, screen_height)
            cont_y = 219
            cont_width = 223
            cont_height = 44
            if game.controls == 1:
                chosen = pygame.rect.Rect(screen_width/4 - 53, cont_y, cont_width, cont_height)
            elif game.controls == 2:
                chosen = pygame.rect.Rect(screen_width/2 + 47, cont_y, cont_width, cont_height)
            pygame.draw.rect(screen, (0, 255, 255), chosen, 2)
            
        # Show sound settings:
        elif show_sounds:
            '''Displays music and sound settings, and draws rectangles 
            around the selected choices.'''
            screens.display_sounds(screen, screen_width, screen_height)
            
            y_on = 297
            y_off = 342
            sndset_height = 31
            
            ## Music:
            music_x = screen_width/4 - 53
            if music_on:
                music_chosen = pygame.rect.Rect(music_x, y_on, 152, sndset_height)
            else:
                music_chosen = pygame.rect.Rect(music_x, y_off, 163, sndset_height)
            pygame.draw.rect(screen, (0, 255, 255), music_chosen, 2)
            
            ## Sound FX:
            sound_x = screen_width/2 + 47
            if sound_on:
                sound_chosen = pygame.rect.Rect(sound_x, y_on, 242, sndset_height)
            else:
                sound_chosen = pygame.rect.Rect(sound_x, y_off, 253, sndset_height)
            pygame.draw.rect(screen, (0, 255, 255), sound_chosen, 2)         
            
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
