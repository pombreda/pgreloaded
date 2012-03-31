"""
Wrapper methods around the SDL2 cpuinfo routines.
"""
import ctypes
from pygame2.sdl import sdltype, dll, SDL_FALSE, SDL_TRUE
from pygame2.sdl.error import SDLError

@sdltype("SDL_GetCPUCacheLineSize", None, ctypes.c_int)
def get_cpu_cache_line_size ():
    """get_cpu_cache_line_size () -> int
    
    Gets the L1 cache line size.
    """
    val = dll.SDL_GetCPUCacheLineSize ()
    if val < 0:
        raise SDLError()
    return val
        
@sdltype("SDL_GetCPUCount", None, ctypes.c_int)
def get_cpu_count ():
    """get_cpu_count () -> int
    
    Gets the number of CPU cores available.
    """
    val = dll.SDL_GetCPUCount ()
    if val < 0:
        raise SDLError()
    return val

@sdltype("SDL_Has3DNow", None, ctypes.c_int)
def has_3dnow ():
    """has_3dnow () -> bool
    
    Checks, if the system has 3DNow! features.
    """
    return dll.SDL_Has3DNow () == SDL_TRUE

@sdltype("SDL_HasAltiVec", None, ctypes.c_int)
def has_altivec ():
    """has_altivec () -> bool
    
    Checks, if the system has AltiVec capabilities.
    """
    return dll.SDL_HasAltiVec () == SDL_TRUE

@sdltype("SDL_HasMMX", None, ctypes.c_int)
def has_mmx ():
    """has_mmx () -> bool
    
    Checks, if the system has MMX features.
    """
    return dll.SDL_HasMMX () == SDL_TRUE

@sdltype("SDL_HasRDTSC", None, ctypes.c_int)
def has_rdtsc ():
    """has_rdtsc () -> bool
    
    Checks, if the system has the RDTSC asm instruction.
    """
    return dll.SDL_HasRDTSC () == SDL_TRUE
    
@sdltype("SDL_HasSSE", None, ctypes.c_int)
def has_sse ():
    """has_sse () -> bool
    
    Checks, if the system has SSE features.
    """
    return dll.SDL_HasSSE () == SDL_TRUE
    
@sdltype("SDL_HasSSE2", None, ctypes.c_int)
def has_sse2 ():
    """has_sse2 () -> bool
    
    Checks, if the system has SSE2 features.
    """
    return dll.SDL_HasSSE2 () == SDL_TRUE
    
@sdltype("SDL_HasSSE3", None, ctypes.c_int)
def has_sse3 ():
    """has_sse3 () -> bool
    
    Checks, if the system has SSE3 features.
    """
    return dll.SDL_HasSSE3 () == SDL_TRUE

@sdltype("SDL_HasSSE41", None, ctypes.c_int)
def has_sse41 ():
    """has_sse41 () -> bool
    
    Checks, if the system has SSE4.1 features.
    """
    return dll.SDL_HasSSE41 () == SDL_TRUE
    
@sdltype("SDL_HasSSE42", None, ctypes.c_int)
def has_sse42 ():
    """has_sse42 () -> bool
    
    Checks, if the system has SSE4.2 features.
    """
    return dll.SDL_HasSSE42 () == SDL_TRUE
