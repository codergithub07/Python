import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from game_stats import Game_stats

from button import Button

def run_game():

    # Initializes game and creates a screen object
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))   # 1200 pixels wide and 800 pixels hight

    # Make a group to store bullets in
    bullets = Group()
    ship = Ship(screen, ai_settings)
    aliens = Group()

    pygame.display.set_caption("Aline Invasion")

    # Create fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens, ship)

    stats = Game_stats(ai_settings)

    play_button = Button(screen, "Play")

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        gf.check_key_events(ai_settings, screen, ship, bullets, stats, play_button, aliens)

        if stats.game_active:
            ship.update()
            gf.bullet_update(bullets, aliens, ai_settings, screen, ship)
            gf.update_alien(aliens, ai_settings, ship, bullets, stats, screen)
        
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats)

run_game()