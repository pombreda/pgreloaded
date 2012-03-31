"""
Wrapper methods around the SDL2 rwops routines.
"""
import ctypes
import sys
from pygame2.compat import *
from pygame2.sdl import sdltype, dll
from pygame2.sdl.error import SDLError

RW_SEEK_SET = 0
RW_SEEK_CUR = 1
RW_SEEK_END = 2

class SDL_RWops (ctypes.Structure):
    pass

_sdlseek = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.POINTER(SDL_RWops),
                            ctypes.c_long, ctypes.c_int)
_sdlread = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(SDL_RWops),
                            ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
_sdlwrite = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(SDL_RWops),
                             ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
_sdlclose = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(SDL_RWops))


# TODO: do we need the union values below?

#
# Win32 specific RWops information
#
#class _win32buffer (ctypes.Structure):
#    _fields_ = [("data", ctypes.c_void_p),
#                ("size", ctypes.c_int),
#                ("left", ctypes.c_int)
#                ]

#class _win32windowsio (ctypes.Structure)
#    _fields_ = [("append", ctypes.c_int),
#                ("h", ctypes.c_void_p),
#                ("buffer", _win32buffer)
#                ]

#
# Android specific RWops information
#
#class _androidio (ctypes.Structure):
#    _fields_ = [("filename", ctypes.c_void_p),
#                ("filenameref", ctypes.c_void_p),
#                ("inputstream", ctypes.c_void_p),
#                ("inputstreamref", ctypes.c_void_p),
#                ("readablebytechannel", ctypes.c_void_p),
#                ("readablebytechannelref", ctypes.c_void_p),
#                ("readmethod", ctypes.c_void_p),
#                ("position", ctypes.c_long),
#                ("size", ctypes.c_int),
#                ]

#class _stdio (ctypes.Structure):
#    _fields_ = [("autoclose", ctypes.c_int),
#                ("fp", ctypes.c_void_p) # FILE*
#                ]

class _mem (ctypes.Structure):
    _fields_ = [("base", ctypes.POINTER(ctypes.c_ubyte)),
                ("here", ctypes.POINTER(ctypes.c_ubyte)),
                ("stop", ctypes.POINTER(ctypes.c_ubyte)),
                ]
class _unknown (ctypes.Structure):
    _fields_ = [("data1", ctypes.c_void_p)]

SDL_RWops._fields_ = [("seek", _sdlseek),
                      ("read", _sdlread),
                      ("write", _sdlwrite),
                      ("close", _sdlclose),
                      ("type", ctypes.c_uint),
                      # TODO: omitted the union here...
                      ("_mem", _mem),
                      ("_unknown", _unknown)
                      ]

@sdltype("SDL_RWFromFile", [ctypes.c_char_p, ctypes.c_char_p],
         ctypes.POINTER(SDL_RWops))
def rw_from_file (filename, mode):
    """rw_from_file (filename, mode) -> SDL_RWops
    
    Creates a new SDL_RWops from a file.
    
    mode specifies the access mode for the file and as such is similar to what
    you can pass to open().
    """
    filename = byteify (filename, "utf-8")
    mode = byteify (mode, "utf-8")
    retval = dll.SDL_RWFromFile (filename, mode)
    if retval is None or not bool(retval):
        raise SDLError ()
    return retval.contents

@sdltype("SDL_RWFromFP", [ctypes.c_void_p, ctypes.c_int],
         ctypes.POINTER(SDL_RWops))
def rw_from_fp (fp, autoclose):
    """rw_from_fp (fp, autoclose) -> SDL_RWops
    
    Creates a SDL_RWops from a file handle.
    
    TODO
    
    """
    ptr = cast (fp, ctypes.c_void_p)
    if autoclose:
        retval = dll.SDL_RWFromFP (ptr, 1)
    else:
        retval = dll.SDL_RWFromFP (ptr, 0)
    if retval is None or not bool(retval):
        raise SDLError ()
    return retval.contents

@sdltype("SDL_RWFromMem", [ctypes.c_void_p, ctypes.c_int],
         ctypes.POINTER(SDL_RWops))
def rw_from_mem (mem, size):
    """rw_from_mem (mem, size) -> SDL_RWops
    
    Creates a SDL_RWops from a contiguous memory region.
    
    TODO
    """
    ptr = ctypes.c_void_p (mem)
    retval = dll.SDL_RWFromMem (mem, size)
    if retval is None or not bool(retval):
        raise SDLError ()
    return retval.contents

@sdltype("SDL_RWFromConstMem", [ctypes.c_void_p, ctypes.c_int],
         ctypes.POINTER(SDL_RWops))
def rw_from_const_mem (mem, size):
    """rw_from_const_mem (mem, size) -> SDL_RWops
    
    Creates a SDL_RWops from a contiguous memory region.
    
    TODO
    """
    ptr = ctypes.c_void_p (mem)
    retval = dll.SDL_RWFromMem (mem, size)
    if retval is None or not bool(retval):
        raise SDLError ()
    return retval.contents

def rw_from_object (obj):
    """rw_from_object (obj) -> SDL_RWops
    
    Python helper to create a SDL_RWops from any Python object, which at least
    supports the following methods:
    
        read (length) -> data
            length is the size in bytes to be read. A call to len (data) must
            return the correct amount of bytes for the data, so that
            len (data) / [size in bytes for a single element from data] returns
            the amount of elements.
            Must raise an error on failure.
        
        seek (offset, whence) -> int
            offset denotes the offset to move the read/write pointer of the
            object to. whence indicates the movement behaviour and can be one
            of the following values:
                RW_SEEK_SET - move to offset from the start of the file 
                RW_SEEK_CUR - move by offset from the relative location
                RW_SEEK_END - move to offset from the end of the file
            If it could not move read/write pointer to the desired location,
            an error must be raised.
        
        tell () -> int
            Must return the current offset. This method must only be
            provided, if seek() does not return any value.
            
        close () -> None
            Closes the object (or its internal data access methods). Must raise
            an error on failure.

        write (data) -> None
            Writes the passed data (which is a string of bytes) to the object.
            Must raise an error on failure.
        
        Note: The write() method is optional and only necessary, if the passed
        object should be able to write data.
    """
    if not hasattr (obj, "read"):
        raise TypeError ("obj must have a read(len) -> data method")
    if not hasattr (obj, "seek") or not callable (obj.seek):
        raise TypeError ("obj must have a seek(offset, whence) method")
    if not hasattr (obj, "close") or not callable (obj.close):
        raise TypeError ("obj must have a close() -> int method")

    rwops = SDL_RWops ()
        
    def _rwseek (context, offset, whence):
        try:
            retval = obj.seek (offset, whence)
            if retval is None:
                retval = obj.tell ()
            return retval
        except Exception as e:
            #print (e)
            return -1
    rwops.seek = _sdlseek (_rwseek)
    
    def _rwread (context, ptr, size, maxnum):
        try:
            data = obj.read (size * maxnum)
            num = len (data)
            ctypes.memmove (ptr, data, num)
            return num
        except Exception as e:
            #print (e)
            return 0
    rwops.read = _sdlread (_rwread)
    
    def _rwclose (context):
        try:
            retval = obj.close ()
            if retval is None:
                # No return value; we assume that everything is okay.
                return 0
            return retval
        except Exception as e:
            #print (e)
            return -1
    rwops.close = _sdlclose (_rwclose)
    
    def _rwwrite (context, ptr, size, num):
        try:
            # string_at feels wrong, since we access a raw byte buffer...
            retval = obj.write (ctypes.string_at (ptr, size * num))
            if retval is None:
                # No return value; we assume that everything is okay.
                return num
            return retval
        except Exception as e:
            #print (e)
            return 0
    
    if hasattr (obj, "write") and callable (obj.write):
        rwops.write = _sdlwrite (_rwwrite)
    else:
        rwops.write = None
    return rwops

def rw_seek (ctx, offset, whence):
    """rw_seek (ctx, offset, whence) -> int
    """
    if not isinstance (ctx, SDL_RWops):
        raise TypeError ("ctx must be a SDL_RWops")
    return ctx.seek (ctypes.byref (ctx), offset, whence)

def rw_tell (ctx):
    """rw_tell () -> int
    """
    if not isinstance (ctx, SDL_RWops):
        raise TypeError ("ctx must be a SDL_RWops")
    retval = ctx.seek (ctypes.byref (ctx), 0, RW_SEEK_CUR)
    if retval is None:
        return ctw.tell ()
    return retval

def rw_read (ctx, ptr, size, n):
    """rw_read (ctx, otr, size, n) -> int
    """
    raise NotImplementedError ("not implemented")
    #if not isinstance (ctx, SDL_RWops):
    #    raise TypeError ("ctx must be a SDL_RWops")
    #return ctx.read (ctypes.byref(ctx), ctypes.byref (ptr), size, n)

def rw_write (ctx, ptr, size, n):
    """rw_write (ctx, ptr, size, n) -> int
    """
    raise NotImplementedError ("not implemented")
    #if not isinstance (ctx, SDL_RWops):
    #    raise TypeError ("ctx must be a SDL_RWops")
    #return ctx.write (ctypes.byref (ctx), ctypes.byref (ptr), size, n)

def rw_close (ctx):
    """rw_close (ctx) -> int
    """
    if not isinstance (ctx, SDL_RWops):
        raise TypeError ("ctx must be a SDL_RWops")
    return ctx.close (ctypes.byref (ctx))

@sdltype("SDL_AllocRW", None, ctypes.POINTER(SDL_RWops))
def alloc_rw ():
    """alloc_rw () -> SDL_RWops
    
    Allocates an empty SDL_RWops instance.
    
    This method is mainly for use with unmanaged code, which should gain full
    access to the SDL features. It should not be used within Python.
    
    The return value must be freed using pygame2.sdl.rwops.free_rw ().
    """
    retval = dll.SDL_AllocRW ()
    if retval is None or not bool(retval):
        raise SDLError ()
    return retval.contents

@sdltype("SDL_FreeRW", [ctypes.POINTER(SDL_RWops)], None)
def free_rw (rwops):
    """free_rw (rwops) -> None
    
    Frees a SDL_RWops, which was allocated by pygame2.sdl.rwops.alloc_rw ().
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    dll.SDL_FreeRW (ctypes.byref(rwops))

@sdltype("SDL_ReadLE16", [ctypes.POINTER(SDL_RWops)], ctypes.c_ushort)
def read_le_16 (rwops):
    """read_le_16 (rwops) -> int
    
    Reads a single 16-bit value from the underlying SDL_RWops in little-endian
    byte order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_ReadLE16 (ctypes.byref (rwops))

@sdltype("SDL_ReadBE16", [ctypes.POINTER(SDL_RWops)], ctypes.c_ushort)
def read_be_16 (rwops):
    """read_be_16 (rwops) -> int

    Reads a single 16-bit value from the underlying SDL_RWops in big-endian
    byte order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_ReadBE16 (ctypes.byref (rwops))

@sdltype("SDL_ReadLE32", [ctypes.POINTER(SDL_RWops)], ctypes.c_uint)
def read_le_32 (rwops):
    """read_le_32 (rwops) -> int
    
    Reads a single 32-bit value from the underlying SDL_RWops in little-endian
    byte order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_ReadLE32 (ctypes.byref (rwops))

@sdltype("SDL_ReadBE32", [ctypes.POINTER(SDL_RWops)], ctypes.c_uint)
def read_be_32 (rwops):
    """read_be_32 (rwops) -> int
    
    Reads a single 32-bit value from the underlying SDL_RWops in big-endian
    byte order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_ReadBE32 (ctypes.byref (rwops))

@sdltype("SDL_ReadLE64", [ctypes.POINTER(SDL_RWops)], ctypes.c_ulonglong)
def read_le_64 (rwops):
    """read_le_64 (rwops) -> int
    
    Reads a single 64-bit value from the underlying SDL_RWops in little-endian
    byte order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_ReadLE64 (ctypes.byref (rwops))

@sdltype("SDL_ReadBE64", [ctypes.POINTER(SDL_RWops)], ctypes.c_ulonglong)
def read_be_64 (rwops):
    """read_be_64 (rwops) -> int
    
    Reads a single 64-bit value from the underlying SDL_RWops in big-endian
    byte order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_ReadBE64 (ctypes.byref (rwops))

@sdltype("SDL_WriteLE16", [ctypes.POINTER(SDL_RWops), ctypes.c_ushort],
         ctypes.c_int)
def write_le_16 (rwops, value):
    """write_le_16 (rwops, value) -> int
    
    Writes a single 16-bit to the underlying SDL_RWops in little-endian byte
    order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_WriteLE16 (ctypes.byref (rwops), value)

@sdltype("SDL_WriteBE16", [ctypes.POINTER(SDL_RWops), ctypes.c_ushort],
         ctypes.c_int)
def write_be_16 (rwops, value):
    """write_be_16 (rwops, value) -> int
    
    Writes a single 16-bit to the underlying SDL_RWops in big-endian byte
    order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_WriteBE16 (ctypes.byref (rwops), value)

@sdltype("SDL_WriteLE32", [ctypes.POINTER(SDL_RWops), ctypes.c_uint],
         ctypes.c_int)
def write_le_32 (rwops, value):
    """write_le_32 (rwops, value) -> int
    
    Writes a single 32-bit to the underlying SDL_RWops in little-endian byte
    order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_WriteLE32 (ctypes.byref (rwops), value)

@sdltype("SDL_WriteBE32", [ctypes.POINTER(SDL_RWops), ctypes.c_uint],
         ctypes.c_int)
def write_be_32 (rwops, value):
    """write_be_32 (rwops, value) -> int
    
    Writes a single 32-bit to the underlying SDL_RWops in big-endian byte
    order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    return dll.SDL_WriteBE32 (ctypes.byref (rwops), value)

@sdltype("SDL_WriteLE64", [ctypes.POINTER(SDL_RWops), ctypes.c_ulonglong],
         ctypes.c_int)
def write_le_64 (rwops, value):
    """write_le_64 (rwops, value) -> int
    
    Writes a single 64-bit to the underlying SDL_RWops in little-endian byte
    order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    val = ctypes.c_ulonglong (value)
    return dll.SDL_WriteLE64 (ctypes.byref (rwops), val)

@sdltype("SDL_WriteBE64", [ctypes.POINTER(SDL_RWops), ctypes.c_ulonglong],
         ctypes.c_int)
def write_be_64 (rwops, value):
    """write_be_64 (rwops, value) -> int
    
    Writes a single 64-bit to the underlying SDL_RWops in big-endian byte
    order.
    """
    if not isinstance (rwops, SDL_RWops):
        raise TypeError ("rwops must be a SDL_RWops")
    val = ctypes.c_ulonglong (value)
    return dll.SDL_WriteBE64 (ctypes.byref (rwops), val)

