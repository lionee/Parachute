import pygame
import numpy as np
from pygame.locals import *
import sys
import engine3d

class Render:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.background = pygame.image.load("back.jpg").convert()
        self.surface = pygame.Surface((640,480))
        self.surface.fill((255,255,255))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            #self.surface.blit(self.background, (0,0))
            pygame.draw.line(self.surface, (0,255,0), [0, 0], [400,30], 1)
            self.screen.blit(self.surface,(0,0))
            pygame.display.update()


if __name__=="__main__":
    c = engine3d.camera([0.0, 0.0, 10.0], [0.0, 0.0, 0.0])
    cube = engine3d.mesh("Kostka", 8)
    cube.vertices[0] = np.array([-1.0, 1.0, 1.0])
    cube.vertices[1] = np.array([1.0, 1.0, 1.0])
    cube.vertices[2] = np.array([-1.0, -1.0, 1.0])
    cube.vertices[3] = np.array([-1.0, -1.0, -1.0])
    cube.vertices[4] = np.array([-1.0, 1.0, -1.0])
    cube.vertices[5] = np.array([1.0, 1.0, -1.0])
    cube.vertices[6] = np.array([1.0, -1.0, 1.0])
    cube.vertices[7] = np.array([1.0, -1.0, -1.0])
    print(cube.vertices[:8])

    r = Render()
    r.run()