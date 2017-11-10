import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('skydiver1.png'))
        self.images.append(load_image('skydiver2.png'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 104, 108)

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]