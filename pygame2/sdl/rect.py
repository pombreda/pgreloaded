"""
Wrapper methods around the SDL 2 rect routines.
"""
import ctypes
from pygame2.sdl import dll, sdltype, SDL_TRUE
import pygame2.array as array

__all__ = ["SDL_Point", "SDL_Rect", "enclose_points", "has_intersection",
           "intersect_rect", "intersect_rect_and_line", "union_rect",
           "rect_empty", "rect_equals"
           ]


class SDL_Point(ctypes.Structure):
    """A simple 2D coordinate class."""
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

    def __init__(self, x=0, y=0):
        super(SDL_Point, self).__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        return "SDL_Point(x=%d, y=%d)" % (self.x, self.y)

    def __copy__(self):
        return SDL_Point(self.x, self.y)

    def __deepcopy__(self, memo):
        return SDL_Point(self.x, self.y)

    def __eq__(self, pt):
        return self.x == pt.x and self.y == pt.y

    def __ne__(self, pt):
        return self.x != pt.x or self.y != pt.y


class SDL_Rect(ctypes.Structure):
    """A simple 2D rectangular area class."""
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int),
                ("w", ctypes.c_int), ("h", ctypes.c_int)]

    def __init__(self, x=0, y=0, w=0, h=0):
        super(SDL_Rect, self).__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self):
        return "SDL_Rect(x=%d, y=%d, w=%d, h=%d)" % (self.x, self.y, self.w,
                                                     self.h)

    def __copy__(self):
        return SDL_Rect(self.x, self.y, self.w, self.h)

    def __deepcopy__(self, memo):
        return SDL_Rect(self.x, self.y, self.w, self.h)

    def __eq__(self, rt):
        return self.x == rt.x and self.y == rt.y and \
            self.w == rt.w and self.h == rt.h

    def __ne__(self, rt):
        return self.x != rt.x or self.y != rt.y or \
            self.w != rt.w or self.h != rt.h


@sdltype("SDL_EnclosePoints", [ctypes.POINTER(SDL_Point), ctypes.c_int,
                               ctypes.POINTER(SDL_Rect),
                               ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def enclose_points(points, clip=None):
    """Calculates the minimum rectangle enclosing the passed point list.

    If the clip rectangle is passed, all points outside that rectangle will be
    ignored.
    """
    result = SDL_Rect()

    if clip is not None and not isinstance(clip, SDL_Rect):
        raise TypeError("clip must be a SDL_Rect or None")

    arptr, count = array.to_ctypes(points, SDL_Point)
    arptr = ctypes.cast(arptr, ctypes.POINTER(SDL_Point))
    if count == 0:
        return False, SDL_Rect()

    clipval = None
    if clip is not None:
        clipval = ctypes.byref(clip)
    retval = dll.SDL_EnclosePoints(arptr, count, clipval, ctypes.byref(result))
    return (retval == SDL_TRUE), result


@sdltype("SDL_HasIntersection", [ctypes.POINTER(SDL_Rect),
                                 ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def has_intersection(recta, rectb):
    """Checks, if the passed rectangles intersect."""
    if not isinstance(recta, SDL_Rect) or not isinstance(rectb, SDL_Rect):
        raise TypeError("recta and rectb must be SDL_Rect instances")
    ret = dll.SDL_HasIntersection(ctypes.byref(recta), ctypes.byref(rectb))
    return ret == SDL_TRUE


@sdltype("SDL_IntersectRect", [ctypes.POINTER(SDL_Rect),
                               ctypes.POINTER(SDL_Rect),
                               ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def intersect_rect(recta, rectb):
    """Calculates the intersection area of the passed rectangles.

    The first return value will be True, if both rectangles intersect,
    otherwise False. If both rectangles intersect, the second return value
    denotes the  intersection area of both rectangles. If there is no
    intersection, the returned SDL_Rect value is undefined.
    """
    if not isinstance(recta, SDL_Rect) or not isinstance(rectb, SDL_Rect):
        raise TypeError("recta and rectb must be SDL_Rect instances")
    result = SDL_Rect()
    ret = dll.SDL_IntersectRect(ctypes.byref(recta), ctypes.byref(rectb),
                                ctypes.byref(result))
    return (ret == SDL_TRUE), result


@sdltype("SDL_IntersectRectAndLine", [ctypes.POINTER(SDL_Rect),
                                      ctypes.POINTER(ctypes.c_int),
                                      ctypes.POINTER(ctypes.c_int),
                                      ctypes.POINTER(ctypes.c_int),
                                      ctypes.POINTER(ctypes.c_int)],
         ctypes.c_int)
def intersect_rect_and_line(rect, x1, y1, x2, y2):
    """Calculates the intersection of a SDL_Rect and line.

    If the rect intersects with the line, the line portion of the
    intersection will be returned as a tuple, along with a bool
    indicator True that an intersection took place. Otherwise the bool
    indicator False will be returned with the original line.

    Example:

    # Intersection
    rect = SDL_Rect(0, 0, 10, 10)
    x1, y1, x2, y2 = -20, -20, 30, 30
    print(intersect_rect_and_line(rect, x1, y1, x2, y2)
    # prints(True, 0, 0, 10, 10)

    # No intersection
    rect = SDL_Rect(-4, -4, 14, 14)
    x1, y1, x2, y2 = 8, 22, 8, 33
    print(intersect_rect_and_line(rect, x1, y1, x2, y2)
    # prints(False, 0, 0, 10, 10)
    """
    if not isinstance(rect, SDL_Rect):
        raise TypeError("rect must be a SDL_Rect")

    a1, a2 = ctypes.c_int(x1), ctypes.c_int(y1)
    b1, b2 = ctypes.c_int(x2), ctypes.c_int(y2)
    ret = dll.SDL_IntersectRectAndLine(ctypes.byref(rect), ctypes.byref(a1),
                                       ctypes.byref(a2), ctypes.byref(b1),
                                       ctypes.byref(b2))
    return (ret == SDL_TRUE), a1.value, a2.value, b1.value, b2.value


@sdltype("SDL_UnionRect", [ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect),
                           ctypes.POINTER(SDL_Rect)], None)
def union_rect(recta, rectb):
    """Calculates the union of the passed rects."""
    if not isinstance(recta, SDL_Rect) or not isinstance(rectb, SDL_Rect):
        raise TypeError("recta and rectb must be SDL_Rect instances")
    result = SDL_Rect()
    dll.SDL_UnionRect(ctypes.byref(recta), ctypes.byref(rectb),
                      ctypes.byref(result))
    return result


def rect_empty(rect):
    """Checks, if the width and height of the rect are smaller than or equal
    to 0.
    """
    if not isinstance(rect, SDL_Rect):
        raise TypeError("rect must be a SDL_Rect")
    return rect.w <= 0 or rect.h <= 0


def rect_equals(recta, rectb):
    """Checks, if the passed rects are equal."""
    if not isinstance(recta, SDL_Rect) or not isinstance(rectb, SDL_Rect):
        raise TypeError("recta and rectb must be SDL_Rect instances")
    return recta == rectb
