import pygame


def load_image(name):
    image = pygame.image.load(name)
    return image

class Player(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony):
        super(Player, self).__init__()
        self.images = []
        self.images.append(load_image('assets/skydiver.png'))
        self.images.append(load_image('assets/skydiver2.png'))
        self.animation_time = 50
        self.current_time = 0
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(positionx, positiony, 104, 108)

    def update(self, dt):

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index += 1
            if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

