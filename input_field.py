import pygame

pygame.font.init()

color_inactive = pygame.Color((128, 128, 128))
color_active = pygame.Color((0, 255, 255))
font = pygame.font.Font(None, 30)

class InputField:
    def __init__(self, width, height, screen_width, screen_height, text = ""):
        self.pos_x = screen_width/2 - width/2
        self.pos_y = screen_height/2
        self.rect = pygame.Rect(self.pos_x, self.pos_y, width, height)
        self.color = color_inactive
        self.text = text
        self.text_surface = font.render(text, True, (204, 204, 204))
        self.active = False

    # User input:    
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If player clicks in input field:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = color_active if self.active else color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    if len(self.text) > 0:
                        self.text = self.text[:-1]
                elif len(self.text) < 20:
                        self.text += event.unicode
                self.text_surface = font.render(self.text, True, (204, 204, 204))
                
    def clear(self):
        self.text = self.text.strip()
        self.text_surface = font.render(self.text, True, (204, 204, 204))

    def draw(self, screen):
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
