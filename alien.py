import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__ (self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load The Alien Image and set its rect attribute
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien neat the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horiontal postition.
        self.x = float(self.rect.x)

    def update(self):
        """Move the Alien to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x