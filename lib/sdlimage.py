"""
A thin wrapper package around the SDL2_image library.
"""
import sys
import ctypes
from pygame2.dll import DLL
from pygame2.compat import byteify, stringify
from pygame2.sdl.version import SDL_version
from pygame2.sdl.surface import SDL_Surface
from pygame2.sdl.rwops import SDL_RWops
from pygame2.sdl.render import SDL_Renderer, SDL_Texture

__all__ = ["init", "quit", "load", "load_rw", "load_typed_rw",
           "load_texture", "load_texture_rw", "load_texture_typed_rw",
           "is_ico", "is_cur", "is_bmp", "is_gif", "is_jpg", "is_lbm",
           "is_pcx", "is_pnm", "is_png", "is_pnm", "is_tif", "is_webp",
           "is_xcf", "is_xpm", "is_xv", "load_bmp_rw", "load_cur_rw",
           "load_gif_rw", "load_ico_rw", "load_jpg_rw", "load_lbm_rw",
           "load_pcx_rw", "load_pnm_rw", "load_png_rw", "load_tga_rw",
           "load_tif_rw", "load_webp_rw", "load_xcf_rw", "load_xpm_rw",
           "load_xv_rw", "IMG_INIT_JPG", "IMG_INIT_PNG", "IMG_INIT_TIF",
           "IMG_INIT_WEBP",
           ]


dll = DLL("SDL2_image", ["SDL2_image", "SDL2_image-1.2"])
sdlimgtype = dll.get_decorator()

SDL_Surface_p = ctypes.POINTER(SDL_Surface)
SDL_RWops_p = ctypes.POINTER(SDL_RWops)
SDL_Renderer_p = ctypes.POINTER(SDL_Renderer)
SDL_Texture_p = ctypes.POINTER(SDL_Texture)


IMG_INIT_JPG = 0x00000001
IMG_INIT_PNG = 0x00000002
IMG_INIT_TIF = 0x00000004
IMG_INIT_WEBP = 0x00000008


def _check(ret):
    """Checks the return value of a ctypes function and raises a SDLError,
    if it is invalid (NULL).
    """
    if ret is None or not bool(ret):
        raise SDLError()
    return ret.contents


@sdlimgtype("IMG_Init", [ctypes.c_uint], ctypes.c_int)
def init(flags=(IMG_INIT_JPG | IMG_INIT_PNG)):
    """Initializes the SDL2_image library.

    Initializes the SDL2_image library using the passed bit-wise
    combination of image types defined through the IMG_INIT_ constants.

    Legal values are:

    IMG_INIT_JPG
    IMG_INIT_PNG
    IMG_INIT_TIF
    IMG_INIT_WEBP

    """
    return dll.IMG_Init(flags)


@sdlimgtype("IMG_Quit", None, None)
def quit():
    """Shuts down the SDL2_image library and releases all resources held
    by it.

    Calling SDL2_image related methods after quit() will wake the
    dragons, so do not do it.
    """
    dll.IMG_Quit()


@sdlimgtype("IMG_Linked_Version", None, ctypes.POINTER(SDL_version))
def linked_version():
    """Gets the version of the loaded SDL2_image library."""
    return _check(dll.IMG_Linked_Version())


@sdlimgtype("IMG_Load", [ctypes.c_char_p], SDL_Surface_p)
def load(fname):
    """Load an image into a SDL_Surface from the specified filename.

    Raises a SDLError, if the file could not be loaded.
    """
    return _check(dll.IMG_Load(fname))


@sdlimgtype("IMG_Load_RW", [SDL_RWops_p, ctypes.c_int], SDL_Surface_p)
def load_rw(rwops, freesrc):
    """Load a surface from a seekable data stream.

    If freesrc evaluates to True, the passed stream will be closed after
    being read.

    Raises a SDLError, if the image could not be loaded.
    """
    if not isinstance(rwops, rwops.SDL_RWops):
        raise TypeError("rwops must be a SDL_RWops")
    if bool(freesrc):
        freesrc = 1
    else:
        freesrc = 0
    return _check(dll.IMG_Load_RW(ctypes.byref(rwops), freesrc))


@sdlimgtype("IMG_LoadTyped_RW", [SDL_RWops_p, ctypes.c_int, ctypes.c_char_p],
            SDL_Surface_p)
def load_typed_rw(rwops, freesrc, itype):
    """Load a surface from a seekable data stream.

    itype specifies the image format to use for loading and may be a
    value of "BMP", "GIF", "PNG", etc.

    If freesrc evaluates to True, the passed stream will be closed after
    being read.

    Raises a SDLError, if the image could not be loaded.
    """
    if not isinstance(rwops, rwops.SDL_RWops):
        raise TypeError("rwops must be a SDL_RWops")
    if bool(freesrc):
        freesrc = 1
    else:
        freesrc = 0
    return _check(dll.IMG_LoadTyped_RW(ctypes.byref(rwops), freesrc, itype))


@sdlimgtype("IMG_LoadTexture", [SDL_Renderer_p, ctypes.c_char_p],
            SDL_Texture_p)
def load_texture(renderer, fname):
    """Create a SDL_Texture from the specified filename.

    Raises a SDLError, if the file could not be loaded.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer must be a SDL_Renderer")
    return _check(dll.IMG_LoadTexture(ctypes.byref(renderer), fname))


@sdlimgtype("IMG_LoadTexture_RW", [SDL_Renderer_p, SDL_RWops_p, ctypes.c_int],
            SDL_Texture_p)
def load_texture_rw(renderer, src, freesrc):
    """Create a SDL_Texture from a seekable data stream.

    If freesrc evaluates to True, the passed stream will be closed after
    being read.

    Raises a SDLError, if the image could not be loaded.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer must be a SDL_Renderer")
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    if bool(freesrc):
        freesrc = 1
    else:
        freesrc = 0
    return _check(dll.IMG_LoadTexture_RW(ctypes.byref(renderer),
                                         ctypes.byref(src), freesrc))


@sdlimgtype("IMG_LoadTextureTyped_RW", [SDL_Renderer_p, SDL_RWops_p,
                                        ctypes.c_int, ctypes.c_char_p],
            SDL_Texture_p)
def load_texture_typed_rw(renderer, src, freesrc, itype):
    """Create a SDL_Texture from a seekable data stream.

    itype specifies the image format to use for loading and may be a
    value of "BMP", "GIF", "PNG", etc.

    If freesrc evaluates to True, the passed stream will be closed after
    being read.

    Raises a SDLError, if the image could not be loaded.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer must be a SDL_Renderer")
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    if bool(freesrc):
        freesrc = 1
    else:
        freesrc = 0
    return _check(dll.IMG_LoadTextureTyped_RW(ctypes.byref(renderer),
                                              ctypes.byref(src), freesrc,
                                              itype))


@sdlimgtype("IMG_isICO", [SDL_RWops_p], ctypes.c_int)
def is_ico(src):
    """Checks, if the passed data stream represents ICO image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isICO(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isCUR", [SDL_RWops_p], ctypes.c_int)
def is_cur(src):
    """Checks, if the passed data stream represents CUR image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isCUR(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isBMP", [SDL_RWops_p], ctypes.c_int)
def is_bmp(src):
    """Checks, if the passed data stream represents BMP image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isBMP(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isGIF", [SDL_RWops_p], ctypes.c_int)
def is_gif(src):
    """Checks, if the passed data stream represents GIF image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isGIF(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isJPG", [SDL_RWops_p], ctypes.c_int)
def is_jpg(src):
    """Checks, if the passed data stream represents JPG image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isJPG(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isLBM", [SDL_RWops_p], ctypes.c_int)
def is_lbm(src):
    """Checks, if the passed data stream represents LBM image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isLBM(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isPCX", [SDL_RWops_p], ctypes.c_int)
def is_pcx(src):
    """Checks, if the passed data stream represents PCX image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isPCX(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isPNG", [SDL_RWops_p], ctypes.c_int)
def is_png(src):
    """Checks, if the passed data stream represents PNG image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isPNG(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isPNM", [SDL_RWops_p], ctypes.c_int)
def is_pnm(src):
    """Checks, if the passed data stream represents PNM image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isPNM(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isTIF", [SDL_RWops_p], ctypes.c_int)
def is_tif(src):
    """Checks, if the passed data stream represents TIF image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isTIF(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isXCF", [SDL_RWops_p], ctypes.c_int)
def is_xcf(src):
    """Checks, if the passed data stream represents XCF image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isXCF(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isXPM", [SDL_RWops_p], ctypes.c_int)
def is_xpm(src):
    """Checks, if the passed data stream represents XPM image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isXPM(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isXV", [SDL_RWops_p], ctypes.c_int)
def is_xv(src):
    """Checks, if the passed data stream represents XVimage data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isXV(ctypes.byref(src)) == 1


@sdlimgtype("IMG_isWEBP", [SDL_RWops_p], ctypes.c_int)
def is_webp(src):
    """Checks, if the passed data stream represents WEBP image data."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return dll.IMG_isWEBP(ctypes.byref(src)) == 1


@sdlimgtype("IMG_LoadICO_RW", [SDL_RWops_p], SDL_Surface_p)
def load_ico_rw(src):
    """Loads a SDL_Surface from a ICO data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadICO_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadCUR_RW", [SDL_RWops_p], SDL_Surface_p)
def load_cur_rw(src):
    """Loads a SDL_Surface from a CUR data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadCUR_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadBMP_RW", [SDL_RWops_p], SDL_Surface_p)
def load_bmp_rw(src):
    """Loads a SDL_Surface from a BMP data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadBMP_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadGIF_RW", [SDL_RWops_p], SDL_Surface_p)
def load_gif_rw(src):
    """Loads a SDL_Surface from a GIF data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadGIF_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadJPG_RW", [SDL_RWops_p], SDL_Surface_p)
def load_jpg_rw(src):
    """Loads a SDL_Surface from a JPG data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadJPG_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadLBM_RW", [SDL_RWops_p], SDL_Surface_p)
def load_lbm_rw(src):
    """Loads a SDL_Surface from a LBM data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadLBM_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadPCX_RW", [SDL_RWops_p], SDL_Surface_p)
def load_pcx_rw(src):
    """Loads a SDL_Surface from a PCX data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadPCX_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadPNG_RW", [SDL_RWops_p], SDL_Surface_p)
def load_png_rw(src):
    """Loads a SDL_Surface from a PNG data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadPNG_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadPNM_RW", [SDL_RWops_p], SDL_Surface_p)
def load_pnm_rw(src):
    """Loads a SDL_Surface from a PNM data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadPNM_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadTGA_RW", [SDL_RWops_p], SDL_Surface_p)
def load_tga_rw(src):
    """Loads a SDL_Surface from a TGA data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadTGA_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadTIF_RW", [SDL_RWops_p], SDL_Surface_p)
def load_tif_rw(src):
    """Loads a SDL_Surface from a TIF data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadTIF_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadXCF_RW", [SDL_RWops_p], SDL_Surface_p)
def load_xcf_rw(src):
    """Loads a SDL_Surface from a XCF data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadXCF_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadXPM_RW", [SDL_RWops_p], SDL_Surface_p)
def load_xpm_rw(src):
    """Loads a SDL_Surface from a XPM data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadXPM_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadXV_RW", [SDL_RWops_p], SDL_Surface_p)
def load_xv_rw(src):
    """Loads a SDL_Surface from a XV data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadXV_RW(ctypes.byref(src)))


@sdlimgtype("IMG_LoadWEBP_RW", [SDL_RWops_p], SDL_Surface_p)
def load_webp_rw(src):
    """Loads a SDL_Surface from a WEBP data stream."""
    if not isinstance(src, rwops.SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    return _check(dll.IMG_LoadWEBP_RW(ctypes.byref(src)))


@sdlimgtype("IMG_ReadXPMFromArray", [ctypes.POINTER(ctypes.c_char_p)],
            SDL_Surface_p)
def read_xpm_from_array(xpm):
    """Loads a SDL_Surface from a XPM character buffer."""
    if type(xpm) is not str:
        raise TypeError("xpm must be a string")
    return _check(dll.IMG_ReadXPMFromArray(ctypes.byref(xpm)))
