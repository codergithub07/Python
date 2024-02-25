import pygame.font

class Scoreboard():
    def __init__(self, stats, ai_settings, screen) -> None:
        
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)

        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()