import pygame

from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, screen, ai_settings):

        super().__init__()

        self.screen = screen

        self.ai_settings = ai_settings

        # Load the image and set it's rect
        self.image = pygame.image.load('Images\\alien_ship.png')
        self.rect = self.image.get_rect()

        # Initializing position of alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        
        elif self.rect.left < 0:
            return True

    def update(self, ai_settings):
        self.x += (ai_settings.alien_speed_factor_x * ai_settings.fleet_direction)
        self.rect.x = self.x