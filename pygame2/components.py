"""Predefined components."""
from pygame2.ebs import Component

__all__ = ["Position"]


class Position(Component):
    """A simple positional coordinate on a 2D plane or in a 3D room."""
    def __init__(self, x=0, y=0, z=0):
        super(Position, self).__init__()
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]

    def __setitem__(self, index, val):
        tmp = [self.x, self.y, self.z]
        tmp[index] = val
        self.x = tmp[0]
        self.y = tmp[1]
        self.z = tmp[2]
