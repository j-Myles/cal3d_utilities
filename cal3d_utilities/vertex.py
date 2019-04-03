"""Representation of vertex in Cal3D space"""


class Vertex:
    def __init__(self, v_id, posn, norm, color, uv, infls):
        self.v_id = v_id
        self.posn = posn
        self.norm = norm
        self.color = color
        self.uv = uv
        self.infls = infls
