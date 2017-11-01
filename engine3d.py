import numpy as np
#
#   Class is defining camera object
#
class camera:
    def __init__(self, position, target):

        # Camera position in space
        self.position = np.array(position)

        # Where is camera looking?
        self.target = np.array(target)

#
#   Class is defining shape (mesh). Takes name and vertices count as input.
#
class mesh:
    def __init__(self, name, verts_count):
        self.name = name
        self.vertices = [np.array([0., 0., 0.])] * verts_count
        self.position = np.array([0., 0., 0.])
        self.rotation = np.array([0., 0., 0.])





