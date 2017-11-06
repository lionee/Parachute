import pygame
import numpy as np
from pygame.locals import *
import sys
import engine3d


class Game:
    def __init__(self):
        self.w = 640
        self.h = 480
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.background = pygame.image.load("back.jpg").convert()
        self.surface = pygame.Surface((640, 480))
        self.surface.fill((255, 255, 255))







    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)


            cube.Rotate(0.01, 0.02)
            cube.Render(self.surface)
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()


if __name__ == "__main__":

    #c = engine3d.Camera([0.0, 0.0, 10.0], [0.0, 0.0, 0.0])
    cube = engine3d.Mesh("Kostka", 8)
    cube.vertices[0] = engine3d.Vector4(-1.0, 1.0, 1.0, 0.0)
    cube.vertices[1] = engine3d.Vector4(1.0, 1.0, 1.0, 1.0)
    cube.vertices[2] = engine3d.Vector4(-1.0, -1.0, 1.0, 0.0)
    cube.vertices[3] = engine3d.Vector4(-1.0, -1.0, -1.0, 0.0)
    cube.vertices[4] = engine3d.Vector4(-1.0, 1.0, -1.0, 0.0)
    cube.vertices[5] = engine3d.Vector4(1.0, 1.0, -1.0, 0.0)
    cube.vertices[6] = engine3d.Vector4(1.0, -1.0, 1.0, 0.0)
    cube.vertices[7] = engine3d.Vector4(1.0, -1.0, -1.0, 0.0)

    # Initial scale mesh
    cube.Scale(4.5, 4.5, 4.5)

    g = Game()
    g.run()