.. module:: pygame2.sdl.cpuinfo
   :synopsis: SDL2 CPU info wrapper

:mod:`pygame2.sdl.cpuinfo` - SDL2 CPU info wrapper
==================================================

SDL2 CPU info API
-----------------

.. function:: get_cpu_cache_line_size() -> int

   Gets the L1 cache line size.

   This wraps :c:func:`SDL_GetCPUCacheLineSize`.

.. function:: get_cpu_count() -> int

   Gets the number of CPU cores available.

   This wraps :c:func:`SDL_GetCPUCount`.

.. function:: has_3dnow() -> bool

   Checks, if the system has 3DNow! features.

   This wraps :c:func:`SDL_Has3DNow`.

.. function:: has_altivec() -> bool

   Checks, if the system has AltiVec capabilities.

   This wraps :c:func:`SDL_HasAltiVec`.

.. function:: has_mmx() -> bool

   Checks, if the system has MMX features.

   This wraps :c:func:`SDL_HasMMX`.

.. function:: has_rdtsc() -> bool

   Checks, if the system has the RDTSC asm instruction.

   This wraps :c:func:`SDL_HasRDTSC`.

.. function:: has_sse() -> bool

   Checks, if the system has SSE features.

   This wraps :c:func:`SDL_HasSSE`.

.. function:: has_sse2() -> bool

   Checks, if the system has SSE2 features.

   This wraps :c:func:`SDL_HasSSE2`.

.. function:: has_sse3() -> bool

   Checks, if the system has SSE3 features.

   This wraps :c:func:`SDL_HasSSE3`.

.. function:: has_sse41() -> bool

   Checks, if the system has SSE4.1 features.

   This wraps :c:func:`SDL_HasSSE41`.

.. function:: has_sse42() -> bool

   Checks, if the system has SSE4.2 features.

   This wraps :c:func:`SDL_HasSSE42`.
