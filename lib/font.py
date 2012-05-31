"""OS-specific font handling"""
import os
import sys
from subprocess import Popen, PIPE
from pygame2.compat import stringify

# Font cache entries:
# { family : [...,
#             (fonttype=ttf...,name, (bold, italic), filename),
#             ...
#            ]
# }
__FONTCACHE = None


def _cache_fonts_win32():
    pass


def _cache_fonts_darwin():
    pass


def _cache_fonts_fontconfig():
    try:
        command = "fc-list : file family style fullname fullnamelang"
        proc = Popen(command, stdout=PIPE, shell=True, stderr=PIPE)
        pout = proc.communicate()[0]
        output = stringify(pout, "utf-8")
    except OSError:
        return

    __FONTCACHE = {}
    for entry in output.split(os.linesep):
        if entry.strip() == "":
            continue
        values = entry.split(":")
        filename = values[0]

        # get the font type
        fname, fonttype = os.path.splitext(filename)
        if fonttype == ".gz":
            fonttype = os.path.splitext(fname)[1][1:].lower()
        else:
            fonttype = fonttype.lstrip(".").lower()

        # get the font name
        if len(values) > 3:
            fullnames, fullnamelangs = values[3:]
            langs = fullnamelangs.split(",")
            if "fullnamelang=en" in langs:
                offset = langs.index("fullnamelang=en")
            else:
                offset = langs.index("en")
            if offset != -1:
                # got an english name, use that one
                name = fullnames.split(",")[offset]
                if name.startswith("fullname="):
                    name = name[9:]
        else:
            if fname.endswith(".pcf") or fname.endswith(".bdf"):
                name = os.path.basename(fname[:-4])
            else:
                name = os.path.basename(fname)
        name = name.lower()

        # family and styles
        family = values[1].strip().lower()
        style = values[2].strip()

        boldfont = style.find("Bold") >= 0
        italicfont = style.find("Italic") >= 0 or style.find("Oblique") >= 0

        if family not in __FONTCACHE:
            __FONTCACHE[family] = []
        __FONTCACHE[family].append((fonttype, name, (boldfont, italicfont),
                                    filename))


def init():
    """Initialises the internal font cache."""
    if __FONTCACHE is not None:
        return
    if sys.platform in ("win32", "cli"):
        _cache_fonts_win32()
    elif sys.platform == "darwin":
        _cache_fonts_darwin()
    else:
        _cache_fonts_fontconfig()

