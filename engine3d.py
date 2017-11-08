# Engine is capable of rendering not only flat objects used in this game.
# It can render any 3d object.
#
# TODO: z-buffering, loading objects from Blender exports.
#

import numpy as np
import pygame
from pygame import gfxdraw
import math


#
# Vector4 class
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

    def retw(self):
        return self.vector[3]

    def print_vertex4(self):
        print(self.vector)

    def get_nparray(self):
        return self.vector
#
#   Class is defining camera object
#
class Camera:
    def __init__(self, position):

        # Camera position in space
        self.position = list(position)

        # Where is camera looking?
        #self.target = target

    def update(self, dt, key):
        s = dt/1000 * 10

        if key[pygame.K_w]: self.position[1]+=s
        if key[pygame.K_s]: self.position[1]-=s

        if key[pygame.K_a]: self.position[0]-=s
        if key[pygame.K_d]: self.position[0]+=s

        if key[pygame.K_z]: self.position[2] -= s
        if key[pygame.K_x]: self.position[2] += s


#
#   Class is defining shape (mesh). Takes name and vertices count as input.
#
class Mesh:
    def __init__(self, name, verts_count, edges, faces, colors):
        self.name = name
        self.vertices = [np.array([0., 0., 0., 0.])] * verts_count
        self.edges = edges
        self.faces = faces
        self.colors = colors
        print("Mesh created:", self.name)

    def Scale(self, x, y, z):
        s_matrix = self.ScaleMatrix = np.array([[x, 0., 0., 0.],
                      [0., y, 0., 0.],
                      [0., 0., z, 0.],
                      [0., 0., 0., 1.]])

        for vert in self.vertices:
            vert.vector = vert.vector.dot(s_matrix)

        return s_matrix;

    def Rotate(self, radiansx, radiansy, radiansz):

        rsinx = math.sin(radiansx)
        rcosx = math.cos(radiansx)

        rsiny= math.sin(radiansy)
        rcosy= math.cos(radiansy)

        rsinz = math.sin(radiansz)
        rcosz = math.cos(radiansz)

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
        # Rotation Matrix around Z axis
        rz_matrix = self.RotationZMatrix = np.array([[rcosz, -rsinz, 0, 0.],
                                                     [rsinz, rcosz, 0, 0.],
                                                     [0, 0, 1, 0.],
                                                     [0., 0., 0., 1.]])
        for vert in self.vertices:
            vert.vector = vert.vector.dot(rx_matrix.dot(ry_matrix).dot(rz_matrix))

        return rx_matrix;


    def Translate(self, x, y, z):
        t_matrix = self.TranslateMatrix = np.array([[1., 0., 0., x],
                      [0., 1., 0., y],
                      [0., 0., 1., z],
                      [0., 0., 0., 1.]])

        for vert in self.vertices:
            vert.vector = vert.vector.dot(t_matrix)
            print(vert.vector[3])

        return t_matrix;



    def Render(self, surface, cam):
        """
        THIS CODE USED TO RENDER ONLY DOTS ON EDGES. REPLACED BY LINE DRAWING BELOW!
        v = Vector4(0. ,0. ,0. ,0.)

        for vert in self.vertices:

            v = vert.vector[2]
            vert.vector[2] += 15

            x = vert.retx()*(300/vert.retz())
            y = vert.rety()*(300/vert.retz())
            #print((int(x) + int(surface.get_width()/2), int(y) + int(surface.get_height()/2)))
            #if (x>=0 and y>=0 and x<surface.get_width() and y<surface.get_height()):
            #pygame.draw.circle(surface, (0,0,0), (int(x) + int(surface.get_width()/2), int(y) + int(surface.get_height()/2)), 2)
            #print(int(x))
            #pygame.gfxdraw.aacircle(surface, int(x) + int(surface.get_width()/2), int(y) + int(surface.get_height()/2), 1, (0,0,0))
            vert.vector[2] = v

        #   Render edges!


        for edge in self.edges:
            points =[]

            for vertedge in (self.vertices[edge[0]], self.vertices[edge[1]]):
                ev = vertedge.vector[2]
                vertedge.vector[2] += 15
                ex = vertedge.retx() * (300 / vertedge.retz())
                ey = vertedge.rety() * (300 / vertedge.retz())
                points+=[(int(ex) + int(surface.get_width()/2), int(ey) + int(surface.get_height()/2))]

                vertedge.vector[2]=ev
            pygame.draw.line(surface, (0,0,0), points[0], points[1], 1)

        """

        points = []

        for vert in self.vertices:

            x,y,z = vert.vector[0],vert.vector[1],vert.vector[2]
            x-=cam.position[0]; y-=cam.position[1]; z-=cam.position[2]

            f=500/z

            ex, ey = x * f, y * f
            points += [(int(ex) + int(surface.get_width() / 2), int(ey) + int(surface.get_height() / 2))]


        face_list = []; face_color = []; depth = []
        for face in self.faces:
           for i in face:
               coords = [points[i] for i in face]
               face_list += [coords]
               face_color += [self.colors[self.faces.index(face)]]



        #order = sorted(range(len(face_list)), key=lambda i:depth[i], reverse=1)

        for i in range(len(face_list)):
                pygame.draw.polygon(surface, face_color[i], face_list[i])

