import pygame
from hiscores import read_hiscores

pygame.font.init()

# Fonts:
font_title = pygame.font.Font("fonts/PixeloidSansBold-PKnYd.ttf", 50)
font_regular = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 30)
font_small = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 20)
font_score = pygame.font.Font("fonts/PixeloidMono-d94EV.ttf", 20)

line_spacing = 20

# Menu for start and game over screens:
def display_menu(screen, screen_width, y_pos):
    
    hiscores_surf = font_small.render(" S - Show high scores ", False, (0, 0, 51))
    hiscores_rect = hiscores_surf.get_rect(midtop = (screen_width/2, y_pos))
    pygame.draw.rect(screen, (204, 204, 204), hiscores_rect)        

    controls_surf = font_small.render(" G - Game controls ", False, (0, 0, 51))
    controls_rect = controls_surf.get_rect(topleft = (hiscores_rect.left, hiscores_rect.bottom + line_spacing))
    pygame.draw.rect(screen, (204, 204, 204), controls_rect)        

    help_surf = font_small.render(" H - How to play ", False, (0, 0, 51))
    help_rect = help_surf.get_rect(topleft = (hiscores_rect.left, controls_rect.bottom + line_spacing))
    pygame.draw.rect(screen, (204, 204, 204), help_rect)
    
    # quit_surf = font_small.render(" Q - Quit game ", False, (0, 0, 51))
    # quit_rect = quit_surf.get_rect(topleft = (hiscores_rect.left, help_rect.bottom + line_spacing))
    # pygame.draw.rect(screen, (204, 204, 204), quit_rect)        

    screen.blit(hiscores_surf, hiscores_rect)
    screen.blit(controls_surf, controls_rect)
    screen.blit(help_surf, help_rect)
    # screen.blit(quit_surf, quit_rect)

# Back to main screen -footer:    
def display_back_to_main(screen, screen_width, y_pos):
    
    main_screen_surf = font_small.render(" M - Main menu ", False, (0, 0, 51))
    main_screen_rect = main_screen_surf.get_rect(midtop = (screen_width/2, y_pos))
    pygame.draw.rect(screen, (204, 204, 204), main_screen_rect)     
    
    screen.blit(main_screen_surf, main_screen_rect)  

# Start screen:
def display_start(screen, screen_width, screen_height):
    
    title_surf = font_title.render("Kitten Invaders", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/5))
    
    subtitle_surf = font_regular.render(" Push \"Enter\" to play ", False, (0, 0, 51))
    subtitle_rect = subtitle_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), subtitle_rect)        
    
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle_surf, subtitle_rect)
    display_menu(screen, screen_width, subtitle_rect.bottom + line_spacing * 2)
    
# Hi-scores screen:
def display_hiscores(screen, screen_width, screen_height):
    
    title_surf = font_title.render("High scores", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/5))
    
    screen.blit(title_surf, title_rect)
    
    high_scores = read_hiscores()
    i = 0
    
    for entry in high_scores:
        score = entry[0]
        player = entry[1]
        date = entry[2]
        
        score_surf = font_small.render(f" {str(score)} ", False, (0, 0, 51))
        score_rect = score_surf.get_rect(topright = (screen_width/2 - 180, title_rect.bottom + line_spacing * (2+i)))
        pygame.draw.rect(screen, (204, 204, 204), score_rect)
        
        player_surf = font_small.render(f" {player} ", False, (0, 0, 51))
        player_rect = player_surf.get_rect(topleft = (screen_width/2 - 150, title_rect.bottom + line_spacing * (2+i)))
        pygame.draw.rect(screen, (204, 204, 204), player_rect)
        
        date_surf = font_small.render(f" {date} ", False, (0, 0, 51))
        date_rect = date_surf.get_rect(topleft = (screen_width/2 + 150, title_rect.bottom + line_spacing * (2+i)))
        pygame.draw.rect(screen, (204, 204, 204), date_rect)
        
        screen.blit(score_surf, score_rect)
        screen.blit(player_surf, player_rect)
        screen.blit(date_surf, date_rect)
        
        i += 1
        if i >= 10:
            break

    display_back_to_main(screen, screen_width, title_rect.bottom + line_spacing * (4+i))
    
# Game controls screen:
def display_controls(screen, screen_width, screen_height):
    
    title_surf = font_title.render("Game controls", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/5))
    
    # Controls 1:
    subtitle1_surf = font_regular.render(" 1 - controls: ", False, (0, 0, 51))
    subtitle1_rect = subtitle1_surf.get_rect(topleft = (screen_width/4 - 50, title_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), subtitle1_rect)
    
    msg1_1_surf = font_small.render(" l-arrow: move left ", False, (0, 0, 51))
    msg1_1_rect = msg1_1_surf.get_rect(topleft = (screen_width/4 - 50, subtitle1_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), msg1_1_rect)

    msg1_2_surf = font_small.render(" r-arrow: move right ", False, (0, 0, 51))
    msg1_2_rect = msg1_2_surf.get_rect(topleft = (screen_width/4 - 50, msg1_1_rect.bottom + line_spacing))
    pygame.draw.rect(screen, (204, 204, 204), msg1_2_rect)     
        
    msg1_3_surf = font_small.render(" space: shoot ", False, (0, 0, 51))
    msg1_3_rect = msg1_3_surf.get_rect(topleft = (screen_width/4 - 50, msg1_2_rect.bottom + line_spacing))
    pygame.draw.rect(screen, (204, 204, 204), msg1_3_rect)
    
    # Controls 2:
    subtitle2_surf = font_regular.render(" 2 - controls: ", False, (0, 0, 51))
    subtitle2_rect = subtitle2_surf.get_rect(topleft = (screen_width/2 + 50, title_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), subtitle2_rect)
    
    msg2_1_surf = font_small.render(" A: move left ", False, (0, 0, 51))
    msg2_1_rect = msg2_1_surf.get_rect(topleft = (screen_width/2 + 50, subtitle1_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), msg2_1_rect)

    msg2_2_surf = font_small.render(" D: move right ", False, (0, 0, 51))
    msg2_2_rect = msg2_2_surf.get_rect(topleft = (screen_width/2 + 50, msg2_1_rect.bottom + line_spacing))
    pygame.draw.rect(screen, (204, 204, 204), msg2_2_rect)     
        
    msg2_3_surf = font_small.render(" r-shift: shoot ", False, (0, 0, 51))
    msg2_3_rect = msg2_3_surf.get_rect(topleft = (screen_width/2 + 50, msg2_2_rect.bottom + line_spacing))
    pygame.draw.rect(screen, (204, 204, 204), msg2_3_rect)
      
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle1_surf, subtitle1_rect)
    screen.blit(msg1_1_surf, msg1_1_rect)
    screen.blit(msg1_2_surf, msg1_2_rect)
    screen.blit(msg1_3_surf, msg1_3_rect)
    screen.blit(subtitle2_surf, subtitle2_rect)
    screen.blit(msg2_1_surf, msg2_1_rect)
    screen.blit(msg2_2_surf, msg2_2_rect)
    screen.blit(msg2_3_surf, msg2_3_rect)
    display_back_to_main(screen, screen_width, msg1_3_rect.bottom + line_spacing * 2)

# Help screen:
def display_help(screen, screen_width, screen_height):
    
    title_surf = font_title.render("How to play", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/5))
    
    msg1_a_surf = font_small.render(" Use keyboard to move left <-> right ", False, (0, 0, 51))
    msg1_a_rect = msg1_a_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), msg1_a_rect)
    
    msg1_b_surf = font_small.render(" and shoot (see Game controls). ", False, (0, 0, 51))
    msg1_b_rect = msg1_b_surf.get_rect(topleft = (msg1_a_rect.left, msg1_a_rect.bottom))
    pygame.draw.rect(screen, (204, 204, 204), msg1_b_rect)

    msg2_a_surf = font_small.render(" Avoid falling enemy projectiles and ", False, (0, 0, 51))
    msg2_a_rect = msg2_a_surf.get_rect(topleft = (msg1_a_rect.left, msg1_b_rect.bottom + line_spacing))
    pygame.draw.rect(screen, (204, 204, 204), msg2_a_rect)        

    msg2_b_surf = font_small.render(" descending kittens! ", False, (0, 0, 51))
    msg2_b_rect = msg2_b_surf.get_rect(topleft = (msg1_a_rect.left, msg2_a_rect.bottom))
    pygame.draw.rect(screen, (204, 204, 204), msg2_b_rect)        

    msg3_a_surf = font_small.render(" Do not let invading kittens reach ", False, (0, 0, 51))
    msg3_a_rect = msg3_a_surf.get_rect(topleft = (msg1_a_rect.left, msg2_b_rect.bottom + line_spacing))
    pygame.draw.rect(screen, (204, 204, 204), msg3_a_rect)    
    
    msg3_b_surf = font_small.render(" the ground! ", False, (0, 0, 51))
    msg3_b_rect = msg3_b_surf.get_rect(topleft = (msg1_a_rect.left, msg3_a_rect.bottom))
    pygame.draw.rect(screen, (204, 204, 204), msg3_b_rect)    
    
    screen.blit(title_surf, title_rect)
    screen.blit(msg1_a_surf, msg1_a_rect)
    screen.blit(msg1_b_surf, msg1_b_rect)
    screen.blit(msg2_a_surf, msg2_a_rect)
    screen.blit(msg2_b_surf, msg2_b_rect)
    screen.blit(msg3_a_surf, msg3_a_rect)
    screen.blit(msg3_b_surf, msg3_b_rect)
    display_back_to_main(screen, screen_width, msg3_b_rect.bottom + line_spacing * 2)

# Pause screen
def display_pause(screen, screen_width, screen_height):
    
    pause_surf = font_title.render("Game paused", False, (204, 204, 204))
    pause_rect = pause_surf.get_rect(midtop = (screen_width/2, screen_height/5))
    
    subtitle_surf = font_regular.render(" Push \"P\" to continue ", False, (0, 0, 51))
    subtitle_rect = subtitle_surf.get_rect(midtop = (screen_width/2, pause_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), subtitle_rect)
    
    screen.blit(pause_surf, pause_rect)
    screen.blit(subtitle_surf, subtitle_rect)

# Game over screen:    
def display_game_over(screen, screen_width, screen_height):
    
    title_surf = font_title.render("Game over!", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/5))
    
    subtitle_surf = font_regular.render(" Push \"Enter\" to play again ", False, (0, 0, 51))
    subtitle_rect = subtitle_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), subtitle_rect)        
    
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle_surf, subtitle_rect)
    display_menu(screen, screen_width, subtitle_rect.bottom + line_spacing * 2)
    
# Add high score screen:    
def display_add_highscore(screen, screen_width, screen_height):
    
    title_surf = font_title.render("New high score!", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/5))
    
    msg_surf = font_small.render(" Add player name and push \"Enter\" ", False, (0, 0, 51))
    msg_rect = msg_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + line_spacing * 2))
    pygame.draw.rect(screen, (204, 204, 204), msg_rect)
    
    screen.blit(title_surf, title_rect)
    screen.blit(msg_surf, msg_rect)
