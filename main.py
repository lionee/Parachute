# Attempt to write a 3d game.
# This will be remake of Skydive originaly made on Nokie 3510i
# by Daniel Czerniawski

import pygame
import numpy as np
from pygame.locals import *
import sys
import engine3d
import os
import osd


class Game:
    def __init__(self):
        self.w = 1280
        self.h = 720
        self.screen = pygame.display.set_mode((self.w, self.h))
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Parachute Game")
        print("Display initialized")
        self.background = pygame.image.load("back.jpg").convert()
        self.surface = pygame.Surface((self.w, self.h))
        self.surface.fill((0, 0, 0))



    def run(self):
        clock = pygame.time.Clock()

        while True:

            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)
            self.surface.fill((255,255,255))


            # Rotate our ground plane
            plane.Rotate(0.0, 0, -0.02)

            # ... and render it
            plane.Render(self.surface, c)

            key = pygame.key.get_pressed()
            c.update(dt, key)

            # render OSD texts, etc
            on_screen_display.update("Altitude: "+ str(int(c.position[2])) + " m.")
            on_screen_display.render(self.surface, (0,0,0))
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    c = engine3d.Camera((20.0, 0.0, 40.0))
    cubeedges = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]])
    cubefaces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5)
    cubecolors = (255,1,2),(4,255,6),(255,255,5),(2,255,255),(255,3,255),(255,255,100)

    cube = engine3d.Mesh("Kostka", 8, cubeedges, cubefaces, cubecolors)

    planeedges = np.array([[0,1], [1,2], [2,3], [3,0]])
    planefaces = (0,1,2),(0,3,2)
    planecolors = (128,255,128),(128,255,128)

    plane = engine3d.Mesh("Ziemia", 4, planeedges, planefaces, planecolors)

    # Since we have no 3d models - we make our models by hand...

    cube.vertices[0] = engine3d.Vector4(-1.0, -1.0, -1.0, 0.0)
    cube.vertices[1] = engine3d.Vector4(1.0, -1.0, -1.0, 0.0)
    cube.vertices[2] = engine3d.Vector4(1.0, 1.0, -1.0, 0.0)
    cube.vertices[3] = engine3d.Vector4(-1.0, 1.0, -1.0, 0.0)
    cube.vertices[4] = engine3d.Vector4(-1.0, -1.0, 1.0, 0.0)
    cube.vertices[5] = engine3d.Vector4(1.0, -1.0, 1.0, 0.0)
    cube.vertices[6] = engine3d.Vector4(1.0, 1.0, 1.0, 0.0)
    cube.vertices[7] = engine3d.Vector4(-1.0, 1.0, 1.0, 0.0)


    plane.vertices[0] = engine3d.Vector4(-1.0, -1.0, 10, 0.0)
    plane.vertices[1] = engine3d.Vector4(-1.0, 1.0, 10, 0.0)
    plane.vertices[2] = engine3d.Vector4(1.0, 1.0, 10, 0.0)
    plane.vertices[3] = engine3d.Vector4(1.0, -1.0, 10, 0.0)
    # Initial scale mesh
    cube.Scale(4., 4., 4.)
    plane.Scale(20., 20., 0.)

    on_screen_display = osd.osd()
    g = Game()
    g.run()