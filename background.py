import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, image_file, location):
        super(Background, self).__init__()
        self.image = pygame.image.load('/run/media/drunkwhales/90AC4211AC41F1F0/Python/College/Pengenalan Pemrograman/Alien-Invasion-main/Alien-Invasion-main/images/background.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        