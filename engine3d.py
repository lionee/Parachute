import numpy as np
#
# Point
#
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

#
# Vertex4
#
class Vector4:
    def __init__(self, x, y, z, w):
        self.vertex4 = np.array([x, y, z, w])

    def print_vertex4(self):
        print(self.vertex4)

    def get_nparray(self):
        return self.vertex4
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
        self.vertices = [np.array(Vector4(0., 0., 0., 0.))] * verts_count
        self.position = np.array([0., 0., 0.])
        self.rotation = np.array([0., 0., 0.])
        self.mvp = Vector4(0. ,0. ,0. ,0.)

    def Scale(self, x, y, z):
        s_matrix = self.ScaleMatrix = np.array([[x, 0., 0., 0.],
                      [0., y, 0., 0.],
                      [0., 0., z, 0.],
                      [0., 0., 0., 1.]])

        return s_matrix;

    def Translate(self, x, y, z):
        t_matrix = self.TranslateMatrix = np.array([[1, 0., 0., x],
                      [0., 1, 0., y],
                      [0., 0., 1, z],
                      [0., 0., 0., 1.]])

        return t_matrix;

    def Transform(self):

        for vert in self.vertices:
            mvp = self.ScaleMatrix.dot(self.TranslateMatrix.dot(vert.get_nparray()))
            print(mvp)

    def GetProjectionMatrix(self):
        return self.mvp;


    def Project(self, coord, TransMat):
        p = Point()

        print(coord)
        print("DDDD")
        print(TransMat.get_nparray())

    def Print(self):
        for vert in self.vertices:
            vert.print_vertex4()


#
#   Class doing magic
#
"""
class Engine3d:
    def Render(self, camera, meshes):

    def Project(self, coord, transMatrix):
        point = TransformCoordinate(coord, transMatrix)
"""