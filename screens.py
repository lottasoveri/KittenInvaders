import pygame

pygame.font.init()

# Fonts:
font_title = pygame.font.Font("fonts/PixeloidSansBold-PKnYd.ttf", 50)
font_regular = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 30)
font_small = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 20)
font_score = pygame.font.Font("fonts/PixeloidMono-d94EV.ttf", 20)

# Start screen:
def display_start(screen, screen_width, screen_height):
    
    title_surf = font_title.render("Kitten Invaders", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/4))
    
    subtitle_surf = font_regular.render(" Push \"Enter\" to play ", False, (0, 0, 51))
    subtitle_rect = subtitle_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 100))
    pygame.draw.rect(screen, (204, 204, 204), subtitle_rect)        
    
    hiscores_surf = font_small.render(" S - Show high scores ", False, (0, 0, 51))
    hiscores_rect = hiscores_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 200))
    pygame.draw.rect(screen, (204, 204, 204), hiscores_rect)        

    settings_surf = font_small.render(" G - Game controls ", False, (0, 0, 51))
    settings_rect = settings_surf.get_rect(topleft = (hiscores_rect.left, title_rect.bottom + 250))
    pygame.draw.rect(screen, (204, 204, 204), settings_rect)        

    help_surf = font_small.render(" H - How to play ", False, (0, 0, 51))
    help_rect = help_surf.get_rect(topleft = (hiscores_rect.left, title_rect.bottom + 300))
    pygame.draw.rect(screen, (204, 204, 204), help_rect)
    
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle_surf, subtitle_rect)
    screen.blit(hiscores_surf, hiscores_rect)
    screen.blit(settings_surf, settings_rect)
    screen.blit(help_surf, help_rect)

# Hi-scores screen:
def display_hiscores(screen, screen_width, screen_height):
    
    title_surf = font_title.render("High scores", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/4))
    
    subtitle_surf = font_regular.render(" Nothing here yet... ", False, (0, 0, 51))
    subtitle_rect = subtitle_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 75))
    pygame.draw.rect(screen, (204, 204, 204), subtitle_rect)
    
    main_screen_surf = font_small.render(" M - Main menu ", False, (0, 0, 51))
    main_screen_rect = main_screen_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 200))
    pygame.draw.rect(screen, (204, 204, 204), main_screen_rect)     
    
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle_surf, subtitle_rect)
    screen.blit(main_screen_surf, main_screen_rect)
    
# Settings screen:
def display_settings(screen, screen_width, screen_height):
    
    title_surf = font_title.render("Game controls", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/4))
    
    subtitle1_surf = font_regular.render(" 1 - controls: ", False, (0, 0, 51))
    subtitle1_rect = subtitle1_surf.get_rect(topleft = (screen_width/4, title_rect.bottom + 75))
    pygame.draw.rect(screen, (204, 204, 204), subtitle1_rect)
    
    subtitle2_surf = font_regular.render(" 2 - controls: ", False, (0, 0, 51))
    subtitle2_rect = subtitle2_surf.get_rect(topleft = (screen_width/2 + 100, title_rect.bottom + 75))
    pygame.draw.rect(screen, (204, 204, 204), subtitle2_rect)
    
    msg1_1_surf = font_small.render(" l-arrow: move left ", False, (0, 0, 51))
    msg1_1_rect = msg1_1_surf.get_rect(topleft = (screen_width/4, title_rect.bottom + 150))
    pygame.draw.rect(screen, (204, 204, 204), msg1_1_rect)

    msg1_2_surf = font_small.render(" r-arrow: move right ", False, (0, 0, 51))
    msg1_2_rect = msg1_2_surf.get_rect(topleft = (screen_width/4, title_rect.bottom + 200))
    pygame.draw.rect(screen, (204, 204, 204), msg1_2_rect)     
        
    msg1_3_surf = font_small.render(" space: shoot ", False, (0, 0, 51))
    msg1_3_rect = msg1_3_surf.get_rect(topleft = (screen_width/4, title_rect.bottom + 250))
    pygame.draw.rect(screen, (204, 204, 204), msg1_3_rect)
    
    msg2_1_surf = font_small.render(" A: move left ", False, (0, 0, 51))
    msg2_1_rect = msg2_1_surf.get_rect(topleft = (screen_width/2 + 100, title_rect.bottom + 150))
    pygame.draw.rect(screen, (204, 204, 204), msg2_1_rect)

    msg2_2_surf = font_small.render(" D: move right ", False, (0, 0, 51))
    msg2_2_rect = msg2_2_surf.get_rect(topleft = (screen_width/2 + 100, title_rect.bottom + 200))
    pygame.draw.rect(screen, (204, 204, 204), msg2_2_rect)     
        
    msg2_3_surf = font_small.render(" r-shift: shoot ", False, (0, 0, 51))
    msg2_3_rect = msg2_3_surf.get_rect(topleft = (screen_width/2 + 100, title_rect.bottom + 250))
    pygame.draw.rect(screen, (204, 204, 204), msg2_3_rect)
    
    main_screen_surf = font_small.render(" M - Main menu ", False, (0, 0, 51))
    main_screen_rect = main_screen_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 350))
    pygame.draw.rect(screen, (204, 204, 204), main_screen_rect)
      
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle1_surf, subtitle1_rect)
    screen.blit(subtitle2_surf, subtitle2_rect)
    screen.blit(msg1_1_surf, msg1_1_rect)
    screen.blit(msg1_2_surf, msg1_2_rect)
    screen.blit(msg1_3_surf, msg1_3_rect)
    screen.blit(msg2_1_surf, msg2_1_rect)
    screen.blit(msg2_2_surf, msg2_2_rect)
    screen.blit(msg2_3_surf, msg2_3_rect)
    screen.blit(main_screen_surf, main_screen_rect)
    
# Help screen:
def display_help(screen, screen_width, screen_height):
    
    title_surf = font_title.render("How to play", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/4))
    
    msg1_a_surf = font_small.render(" Use keyboard to move left <-> right ", False, (0, 0, 51))
    msg1_a_rect = msg1_a_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 75))
    pygame.draw.rect(screen, (204, 204, 204), msg1_a_rect)
    
    msg1_b_surf = font_small.render(" and shoot (see Game controls). ", False, (0, 0, 51))
    msg1_b_rect = msg1_b_surf.get_rect(topleft = (msg1_a_rect.left, title_rect.bottom + 100))
    pygame.draw.rect(screen, (204, 204, 204), msg1_b_rect)

    msg2_a_surf = font_small.render(" Avoid falling enemy projectiles and ", False, (0, 0, 51))
    msg2_a_rect = msg2_a_surf.get_rect(topleft = (msg1_a_rect.left, title_rect.bottom + 150))
    pygame.draw.rect(screen, (204, 204, 204), msg2_a_rect)        

    msg2_b_surf = font_small.render(" descending kittens! ", False, (0, 0, 51))
    msg2_b_rect = msg2_b_surf.get_rect(topleft = (msg1_a_rect.left, title_rect.bottom + 175))
    pygame.draw.rect(screen, (204, 204, 204), msg2_b_rect)        

    msg3_a_surf = font_small.render(" Do not let invading kittens reach ", False, (0, 0, 51))
    msg3_a_rect = msg3_a_surf.get_rect(topleft = (msg1_a_rect.left, title_rect.bottom + 225))
    pygame.draw.rect(screen, (204, 204, 204), msg3_a_rect)    
    
    msg3_b_surf = font_small.render(" the ground! ", False, (0, 0, 51))
    msg3_b_rect = msg3_b_surf.get_rect(topleft = (msg1_a_rect.left, title_rect.bottom + 250))
    pygame.draw.rect(screen, (204, 204, 204), msg3_b_rect)    
    
    main_screen_surf = font_small.render(" M - Main menu ", False, (0, 0, 51))
    main_screen_rect = main_screen_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 350))
    pygame.draw.rect(screen, (204, 204, 204), main_screen_rect)
    
    screen.blit(title_surf, title_rect)
    screen.blit(msg1_a_surf, msg1_a_rect)
    screen.blit(msg1_b_surf, msg1_b_rect)
    screen.blit(msg2_a_surf, msg2_a_rect)
    screen.blit(msg2_b_surf, msg2_b_rect)
    screen.blit(msg3_a_surf, msg3_a_rect)
    screen.blit(msg3_b_surf, msg3_b_rect)
    screen.blit(main_screen_surf, main_screen_rect)

# Pause screen
def display_pause(screen, screen_width, screen_height):
    
    pause_surf = font_title.render("Game paused", False, (204, 204, 204))
    pause_rect = pause_surf.get_rect(midtop = (screen_width/2, screen_height/4))
    
    subtitle_surf = font_regular.render(" Push \"P\" to continue ", False, (0, 0, 51))
    subtitle_rect = subtitle_surf.get_rect(midtop = (screen_width/2, pause_rect.bottom + 100))
    pygame.draw.rect(screen, (204, 204, 204), subtitle_rect)
    
    screen.blit(pause_surf, pause_rect)
    screen.blit(subtitle_surf, subtitle_rect)

# Game over screen:    
def display_game_over(screen, screen_width, screen_height):
    
    title_surf = font_title.render("Game over!", False, (204, 204, 204))
    title_rect = title_surf.get_rect(midtop = (screen_width/2, screen_height/4))
    
    subtitle_surf = font_regular.render(" Push \"Enter\" to play again ", False, (0, 0, 51))
    subtitle_rect = subtitle_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 100))
    pygame.draw.rect(screen, (204, 204, 204), subtitle_rect)        
    
    msg1_surf = font_small.render(" S - Show high scores ", False, (0, 0, 51))
    msg1_rect = msg1_surf.get_rect(midtop = (screen_width/2, title_rect.bottom + 200))
    pygame.draw.rect(screen, (204, 204, 204), msg1_rect)        

    msg2_surf = font_small.render(" G - Game controls ", False, (0, 0, 51))
    msg2_rect = msg2_surf.get_rect(topleft = (msg1_rect.left, title_rect.bottom + 250))
    pygame.draw.rect(screen, (204, 204, 204), msg2_rect)        

    msg3_surf = font_small.render(" H - How to play ", False, (0, 0, 51))
    msg3_rect = msg3_surf.get_rect(topleft = (msg1_rect.left, title_rect.bottom + 300))
    pygame.draw.rect(screen, (204, 204, 204), msg3_rect)        
    
    screen.blit(title_surf, title_rect)
    screen.blit(subtitle_surf, subtitle_rect)
    screen.blit(msg1_surf, msg1_rect)
    screen.blit(msg2_surf, msg2_rect)
    screen.blit(msg3_surf, msg3_rect)