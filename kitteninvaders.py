import pygame
from random import randrange, choice

pygame.init()

screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption("Kitten Invaders")
clock = pygame.time.Clock()

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
starfield_surf = pygame.Surface((screen.get_width(), screen.get_height()-50))
starfield_surf.fill((0,0,25))
for star in star_coords:
    pygame.draw.circle(starfield_surf, (204, 229, 255), (star["star_x"], star["star_y"]), star["star_size"])
    
ground_surf = pygame.Surface((screen.get_width(), 50))
ground_surf.fill((64, 64, 64))

# Game characters:  
player = pygame.image.load("images/cannon.png")
kitty1 = pygame.image.load("images/kitty1.png")
bolt = pygame.image.load("images/piu.png")

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
                
    # if right:
    #     if player.x < 1280 - player.get_width():
    #         player.x += 3
    # if left:
    #     if player.x > 0:
    #         player.x -= 3
    
    screen.blit(starfield_surf, (0, 0))
    screen.blit(ground_surf, (0, screen.get_height()-50))            
    screen.blit(player, (screen.get_width()/2 - player.get_width()/2, screen.get_height() - player.get_height() - 50))
    
    pygame.display.flip()
    
    clock.tick(60)