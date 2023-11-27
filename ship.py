import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('rocket.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx # can also do it in screen_rect(centerx = (x,y))
        self.rect.bottom = self.screen_rect.bottom # just saying this makes it faster

        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        #movements flags.
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """Update the ship's position, based on movement flags."""
        # if key is press movement is True
        # if self.moving_right:
        #     self.rect.centerx += 1
        # if self.moving_left:
        #     self.rect.centerx -= 1
        # instead of using this number we can just refer to ai_setting so its easier
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
