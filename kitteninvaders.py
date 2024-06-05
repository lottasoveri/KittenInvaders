import pygame
from random import randrange, choice

def enemy_movement(enemy_list: list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.y += 1
            if enemy_rect.height < 100:
                screen.blit(kitty2_surf, enemy_rect)
            else:
                screen.blit(kitty1_surf, enemy_rect)    
        enemy_list = [enemy for enemy in enemy_list if enemy.y < (screen.get_height() + 100)]    
        return enemy_list
    else:
        return []
    
def firing_bolts(bolt_list: list):
    if bolt_list:
        for bolt_rect in bolt_list:
            bolt_rect.y -= 5
            screen.blit(bolt_surf, bolt_rect)
        bolt_list = [bolt for bolt in bolt_list if bolt.y > -20]    
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
                    bolt_rect.y = -20
                    game_score += 100

def display_score(score):
    score_surf = font.render(f"Score: {score}", False, (0, 0, 25))
    score_rect = score_surf.get_rect(center = (screen.get_width()/2, screen.get_height()-25))
    screen.blit(score_surf, score_rect)
    
pygame.init()

screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption("Kitten Invaders")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# Game score:
game_score = 0

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

# Player:  
player_surf = pygame.image.load("images/cannon.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (screen.get_width()/2, screen.get_height()-50))

# Cannon bolts:
bolt_surf = pygame.image.load("images/piu.png").convert_alpha()

bolt_rect_list = []

# Enemies:
kitty1_surf = pygame.image.load("images/kitty1.png").convert_alpha()
kitty2_surf = pygame.image.load("images/kitty2.png").convert_alpha()

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
                bolt_rect_list.append(bolt_surf.get_rect(midbottom = player_rect.midtop))
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
                
        if event.type == enemy_timer:
            enemy_rect_list.append(choice([kitty1_surf, kitty2_surf]).get_rect(midbottom = (randrange(20, screen.get_width()-20), -10)))       
                
    if right:
        if player_rect.right <= screen.get_width():
            player_rect.x += 5
    if left:
        if player_rect.left > 0:
            player_rect.x -= 5
    
    # Space background:        
    screen.blit(starfield, (0, 0))
    
    # Enemy movement:
    enemy_rect_list = enemy_movement(enemy_rect_list)
    
    # Bolt movement
    bolt_rect_list = firing_bolts(bolt_rect_list)
    
    # Collisions
    bolt_collision(bolt_rect_list, enemy_rect_list)
    
    # Player:    
    screen.blit(player_surf, player_rect)
    
    # Ground:
    screen.blit(ground, (0, screen.get_height()-50))    
 
    # Game score:
    display_score(game_score)
    
    pygame.display.update()
    clock.tick(60)