import pygame
from random import randrange, choice

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
starfield.fill((0,0,25))
for star in star_coords:
    pygame.draw.circle(starfield, (204, 229, 255), (star["star_x"], star["star_y"]), star["star_size"])
    
ground = pygame.Surface((screen.get_width(), 50))
ground.fill((64, 64, 64))

score_counter = font.render("counter", False, (255, 255, 255))

# Game characters:  
player_surf = pygame.image.load("images/cannon.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (screen.get_width()/2, screen.get_height()-50))

kitty1_surf = pygame.image.load("images/kitty1.png").convert_alpha()
kitty_x = randrange(10, screen.get_width()-10)
kitty1_rect = kitty1_surf.get_rect(midbottom = (kitty_x, -10))

bolt_surf = pygame.image.load("images/piu.png").convert_alpha()
bolt_rect = bolt_surf.get_rect()

# Game control initiation:
right = False
left = False

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
                
    if right:
        if player_rect.right <= screen.get_width():
            player_rect.x += 5
    if left:
        if player_rect.left > 0:
            player_rect.x -= 5
            
    kitty1_rect.y += 1
    if kitty1_rect.top >= screen.get_height():
        kitty_x = randrange(10, screen.get_width()-10)
        kitty1_rect.midbottom = (kitty_x, -10)
            
    screen.blit(starfield, (0, 0))
    screen.blit(kitty1_surf, kitty1_rect)
    screen.blit(ground, (0, screen.get_height()-50))            
    screen.blit(score_counter, (10, screen.get_height()-35))
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)