import numpy as np

class camera:
    def __init__(self):
        self.position = np.array([0., 0., 0.])
        self.target = np.array([0., 0., 0.])

class mesh:
    def __init__(self, name, verts_count):
        self.name = name
        self.vertices = [np.array([0., 0., 0.])] * verts_count
        self.position = np.array([0., 0., 0.])
        self.rotation = np.array([0., 0., 0.])





