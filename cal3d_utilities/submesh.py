"""Representation of submesh in Cal3D space"""


class Submesh:
    def __init__(self, verts, faces, mtl):
        self.verts = verts
        self.faces = faces
        self.mtl = mtl
