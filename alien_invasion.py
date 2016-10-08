<<<<<<< HEAD
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
#from alien import Alien
import game_functions as gf

def run_game():
    #initialize game, settings and create a screen object
=======
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
>>>>>>> 6c31f6438409964a7ee5767c50064402572b5b84
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
<<<<<<< HEAD

    #make a ship
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()

    #set background
    bg_color = (230, 230, 230)

    #Make a group of aliens
    aliens = Group()

    #create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #start the main loop
    while True:
        #watch for keyboard and mouse event
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)

        #print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
=======
    bg_color = (230, 230, 230)

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
>>>>>>> 6c31f6438409964a7ee5767c50064402572b5b84

run_game()
