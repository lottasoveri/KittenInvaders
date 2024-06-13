import pygame
from random import randrange, choice
from sys import exit

# FUNCTIONS:

def generate_starfield(surface):
    star_coords = []
    star_counter = 0
    while star_counter < 200:
        star = {}
        star["star_x"] = randrange(1, screen.get_width())
        star["star_y"] = randrange(1, screen.get_height()-50)
        star["star_size"] = choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3])
        star_coords.append(star)
        star_counter += 1
        for star in star_coords:
            pygame.draw.circle(surface, 
                               (204, 229, 255), 
                               (star["star_x"], star["star_y"]), 
                               star["star_size"]
                               )
    
def enemy_movement(enemy_list: list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.y += 1
            if enemy_rect.height < 95:
                screen.blit(kitty2_surf, enemy_rect)
            elif enemy_rect.height < 100:
                screen.blit(kitty4_surf, enemy_rect)
            else:
                screen.blit(kitty3_surf, enemy_rect)
        enemy_list = [enemy for enemy in enemy_list if enemy.y < (screen.get_height() + 100)]    
        return enemy_list
    else:
        return []
    
def bolt_movement(bolt_list: list):
    if bolt_list:
        for bolt_rect in bolt_list:
            bolt_rect.y -= 5
            if bolt_rect.height < 30:
                screen.blit(bolt1_surf, bolt_rect)
            else:
                screen.blit(bolt2_surf, bolt_rect)
        bolt_list = [bolt for bolt in bolt_list if bolt.y > 0]    
        return bolt_list
    else:
        return []
        
def bolt_collision(bolts, enemies):
    global game_score
    if enemies:
        for enemy_rect in enemies:
            for bolt_rect in bolts:
                if enemy_rect.colliderect(bolt_rect):
                    enemy_rect.y = screen.get_height() +100
                    bolt_rect.y = -200
                    game_score += 100
                    
def ground_collision(ground, enemies):
    global game_active
    if enemies:
        for enemy_rect in enemies:
            if enemy_rect.colliderect(ground):
                game_active = False

def display_score(score):
    score_surf = font_score.render(f" Score: {score} ", False, (0, 0, 25))
    score_rect = score_surf.get_rect(center = (screen.get_width()/2, screen.get_height()-25))
    pygame.draw.rect(screen, (156, 156, 156), score_rect)
    screen.blit(score_surf, score_rect)
    
# GAME ELEMENTS:
    
pygame.init()

screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("Kitten Invaders")
clock = pygame.time.Clock()

font_title = pygame.font.Font("fonts/PixeloidSansBold-PKnYd.ttf", 50)
font_regular = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 30)
font_small = pygame.font.Font("fonts/PixeloidSans-mLxMm.ttf", 20)
font_score = pygame.font.Font("fonts/PixeloidMono-d94EV.ttf", 20)

game_active = False     # Switch between start screen and game
game_started = False    # True after first game started, affects start screen title

# Start screen:
title_surf = font_title.render("Kitten Invaders", False, (156, 156, 156))
title_rect = title_surf.get_rect(midbottom = (screen.get_width()/2, screen.get_height()/3))

game_over_surf = font_title.render("Game over!", False, (156, 156, 156))
game_over_rect = game_over_surf.get_rect(midbottom = (screen.get_width()/2, screen.get_height()/3))

instruct1_surf = font_small.render("Left-arrow & right-arrow to move", False, (156, 156, 156))
instruct1_rect = instruct1_surf.get_rect(midtop = (screen.get_width()/2, screen.get_height()/3*1.4))

instruct2_surf = font_small.render("Space to shoot", False, (156, 156, 156))
instruct2_rect = instruct2_surf.get_rect(midtop = (screen.get_width()/2, screen.get_height()/3*1.6))

info_surf = font_regular.render("Push Enter to play", False, (156, 156, 156))
info_rect = info_surf.get_rect(midtop = (screen.get_width()/2, screen.get_height()/3*2))

# Game score:
game_score = 0

# Starfield surface:
starfield_surf = pygame.Surface((screen.get_width(), screen.get_height()-50))
starfield_surf.fill((0, 0, 25))
generate_starfield(starfield_surf)

# Ground surface:    
ground_surf = pygame.Surface((screen.get_width(), 50))
ground_surf.fill((64, 64, 64))
ground_rect = ground_surf.get_rect(bottomleft = (0, screen.get_height()))

# Player:  
player_surf = pygame.image.load("images/cannon.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (screen.get_width()/2, screen.get_height()-50))

# Cannon bolts:
bolt1_surf = pygame.image.load("images/bolt1.png").convert_alpha()
bolt2_surf = pygame.image.load("images/bolt2.png").convert_alpha()
bolt_surf_list = [bolt1_surf, bolt2_surf]
bolt_rect_list = []

# Enemies:
# kitty1_surf = pygame.image.load("images/kitty1.png").convert_alpha()
kitty2_surf = pygame.image.load("images/kitty2.png").convert_alpha()
kitty3_surf = pygame.image.load("images/kitty3.png").convert_alpha()
kitty4_surf = pygame.image.load("images/kitty4.png").convert_alpha()
enemy_surf_list = [kitty2_surf, kitty3_surf, kitty4_surf]
enemy_rect_list = []

# Game controls:
right = False
left = False

# Timers:
enemy_timer = pygame.USEREVENT + 1
enemy_spawn_rate = 2000
pygame.time.set_timer(enemy_timer, enemy_spawn_rate)
spawn_rate_decreaser = 200

spawn_increase_timer = pygame.USEREVENT + 2
pygame.time.set_timer(spawn_increase_timer, 5000)

# MAIN GAME LOOP:

while True:
    
    for event in pygame.event.get():
        
        # Close game:
        if event.type == pygame.QUIT:
            exit() 
        
        if game_active:
        
        # Game screen events:

            if event.type == pygame.KEYDOWN:
                # Move player:
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                # Shoot bolts:
                if event.key == pygame.K_SPACE:
                    bolt_rect_list.append(choice(bolt_surf_list).get_rect(midbottom = player_rect.midtop))
                    game_score -= 10
                # Quit to start screen:
                if event.key == pygame.K_q:
                    game_active = False
            
            # Stop player movement:    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
            
            # Spawning enemies;        
            if event.type == enemy_timer:
                enemy_rect_list.append(choice(enemy_surf_list).get_rect(midbottom = (randrange(60, screen.get_width()-60), 0)))       
                
            if event.type == spawn_increase_timer:
                if enemy_spawn_rate <= 100:
                    enemy_spawn_rate = (2000 - spawn_rate_decreaser)
                    pygame.time.set_timer(enemy_timer, enemy_spawn_rate)
                    if spawn_rate_decreaser <= 1700:
                        spawn_rate_decreaser += 200
                    print(enemy_spawn_rate)
                    print(spawn_rate_decreaser)    
                else:
                    enemy_spawn_rate -= 100
                    pygame.time.set_timer(enemy_timer, enemy_spawn_rate)

        else:
        
        # Start screen events:
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    game_score = 0
                    enemy_rect_list = []
                    bolt_rect_list = []
                    player_rect.x = screen.get_width()/2 - player_surf.get_width()/2
                    enemy_spawn_rate = 2000
                    spawn_rate_decreaser = 200
                    game_active = True
                    game_started = True
                    print(enemy_spawn_rate)
                    print(spawn_rate_decreaser)   
                    
            # Stop player movement, in case it got stuck when game ended:    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
   
    if game_active:
        
    # Game screen:                    
        if right:
            if player_rect.right <= screen.get_width():
                player_rect.x += 5
        if left:
            if player_rect.left > 0:
                player_rect.x -= 5
        
        # Space background:        
        screen.blit(starfield_surf, (0, 0))
        
        # Enemy movement:
        enemy_rect_list = enemy_movement(enemy_rect_list)
        
        # Bolt movement
        bolt_rect_list = bolt_movement(bolt_rect_list)
        
        # Collisions
        bolt_collision(bolt_rect_list, enemy_rect_list)
        ground_collision(ground_rect, enemy_rect_list)
        
        # Player:    
        screen.blit(player_surf, player_rect)
        
        # Ground:
        screen.blit(ground_surf, ground_rect)    
    
        # Game score:
        display_score(game_score)
    
    else:
    # Start screen
    
        # Space background:        
        screen.blit(starfield_surf, (0, 0))
              
        # Title:
        if game_started:
            screen.blit(game_over_surf, game_over_rect)
        else:    
            screen.blit(title_surf, title_rect)
        
        # Instruction:
        screen.blit(instruct1_surf, instruct1_rect)
        screen.blit(instruct2_surf, instruct2_rect)
        
        # Info    
        screen.blit(info_surf, info_rect)  
    
    pygame.display.update()
    clock.tick(60)