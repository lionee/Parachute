import pygame
import math


def load_image(name):
    image = pygame.image.load(name)
    return image

# TODO: Prepare sprite for different parachuter's lean

class Player(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony):
        super(Player, self).__init__()
        self.images = []
        self.images2 = []
        self.images3 = []
        self.images4 = []
        self.images5 = []
        self.images.append(load_image('assets/skydiver.png'))
        self.images.append(load_image('assets/skydiver2.png'))
        self.images2.append(load_image('assets/skydiver3.png'))
        self.images2.append(load_image('assets/skydiver4.png'))
        self.images3.append(load_image('assets/skydiver5.png'))
        self.images3.append(load_image('assets/skydiver6.png'))
        self.images4.append(load_image('assets/skydiver7.png'))
        self.images4.append(load_image('assets/skydiver8.png'))
        self.images5.append(load_image('assets/skydiver9.png'))
        self.images5.append(load_image('assets/skydiver10.png'))

        self.animation_time = 50
        self.current_time = 0
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(positionx, positiony, 104, 108)
        self.points = 0
        self.fallspeed = 0.17
        self.vrot=0

    def update(self, dt, key):

        self.current_time += dt
        if (key[pygame.K_w] and self.vrot<=90):
            self.vrot += 2

        if (key[pygame.K_s] and self.vrot>=-90):
            self.vrot -= 2


        if (self.fallspeed > 0.30): self.fallspeed = 0.30
        if (self.fallspeed < 0.15): self.fallspeed = 0.15

        if (self.fallspeed <= 0.30 and self.fallspeed >= 0.15):
            self.fallspeed=0.17 + abs(self.vrot/700)

        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index += 1

            if self.index >= len(self.images):
                    self.index = 0


            if (self.vrot/1000 > 0.07):
                self.image = self.images[self.index]


            elif (self.vrot/1000 > 0.02 and self.vrot/1000 <= 0.07):
                self.image = self.images2[self.index]

            elif (self.vrot/1000 <= 0.02 and self.vrot/1000 >= -0.02):
                self.image = self.images3[self.index]

            elif (self.vrot/1000 < -0.02 and self.vrot/1000 >= -0.07):
                self.image = self.images4[self.index]

            elif (self.vrot/1000 < -0.07):
                self.image = self.images5[self.index]

            else:
                pass
            print(100/self.fallspeed)
