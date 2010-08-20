import os, sys
##
## You can disable the components you do not want to support by setting them
## to False. If you e.g. do not need or want SDL_mixer support, simply set
##
##    WITH_SDL_MIXER = False
##
## In case certain parts do not build, try to disable them.
## 
##
## Default values for the build are specified in defaults = { ... }.
## Those will be overriden by detected WITH_xxx environment
## variables. You also can manually adjust the settings within this
## dictionary.
##
defaults = {
    # SDL Support.
    # This MUST be enabled for the other SDL related modules.
    'WITH_SDL'          : True,

    # SDL_mixer support.
    'WITH_SDL_MIXER'    : True,

    # SDL_image support.
    'WITH_SDL_IMAGE'    : True,

    # SDL_gfx support.
    'WITH_SDL_GFX'      : True,

    # SDL_ttf support.
    'WITH_SDL_TTF'      : True,

    # libpng support.
    # This is used by Surface.save() to enable PNG saving.
    'WITH_PNG'          : True,

    # libjpeg support.
    # This is used by Surface.save() to enable JPEG saving.
    'WITH_JPEG'         : True,

    # freetype (module) support.
    'WITH_FREETYPE'     : True,
    
    # midi (module) support.
    'WITH_PORTMIDI'     : True,
    
    # OpenAL (module) support.
    'WITH_OPENAL'       : True,
    
    # Open Multiprocessing support.
    'WITH_OPENMP'       : True,
    
    # Experimental modules support.
    'WITH_EXPERIMENTAL' : False,
    }

if sys.version_info[0] >= 3:
    unicode = str

# Check function for the environment flags.
def istrue (val):
    valset = os.getenv (val, None)
    if valset is None:
        if val in defaults:
            return defaults[val]
        return False
    if type (valset) in (str, unicode):
        return valset.lower () in ("yes", "true", "1")
    return valset in (1, True)

# build flags 
build = {
    'SDL'          : istrue ('WITH_SDL'),
    'SDL_MIXER'    : istrue ('WITH_SDL_MIXER') and istrue ('WITH_SDL'),
    'SDL_IMAGE'    : istrue ('WITH_SDL_IMAGE') and istrue ('WITH_SDL'),
    'SDL_GFX'      : istrue ('WITH_SDL_GFX') and istrue ('WITH_SDL'),
    'SDL_TTF'      : istrue ('WITH_SDL_TTF') and istrue ('WITH_SDL'),
    'PNG'          : istrue ('WITH_PNG'),
    'JPEG'         : istrue ('WITH_JPEG'),
    'FREETYPE'     : istrue ('WITH_FREETYPE'),
    'PORTMIDI'     : istrue ('WITH_PORTMIDI'),
    'OPENAL'       : istrue ('WITH_OPENAL'),
    'OPENMP'       : istrue ('WITH_OPENMP'),
    'EXPERIMENTAL' : istrue ('WITH_EXPERIMENTAL'),
    }
