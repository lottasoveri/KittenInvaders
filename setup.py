from pygame.draw import circle
from random import randrange, choice

def generate_starfield(surface, width, height):
    star_coords = []
    star_counter = 0
    while star_counter < 200:
        star = {}
        star["star_x"] = randrange(1, width - 1)
        star["star_y"] = randrange(1, height - 1)
        star["star_size"] = choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3])
        star_coords.append(star)
        star_counter += 1
        for star in star_coords:
            circle(surface, 
                   (204, 229, 255), 
                   (star["star_x"], star["star_y"]), 
                   star["star_size"]
                   )
