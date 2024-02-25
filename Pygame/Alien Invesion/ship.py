import pygame

class Ship():
    def __init__(self, screen, ai_settings) -> None:
        """Initiates the ship and set it's starting position"""
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings

        # Load the ship image and get it's rect
        self.image = pygame.image.load('Images\\ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start new ship at bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor
        
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.speed_factor
        
        self.rect.centerx = int(self.center)

    def ship_draw(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx