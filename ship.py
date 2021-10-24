import pygame

class Ship:
    """A Class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting point"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottome center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships postion based on the movement flag."""
        #Update the ships x value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #Update rect object
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
