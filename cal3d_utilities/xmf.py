"""Extensibility for Cal3D XMF Files"""


class XMF:
    def __init__(self, mesh, ver=919):
        self.mesh = mesh
        self.ver = ver
