import pygame
import numpy as np
from pygame.locals import *
import sys
import engine3d


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.background = pygame.image.load("back.jpg").convert()
        self.surface = pygame.Surface((640, 480))
        self.surface.fill((255, 255, 255))

        c = engine3d.Camera([0.0, 0.0, 10.0], [0.0, 0.0, 0.0])
        cube = engine3d.Mesh("Kostka", 8)
        cube.vertices[0] = engine3d.Vector4(-0.0, 0.0, 0.0, 0.0)
        cube.vertices[1] = engine3d.Vector4(1.0, 1.0, 1.0, 1.0)
        cube.vertices[2] = engine3d.Vector4(-1.0, -1.0, 1.0, 0.0)
        cube.vertices[3] = engine3d.Vector4(-1.0, -1.0, -1.0, 0.0)
        cube.vertices[4] = engine3d.Vector4(-1.0, 1.0, -1.0, 0.0)
        cube.vertices[5] = engine3d.Vector4(1.0, 1.0, -1.0, 0.0)
        cube.vertices[6] = engine3d.Vector4(1.0, -1.0, 1.0, 0.0)
        cube.vertices[7] = engine3d.Vector4(1.0, -1.0, -1.0, 0.0)

        # translate into world space
        cube.Translate(2.0, 2.0, 2.0)

        # scale mesh
        cube.Scale(4.0, 3.0, 5.0)

        # There should be projection
        cube.Transform()
        cube.Project(cube.vertices[1].get_nparray(), cube.GetProjectionMatrix())

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # self.surface.blit(self.background, (0, 0))
            pygame.draw.line(self.surface, (0, 255, 0), [0, 0], [400, 30], 1)
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()


if __name__ == "__main__":


    g = Game()
    g.run()