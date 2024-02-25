import pygame

pygame.init()

width, height = pygame.display.set_mode().get_size()


class Settings():
    def __init__(self) -> None:
        self.screen_width = width
        self.screen_height = height
        self.bg_color = (230, 230, 230)
        self.bullet_width = 1200 #5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_limit = 100

        # Game speedup scale factor
        self.speedup_factor = 1.2

        self.init_dynamic_settings()

        # Alien settings
        self.fleet_drop_speed = 50

        # Ship settings
        self.ships_limit = 1

    def init_dynamic_settings(self):

        self.speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor_x = 1
        self.fleet_direction = 1

    def increase_speed(self):

        self.speed_factor *= self.speedup_factor
        self.bullet_speed_factor *= self.speedup_factor
        self.alien_speed_factor_x *= self.speedup_factor