# Attempt to write a 3d game.
# by Daniel Czerniawski

import pygame
import numpy as np
from pygame.locals import *
import sys
import engine3d


class Game:
    def __init__(self):
        self.w = 1280
        self.h = 720
        self.screen = pygame.display.set_mode((self.w, self.h))
        print("Display initialized")
        self.background = pygame.image.load("back.jpg").convert()
        self.surface = pygame.Surface((self.w, self.h))
        self.surface.fill((255, 255, 255))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # We rotate our cube mesh...
            cube.Rotate(0.01, 0.02)
            plane.Rotate(0.01,0)
            # ... and render it
            cube.Render(self.surface)
            #plane.Render(self.surface)
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()


if __name__ == "__main__":

    #c = engine3d.Camera([0.0, 0.0, 10.0], [0.0, 0.0, 0.0])
    cubeedges = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]])
    cube = engine3d.Mesh("Kostka", 8, cubeedges)

    planeedges = np.array([[0,1], [1,2], [2,3], [3,0]])
    plane = engine3d.Mesh("Ziemia", 4, planeedges)
    # Since we have no 3d model - we make our cube by hand...

    cube.vertices[0] = engine3d.Vector4(-1.0, -1.0, -1.0, 0.0)
    cube.vertices[1] = engine3d.Vector4(1.0, -1.0, -1.0, 0.0)
    cube.vertices[2] = engine3d.Vector4(1.0, 1.0, -1.0, 0.0)
    cube.vertices[3] = engine3d.Vector4(-1.0, 1.0, -1.0, 0.0)
    cube.vertices[4] = engine3d.Vector4(-1.0, -1.0, 1.0, 0.0)
    cube.vertices[5] = engine3d.Vector4(1.0, -1.0, 1.0, 0.0)
    cube.vertices[6] = engine3d.Vector4(1.0, 1.0, 1.0, 0.0)
    cube.vertices[7] = engine3d.Vector4(-1.0, 1.0, 1.0, 0.0)


    plane.vertices[0] = engine3d.Vector4(-1.0, -1.0, 1, 0.0)
    plane.vertices[1] = engine3d.Vector4(-1.0, 1.0, 1, 0.0)
    plane.vertices[2] = engine3d.Vector4(1.0, -1.0, 1, 0.0)
    plane.vertices[3] = engine3d.Vector4(1.0, 1.0, 1, 0.0)
    # Initial scale mesh
    cube.Scale(4., 4., 4.)
    plane.Scale(4., 4., 4.)

    g = Game()
    g.run()