import pygame
from random import randrange, choice

def enemy_movement(enemy_list: list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.y += 1
            screen.blit(kitty1_surf, enemy_rect)
        return enemy_list
    else:
        return []

pygame.init()

screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption("Kitten Invaders")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# Starfield generator:
star_coords = []
star_counter = 0
while star_counter < 200:
    star = {}
    star["star_x"] = randrange(1, screen.get_width())
    star["star_y"] = randrange(1, screen.get_height()-50)
    star["star_size"] = choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3])
    star_coords.append(star)
    star_counter += 1
    
# Game surfaces:
starfield = pygame.Surface((screen.get_width(), screen.get_height()-50))
starfield.fill((0, 0, 25))
for star in star_coords:
    pygame.draw.circle(starfield, (204, 229, 255), (star["star_x"], star["star_y"]), star["star_size"])
    
ground = pygame.Surface((screen.get_width(), 50))
ground.fill((64, 64, 64))

score_surf = font.render(" 0 ", False, (0, 0, 25))
score_rect = score_surf.get_rect(center = (screen.get_width()/2, screen.get_height()-25))

# Player:  
player_surf = pygame.image.load("images/cannon.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (screen.get_width()/2, screen.get_height()-50))

bolt_surf = pygame.image.load("images/piu.png").convert_alpha()
bolt_rect = bolt_surf.get_rect(center = (screen.get_width(), screen.get_height()))

# Enemies:
kitty1_surf = pygame.image.load("images/kitty1.png").convert_alpha()
kitty_x = randrange(20, screen.get_width()-20)
kitty1_rect = kitty1_surf.get_rect(midbottom = (kitty_x, -10))

enemy_rect_list = []

# Game control initiation:
right = False
left = False

# Timer:
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 2000)

# MAIN GAME LOOP:

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_SPACE:
                pass
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
                
        if event.type == enemy_timer:
            enemy_rect_list.append(kitty1_surf.get_rect(midbottom = (randrange(20, screen.get_width()-20), -10)))
                
    if right:
        if player_rect.right <= screen.get_width():
            player_rect.x += 5
    if left:
        if player_rect.left > 0:
            player_rect.x -= 5
            
    # kitty1_rect.y += 1
    # if kitty1_rect.top >= screen.get_height():
    #     kitty_x = randrange(20, screen.get_width()-20)
    #     kitty1_rect.midbottom = (kitty_x, -10)
            
    screen.blit(starfield, (0, 0))
    screen.blit(bolt_surf, bolt_rect)
    # screen.blit(kitty1_surf, kitty1_rect)
    
    # Enemy movement:
    enemy_rect_list = enemy_movement(enemy_rect_list)
    
    screen.blit(ground, (0, screen.get_height()-50))    
    pygame.draw.rect(screen, (150, 150, 150), score_rect) 
    screen.blit(score_surf, score_rect)
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)