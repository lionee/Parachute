# Attempt to write a 3d game.
# This will be remake of Skydive originaly made on Nokia 3510i
# by Daniel Czerniawski

import pygame
import numpy as np
from pygame.locals import *
import sys
import engine3d
import os
import osd
import copy


class Game:
    def __init__(self):
        self.w = 1280
        self.h = 720
        self.screen = pygame.display.set_mode((self.w, self.h))
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Parachute Game")
        print("Display initialized")
        self.surface = pygame.Surface((self.w, self.h))
        self.surface.fill((153, 204, 255))

        self.player = pygame.image.load("skydiver.png").convert_alpha()

    def run(self):
        clock = pygame.time.Clock()
        alt = 400 # Initial altitude
        Landed = 0 # Have we landed?

        while (Landed < 1):
            alt-=.59 # Falling speed

            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)

            self.surface.fill((153, 204, 255))

            # we are falling
            c.position[2]=alt
            # Rotate our Meshes
            # todo: prepare common function

            plane.Rotate(0.0, 0, 0)
            road.Rotate(0.0, 0, 0)
            road2.Rotate(0.0, 0, 0)

            # Render Meshes
            # todo: prepare commmon function

            plane.Render(self.surface, c)
            road.Render(self.surface, c)
            road2.Render(self.surface, c)

            # Keyboard handling
            key = pygame.key.get_pressed()
            c.update(dt, key)

            # Draw shadow on certain altitude
            if (c.position[2]<60):
                pygame.draw.circle(self.surface, (100, 100, 100), (int(self.w/2), 525-int(50/c.position[2])*5-34), int(120 / c.position[2]))

            # Draw player sprite
            self.surface.blit(self.player, (self.w/2-self.player.get_width()/2, self.h/2-self.player.get_height()/2))

            # render OSD texts, etc
            if (alt>2):
                on_screen_display.update("Altitude: "+ str(int(c.position[2])) + " m.")


            else:
                on_screen_display.update("YOU ARE DEAD BABY!")
            on_screen_display.render(self.surface, (0, 0, 0))

            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()

            if (alt<2): Landed=1

        pygame.time.wait(10000)

if __name__ == "__main__":

    pygame.init()
    c = engine3d.Camera((0.0, 0.0, 400.0), 0.4)

    # Since we have no 3d models - we make our models by hand...
    planeedges = np.array([[0,1], [1,2], [2,3], [3,0]])
    planefaces = (0,1,2),(0,3,2)
    planecolors = (51, 204, 51),(51, 204, 51)

    plane = engine3d.Mesh("Ziemia", 4, planeedges, planefaces, planecolors)

    plane.vertices[0] = engine3d.Vector4(-3.0, -3.3, 10, 0.0)
    plane.vertices[1] = engine3d.Vector4(-4.2, 2.6, 10, 0.0)
    plane.vertices[2] = engine3d.Vector4(2.1, 5.0, 10, 0.0)
    plane.vertices[3] = engine3d.Vector4(2.1, -3.3, 10, 0.0)

    roadedges=np.array([[0,1], [1,2], [2,3], [3,0]])
    roadfaces = (0, 1, 2), (0, 3, 2)
    roadcolors = (200, 200, 200), (200, 200, 200)

    road = engine3d.Mesh("Droga", 4, roadedges, roadfaces, roadcolors)

    road.vertices[0] = engine3d.Vector4(-1, -1, 11, 0.0)
    road.vertices[1] = engine3d.Vector4(-1, 1, 11, 0.0)
    road.vertices[2] = engine3d.Vector4(1, 1, 11, 0.0)
    road.vertices[3] = engine3d.Vector4(1, -1, 11, 0.0)

    road2 = copy.deepcopy(road)
    # Initial scale mesh

    plane.Scale(60., 50., 0.)
    road.Scale(30,4,0)
    road2.Scale(55,4,0)

    road2.Rotate(0,0,.8)
    on_screen_display = osd.osd()
    g = Game()
    g.run()

    print("Game Over")