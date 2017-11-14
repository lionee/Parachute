# Attempt to write a 3d game.
# This will be remake of Skydive originaly made on Nokia 3510i
# by Daniel Czerniawski

import pygame
import numpy as np
import sys
import engine3d
import os
import osd
import copy
import player
import random



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

    def GenerateCircles(self, meshes_list, radius, amount):
        print("Generating Circles...")

        for i in range(amount):
            # Max horizontal distance is 50
            randx = random.randint(-25, 25)
            randy = random.randint(-25, 25)

            circleedges = np.array([[0, 1], [1, 2], [2, 3], [3, 0]])
            circlefaces = (0, 1, 2), (0, 3, 2)
            circlecolors = (51, 204, 51), (51, 204, 51)

            cir = engine3d.Mesh(str(i), 4, circleedges, circlefaces, circlecolors, 1)

            cir.vertices[0] = engine3d.Vector4(-1, -1, 1, 1)
            cir.vertices[1] = engine3d.Vector4(-1, 1, 1, 1)
            cir.vertices[2] = engine3d.Vector4(1, 1, 1, 1)
            cir.vertices[3] = engine3d.Vector4(1, -1, 1, 1)

            cir2 = copy.deepcopy(cir)

            cir.Scale(radius, radius, 1.)
            cir2.Scale(radius, radius, 1.)
            cir2.Rotate(0, 0, .785)
            cir.Translate(randx, randy, (i + 1) * 100)  # adding 1 to i, to make sure we are not starting generation from 0 meters
            cir2.Translate(randx, randy, (i + 1) * 100)

            meshes_list.append(cir)
            meshes_list.append(cir2)

    def run(self):
        clock = pygame.time.Clock()
        alt = 800  # Initial altitude
        Landed = 0  # Have we landed?

        while (Landed < 1):
            alt -= .19  # Falling speed

            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)

            self.surface.fill((153, 204, 255))

            # we are falling
            c.position[2] = alt

            # Render Meshes
            engine3d.RenderAllMeshes(all_meshes, alt, self.surface, c)

            # Keyboard handling
            key = pygame.key.get_pressed()
            c.update(dt, key)

            # Draw shadow on certain altitude
            if (c.position[2] < 60):
                pygame.draw.circle(self.surface, (100, 100, 100),
                                   (int(self.w / 2), 525 - int(50 / c.position[2]) * 5 - 34), int(120 / c.position[2]))

            # Draw player sprite
            sprite_group.update(dt, key)
            sprite_group.draw(self.surface)

            # render OSD texts, etc
            if (alt > 100):
                on_screen_display.update("Altitude: " + str(int(c.position[2])) + " m. " + str(player.vrot))
            elif (alt < 100 and alt > 2):
                on_screen_display.update("Altitude: " + str(int(c.position[2])) + " m. OPEN PARACHUTE!!!")

            elif (alt < 2):
                on_screen_display.update("YOU ARE DEAD BABY!")
            on_screen_display.render(self.surface, (0, 0, 0))

            # Finally put all to screen
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()

            if (alt < 2): Landed = 1



def getz(mesh):
    return mesh.Getz()


if __name__ == "__main__":
    pygame.init()

    # Scene mesh list
    all_meshes = list()

    # Camera initialization
    c = engine3d.Camera((0.0, 0.0, 400.0), 0.4)

    cubeedges = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]])
    cubefaces = (0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)
    cubecolors = (100, 100, 100), (110, 110, 110), (120, 120, 120), (130, 130, 130), (140, 140, 140), (150, 150, 150)

    cube = engine3d.Mesh("Kostka", 8, cubeedges, cubefaces, cubecolors, 2)

    cube.vertices[0] = engine3d.Vector4(-1.0, -1.0, 0, 1)
    cube.vertices[1] = engine3d.Vector4(1.0, -1.0, 0, 1)
    cube.vertices[2] = engine3d.Vector4(1.0, 1.0, 0, 1)
    cube.vertices[3] = engine3d.Vector4(-1.0, 1.0, 0, 1)
    cube.vertices[4] = engine3d.Vector4(-1.0, -1.0, 10.0, 1)
    cube.vertices[5] = engine3d.Vector4(1.0, -1.0, 10.0, 1)
    cube.vertices[6] = engine3d.Vector4(1.0, 1.0, 10.0, 1)
    cube.vertices[7] = engine3d.Vector4(-1.0, 1.0, 10.0, 1)



    # Since we have no 3d models - we make our models by hand...
    planeedges = np.array([[0, 1], [1, 2], [2, 3], [3, 0]])
    planefaces = (0, 1, 2), (0, 3, 2)
    planecolors = (51, 204, 51), (51, 204, 51)

    plane = engine3d.Mesh("Ziemia", 4, planeedges, planefaces, planecolors, 2)

    plane.vertices[0] = engine3d.Vector4(-3.0, -3.3, 0, 0.0)
    plane.vertices[1] = engine3d.Vector4(-4.2, 2.6, 0, 0.0)
    plane.vertices[2] = engine3d.Vector4(2.1, 5.0, 0, 0.0)
    plane.vertices[3] = engine3d.Vector4(2.1, -3.3, 0, 0.0)

    roadedges = np.array([[0, 1], [1, 2], [2, 3], [3, 0]])
    roadfaces = (0, 1, 2), (0, 3, 2)
    roadcolors = (200, 200, 200), (200, 200, 200)

    road = engine3d.Mesh("Droga", 4, roadedges, roadfaces, roadcolors, 2)

    road.vertices[0] = engine3d.Vector4(-1, -1, 0, 0.0)
    road.vertices[1] = engine3d.Vector4(-1, 1, 0, 0.0)
    road.vertices[2] = engine3d.Vector4(1, 1, 0, 0.0)
    road.vertices[3] = engine3d.Vector4(1, -1, 0, 0.0)

    road2 = copy.deepcopy(road)

    # Initial scale mesh

    plane.Scale(60., 50., 1.)
    road.Scale(30, 4, 1)
    road2.Scale(55, 4, 1)

    # And Rotation
    road2.Rotate(0, 0, .8)

    cube.Scale(3,2,1)
    cube.Rotate(0,0, 0.2)
    cube.Translate(20,10,1)
    # On screen text
    on_screen_display = osd.Osd()

    # We are adding to out mesh list

    all_meshes.append(plane)
    all_meshes.append(road)
    all_meshes.append(road2)
    all_meshes.append(cube)

    g = Game()

    # Let's generate some circles to fall through
    g.GenerateCircles(all_meshes, 1, 5)

    # Sort meshes by average Z-index
    all_meshes = sorted(all_meshes, key=getz)
    print(all_meshes)

    player = player.Player(g.w / 2 - 108 / 2, g.h / 2 - 104 / 2)
    sprite_group = pygame.sprite.Group(player)
    g.run()

    print("Game Over")
