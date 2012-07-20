.. module:: pygame2.sdl.endian
   :synopsis: SDL2 endian wrapper

:mod:`pygame2.sdl.endian` - SDL2 endian wrapper
===============================================

.. data:: SDL_BYTEORDER

   Indicates the byte order of the executing system. This value will be
   set to either ``SDL_LIL_ENDIAN`` or ``SDL_BIG_ENDIAN`` and is
   determined by :data:`sys.byteorder`.

.. data:: SDL_LIL_ENDIAN

   Little endian byte order identifier.

.. data:: SDL_BIG_ENDIAN

   Big endian byte order identifier.

.. function:: swap16(x : int) -> int

   Swaps the byte order of a 16-bit value.

   This wraps :c:func:`SDL_Swap16`.

.. function:: swap32(x : int) -> int

   Swaps the byte order of a 32-bit value.

   This wraps :c:func:`SDL_Swap32`.

.. function:: swap64(x : int) -> int

   Swaps the byte order of a 64-bit value.

   This wraps :c:func:`SDL_Swap64`.

.. function:: swap_float(x : float) -> float

   Swaps the byte order of a float value.

   .. note::

      This is currently not implemented and will raise a
      :exc:`NotImplementedError`.

   This wraps :c:func:`SDL_SwapFloat`.

.. function:: swap_le_16(x : int) -> int

   Swaps the byte order of a 16-bit value on big-endian systems. Does
   nothing on little-endian systems.

   This wraps :c:func:`SDL_SwapLE16`.

.. function:: swap_le_32(x : int) -> int

   Swaps the byte order of a 32-bit value on big-endian systems. Does
   nothing on little-endian systems.

   This wraps :c:func:`SDL_SwapLE32`.

.. function:: swap_le_64(x : int) -> int

   Swaps the byte order of a 64-bit value on big-endian systems. Does
   nothing on little-endian systems.

   This wraps :c:func:`SDL_SwapLE64`.

.. function:: swap_float_le(x : float) -> float

   Swaps the byte order of a floating point value on big-endian
   systems. Does nothing on little-endian systems.

   This wraps :c:func:`SDL_SwapFloatLE`.

.. function:: swap_be_16(x : int) -> int

   Swaps the byte order of a 16-bit value on little-endian systems. Does
   nothing on big-endian systems.

   This wraps :c:func:`SDL_SwapBE16`.

.. function:: swap_be_32(x : int) -> int

   Swaps the byte order of a 32-bit value on little-endian systems. Does
   nothing on big-endian systems.

   This wraps :c:func:`SDL_SwapBE32`.

.. function:: swap_be_64(x : int) -> int

   Swaps the byte order of a 64-bit value on little-endian systems. Does
   nothing on big-endian systems.

   This wraps :c:func:`SDL_SwapBE64`.

.. function:: swap_float_be(x : float) -> float

   Swaps the byte order of a floating point value on little-endian
   systems. Does nothing on big-endian systems.

   This wraps :c:func:`SDL_SwapFloatLE`.
