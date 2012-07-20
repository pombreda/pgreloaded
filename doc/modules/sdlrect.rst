.. module:: pygame2.sdl.rect
   :synopsis: SDL2 rect wrapper

:mod:`pygame2.sdl.rect` - SDL2 rect wrapper
===========================================

.. class:: SDL_Point(x=0, y=0)

   A simple 2D coordinate class.

   This wraps `SDL_Point`

   .. attribute:: x

      The x offset of the point.

   .. attribute:: y

      The y offset of the point.

.. class:: SDL_Rect(x=0, y=0, w=0, h=0)

   A simple 2D rectangular area class.

   This wraps `SDL_Rect`.

   .. attribute:: x

      The x offset (top-left) of the rect.

   .. attribute:: y

      The y offset (top-left) of the rect.

   .. attribute:: w

      The width of the rect.

   .. attribute:: h

      The height of the rect.

.. function:: enclose_points(points : iterable[, clip=None]) -> (bool, SDL_Rect)

   Calculates the minimum rectangle enclosing the passed :class:`SDL_Point`
   list. If a *clip* rectangle is passed, all points outside that rectangle
   will be ignored.

   This wraps `SDL_EnclosePoints`.

.. function:: has_intersection(recta : SDL_Rect, rectb : SDL_Rect) -> bool

   Checks, if the passed rectangles intersect.

   This wraps `SDL_HasIntersection`.

.. function:: intersect_rect(recta : SDL_Rect, rectb : SDL_Rect) -> (bool, SDL_Rect)

   Calculates the intersection area of the passed rectangles. The first return
   value will be ``True``, if both rectangles intersect, otherwise ``False``.
   If both rectangles intersect, the second return value denotes the
   intersection area of both rectangles. If there is no intersection, the
   returned :class:`SDL_Rect` value is undefined.

   This wraps `SDL_IntersectRect`.

.. function:: intersect_rect_and_line(rect : SDL_Rect, x1 : int, y1 : int, \
                                      x2 : int, y2 : int) -> (bool, int, int, int, int)

   Calculates the intersection of a :class:`SDL_Rect` and line. If the *rect*
   intersects with the line, the line portion of the intersection will be
   returned as a tuple, along with a bool indicator ``True`` that an
   intersection took place. Otherwise the bool indicator ``False`` will be
   returned with the original line. ::

     >>> # Intersection
     >>> rect = SDL_Rect(0, 0, 10, 10)
     >>> x1, y1, x2, y2 = -20, -20, 30, 30
     >>> print(intersect_rect_and_line(rect, x1, y1, x2, y2)
     (True, 0, 0, 10, 10)

     >>> # No intersection
     >>> rect = SDL_Rect(-4, -4, 14, 14)
     >>> x1, y1, x2, y2 = 8, 22, 8, 33
     >>> print(intersect_rect_and_line(rect, x1, y1, x2, y2)
    (False, 0, 0, 10, 10)

   This wraps `SDL_IntersectRectAndLine`.

.. function:: union_rect(recta : SDL_Rect, rectb : SDL_Rect) -> SDL_Rect

   Calculates the union of the passed rects.

   This wraps `SDL_UnionRect`.

.. function:: rect_empty(rect : SDL_Rect) -> bool

   Checks, if the width and height of the rect are smaller than or equal to 0.

   This wraps `SDL_RectEmpty`.

.. function:: rect_equals(recta : SDL_Rect, rectb : SDL_Rect) -> bool

   Checks, if the passed rects are equal.

   This wraps `SDL_RectEquals`.
