import sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep


def check_key_act(ai_settings, screen, ship, bullets, stats, play_button, aliens):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Moves the ship towards right
                ship.moving_right = True
            
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

            elif event.key == pygame.K_SPACE:
                if len(bullets) < ai_settings.bullets_limit:
                    new_bullet = Bullet(ai_settings, screen, ship)
                    bullets.add(new_bullet)
                
            elif event.key == pygame.K_q:
                sys.exit()
            
            elif event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            
            if event.key == pygame.K_LEFT:
                ship.moving_left = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mouse(play_button, mouse_x, mouse_y, stats, bullets, aliens, ship, ai_settings, screen)




def check_mouse(play_button, mouse_x, mouse_y, stats, bullets, aliens, ship, ai_settings, screen):

    play_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    
    if play_clicked and not stats.game_active:

        ai_settings.init_dynamic_settings()
        
        pygame.mouse.set_visible(False)
        stats.game_active = True
        stats.reset_stats()

        bullets.empty()
        aliens.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()




def check_key_events(ai_settings, screen, ship, bullets, stats, play_button, aliens):
    """Responds to key presses and mouse events"""

    check_key_act(ai_settings, screen, ship, bullets, stats, play_button, aliens)
    # if stats.ships_left <=0 :
    #     sys.exit()


    

def bullet_update(bullets, aliens, ai_settings, screen, ship):
    bullets.update()

    check_bullet_collisions(aliens, bullets, ai_settings, ship, screen)

    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)




def check_bullet_collisions(aliens, bullets, ai_settings, ship, screen):
    colloid = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)



def ship_hit(ai_settings, ship, bullets, aliens, stats, screen):

    if stats.ships_left >0:

        stats.ships_left -= 1

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        
        # Create new fleet and center the ship
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # Pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)





def check_alien_bottom(screen, aliens, ai_settings, ship, bullets, stats):

    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, ship, bullets, aliens, stats, screen)
            break




def update_alien(aliens, ai_settings, ship, bullets, stats, screen):
    check_fleet_edge(aliens, ai_settings)
    aliens.update(ai_settings)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, ship, bullets, aliens, stats, screen)

    check_alien_bottom(screen, aliens, ai_settings, ship, bullets, stats)




def check_fleet_edge(aliens, ai_settings):

    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(aliens, ai_settings)
            break




def change_fleet_direction(aliens, ai_settings):
    
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1




def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats):

    """Update image on screen and flip to the new screen"""

    # Redraw screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()  

    ship.ship_draw()

    

    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()


    # Make the most recently drawn screen visible
    pygame.display.flip()




def get_number_aliens_x(ai_settings, alien_width):

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x




def get_number_aliens_y(ai_settings, alien_height, ship_height):

    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_alien_y = int(available_space_y/(2 * alien_height))
    return number_alien_y




def create_alien(screen, ai_settings, alien_number, aliens, row_number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)




def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(screen, ai_settings)
    number_alien = get_number_aliens_x(ai_settings, alien.rect.width)
    

    # Creating first row of aliens
    for alien_number_y in range(get_number_aliens_y(ai_settings, alien.rect.height, ship.rect.height)):

        for alien_number_x in range(number_alien):

            create_alien(screen, ai_settings, alien_number_x, aliens, alien_number_y)