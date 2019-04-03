"""Extensibility for Cal3D XMF Files"""


class XMF:
    def __init__(self, verts, faces):
        self.verts = verts
        self.faces = faces


def nothing():
    pass

