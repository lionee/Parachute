# Engine is capable of rendering not only flat objects used in this game.
# It can render any 3d object.
#
# TODO: loading objects from Blender exports.
#
#

import numpy as np
import pygame
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


#
#   Class is defining camera object
#
class Camera:
    def __init__(self, position, radian):

        # Camera position and rotation in space
        self.position = list(position)
        self.rotation = radian

    def update(self, dt, key, vrot):

        s = dt / 1000 * abs(vrot)*1.8
        x, y = s * math.sin(self.rotation), s * math.cos(self.rotation)


        if(vrot>0):
            self.position[0] += x; self.position[1] += y

        if(vrot<0):
            self.position[0] -= x; self.position[1] -= y

        if key[pygame.K_d]:
            self.rotation -= 0.15 / 10
        if key[pygame.K_a]:
            self.rotation += 0.15 / 10

#
#   Class is defining shape (mesh). Takes name and vertices count as input.
#
class Mesh:
    def __init__(self, name, verts_count, edges, faces, colors, type):
        self.name = name
        self.vertices = [np.array([0., 0., 0., 0.])] * verts_count
        self.edges = edges
        self.faces = faces
        self.colors = colors
        self.type = type  # Rendering type: 1 - full, 2 - circles
        print("Mesh created:", self.name)

    def __repr__(self):
        return self.name

    def Getz(self):
        sumz = 0
        for vertex in self.vertices:
            sumz += vertex.retz()

        return sumz

    def Scale(self, x, y, z):
        s_matrix = np.array([[x, 0., 0., 0.],
                            [0., y, 0., 0.],
                            [0., 0., z, 0.],
                            [0., 0., 0., 1.]])

        for vert in self.vertices:
            vert.vector = vert.vector.dot(s_matrix)

        return s_matrix

    def Rotate(self, radiansx, radiansy, radiansz):

        rsinx = math.sin(radiansx)
        rcosx = math.cos(radiansx)

        rsiny = math.sin(radiansy)
        rcosy = math.cos(radiansy)

        rsinz = math.sin(radiansz)
        rcosz = math.cos(radiansz)

        # Rotation Matrix around X axis
        rx_matrix = np.array([[rcosx, 0., rsinx, 0.],
                            [0., 1, 0., 0.],
                            [-rsinx, 0., rcosx, 0.],
                            [0., 0., 0., 1.]])
        # Rotation Matrix around Y axis
        ry_matrix = np.array([[1, 0., 0, 0.],
                            [0., rcosy, -rsiny, 0.],
                            [0, rsiny, rcosy, 0.],
                            [0., 0., 0., 1.]])
        # Rotation Matrix around Z axis
        rz_matrix = np.array([[rcosz, -rsinz, 0, 0.],
                            [rsinz, rcosz, 0, 0.],
                            [0, 0, 1, 0.],
                            [0., 0., 0., 1.]])
        for vert in self.vertices:
            vert.vector = vert.vector.dot(rx_matrix.dot(ry_matrix).dot(rz_matrix))

        return rx_matrix

    def Translate(self, x, y, z):
        t_matrix = np.array([[1., 0., 0., x],
                            [0., 1., 0., y],
                            [0., 0., 1., z],
                            [0., 0., 0., 1.]])

        for vert in self.vertices:
            vert.vector = t_matrix.dot(vert.vector)

        return t_matrix

    def rotate2d(self, pos, rad):
        x, y = pos
        s, c = math.sin(rad), math.cos(rad)
        return x * c - y * s, y * c + x * s

    def Render(self, surface, cam, color):
        # We draw dots
        calculated = False
        if (self.type == 1):

            for vert in self.vertices:

                x, y, z = vert.vector[0], vert.vector[1], vert.vector[2]
                x -= cam.position[0]
                y -= cam.position[1]
                z -= cam.position[2]

                x, y = self.rotate2d((x, y), cam.rotation)
                f = 500 / z

                ex, ey = x * f, y * f

                # TODO: Make it as point counting routine
                if (int(cam.position[2]) == int(vert.vector[2]) and calculated == False):
                    # print(int(cam.position[2]), vert.vector[2])
                    calculated = True

                if (cam.position[2] >= vert.vector[2]):
                    try:

                        pygame.draw.circle(surface, color, (int(ex) + int(surface.get_width() / 2), int(ey) + int(surface.get_height() / 2)), int(2/(cam.position[2]-vert.vector[2])*40))
                    except:
                        pass

        vert_list = []
        # Or we draw shapes
        if (self.type == 2):
            points = []

            for vert in self.vertices:
                x, y, z = vert.vector[0], vert.vector[1], vert.vector[2]
                x -= cam.position[0]
                y -= cam.position[1]
                z -= cam.position[2]

                vert_list += [(x,y,z)]
                x, y = self.rotate2d((x, y), cam.rotation)
                f = 500 / z

                ex, ey = x * f, y * f
                points += [(int(ex) + int(surface.get_width() / 2), int(ey) + int(surface.get_height() / 2))]

            face_list = []
            face_color = []
            depth = []

            for f in range(len(self.faces)):
                face = self.faces[f]
                for i in face:
                    coords = [points[i] for i in face]
                    face_list += [coords]
                    face_color += [self.colors[f]]
                    depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

            order = sorted(range(len(face_list)), key=lambda i:depth[i], reverse=True)

            for i in order:
                if(cam.position[2]>vert.vector[2]):
                    try:
                        pygame.draw.polygon(surface, face_color[i], face_list[i])
                    except:
                        pass


def RenderAllMeshes(meshes, alt, surface, camera):

    color = (255, 255, 0)
    for mesh in meshes:
        mesh.Render(surface, camera, color)
