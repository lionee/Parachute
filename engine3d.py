import numpy as np
import pygame
from pygame import gfxdraw
import math


#
# Vertex4
#
class Vector4:
    def __init__(self, x, y, z, w):
        self.vector = np.array([x, y, z, w])

    def retx(self):
        return self.vector[0]

    def rety(self):
        return self.vector[1]

    def retz(self):
        return self.vector[2]

    def print_vertex4(self):
        print(self.vector)

    def get_nparray(self):
        return self.vector
#
#   Class is defining camera object
#
class Camera:
    def __init__(self, position, target):

        # Camera position in space
        self.position = np.array(position)

        # Where is camera looking?
        self.target = np.array(target)


#
#   Class is defining shape (mesh). Takes name and vertices count as input.
#
class Mesh:
    def __init__(self, name, verts_count):
        self.name = name
        self.vertices = [np.array([0., 0., 0., 0.])] * verts_count
        self.position = np.array([0., 0., 0.])
        self.rotation = np.array([0., 0., 0.])
        self.mvp = Vector4(0. ,0. ,0. ,0.)
        self.points2d = np.array([0, 0]) * verts_count

    def Scale(self, x, y, z):
        s_matrix = self.ScaleMatrix = np.array([[x, 0., 0., 0.],
                      [0., y, 0., 0.],
                      [0., 0., z, 0.],
                      [0., 0., 0., 1.]])

        for vert in self.vertices:
            vert.vector = vert.vector.dot(s_matrix)

        return s_matrix;

    def Rotate(self, radiansx, radiansy):

        rsinx = math.sin(radiansx)
        rcosx = math.cos(radiansx)

        rsiny= math.sin(radiansy)
        rcosy= math.cos(radiansy)

        # Rotation Matrix around X axis
        rx_matrix = self.RotationXMatrix = np.array([[rcosx, 0., rsinx, 0.],
                                                [0., 1, 0., 0.],
                                                [-rsinx, 0., rcosx, 0.],
                                                [0., 0., 0., 1.]])
        # Rotation Matrix around Y axis
        ry_matrix = self.RotationYMatrix = np.array([[1, 0., 0, 0.],
                                                [0., rcosy, -rsiny, 0.],
                                                [0, rsiny, rcosy, 0.],
                                                [0., 0., 0., 1.]])
        for vert in self.vertices:
            vert.vector = vert.vector.dot(rx_matrix.dot(ry_matrix))

        return rx_matrix;


    def Translate(self, x, y, z):
        t_matrix = self.TranslateMatrix = np.array([[1., 0., 0., x],
                      [0., 1., 0., y],
                      [0., 0., 1., z],
                      [0., 0., 0., 1.]])

        for vert in self.vertices:
            vert.vector = vert.vector.dot(t_matrix)

        return t_matrix;


    def Render(self, surface):
        surface.fill((255, 255, 255))
        v = Vector4(0. ,0. ,0. ,0.)
        for vert in self.vertices:

            v = vert.vector[2]
            vert.vector[2] += 15

            x = vert.retx()*(300/vert.retz())
            y = vert.rety()*(300/vert.retz())
            print((int(x) + int(surface.get_width()/2), int(y) + int(surface.get_height()/2)))

            # TODO - Clipping!

            #if (x>=0 and y>=0 and x<surface.get_width() and y<surface.get_height()):
            pygame.draw.circle(surface, (0,0,0), (int(x) + int(surface.get_width()/2), int(y) + int(surface.get_height()/2)), 4)
            vert.vector[2] = v


    def GetProjectionMatrix(self):
        return self.mvp;



