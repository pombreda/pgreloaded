"""
Various, indexed color palettes.

Indexed color palettes. The following palettes are currently available:

+--------------------+---------------------------------------------------+
| MONOPALETTE        | 1-bit monochrome palette (black and white).       |
+--------------------+---------------------------------------------------+
| GRAY2PALETTE       | 2-bit grayscale palette with black, white and two |
|                    | shades of gray.                                   |
+--------------------+---------------------------------------------------+
| GRAY4PALETTE       | 4-bit grayscale palette with black, white and     |
|                    | 14 shades shades of gray.                         |
+--------------------+---------------------------------------------------+
| GRAY8PALETTE       | 8-bit grayscale palette with black, white and     |
|                    | 254 shades shades of gray.                        |
+--------------------+---------------------------------------------------+
| RGB3PALETTE        | 3-bit RGB color palette with pure red, green and  |
|                    | blue and their complementary colors as well as    |
|                    | black and white.                                  |
+--------------------+---------------------------------------------------+
| CGAPALETTE         | CGA color palette.                                |
+--------------------+---------------------------------------------------+
| EGAPALETTE         | EGA color palette.                                |
+--------------------+---------------------------------------------------+
| VGAPALETTE         | 8-bit VGA color palette.                          |
+--------------------+---------------------------------------------------+
| WEBPALETTE         | "Safe" web color palette with 225 colors.         |
+--------------------+---------------------------------------------------+
"""

from pygame2.color import Color, ARGB

__all__ = ["MONOPALETTE", "GRAY2PALETTE", "GRAY4PALETTE", "CGAPALETTE",
           "EGAPALETTE", "WEBPALETTE", "RGB3PALETTE", "VGAPALETTE"]


def _create_8bpp_gray():
    """Creates a 8 bit grayscale color palette."""
    l = []
    for x in range(0x00, 0xF1, 0x10):
        for y in range(0x00, 0x10, 0x01):
            l.append(Color(x | y, x | y, x | y))
    return tuple(l)

MONOPALETTE = (ARGB(0xFF000000), ARGB(0xFFFFFFFF),)

GRAY2PALETTE = (
    ARGB(0xFF000000), ARGB(0xFF555555), ARGB(0xFFAAAAAA), ARGB(0xFFFFFFFF),
    )

GRAY4PALETTE = (
    ARGB(0xFF000000), ARGB(0xFF111111), ARGB(0xFF222222), ARGB(0xFF333333),
    ARGB(0xFF444444), ARGB(0xFF555555), ARGB(0xFF666666), ARGB(0xFF777777),
    ARGB(0xFF888888), ARGB(0xFF999999), ARGB(0xFFAAAAAA), ARGB(0xFFBBBBBB),
    ARGB(0xFFCCCCCC), ARGB(0xFFDDDDDD), ARGB(0xFFEEEEEE), ARGB(0xFFFFFFFF),
    )

GRAY8PALETTE = _create_8bpp_gray()

CGAPALETTE = (
    ARGB(0xFF000000), ARGB(0xFF0000AA), ARGB(0xFF00AA00), ARGB(0xFF00AAAA),
    ARGB(0xFFAA0000), ARGB(0xFFAA00AA), ARGB(0xFFAA5500), ARGB(0xFFAAAAAA),
    ARGB(0xFF555555), ARGB(0xFF5555FF), ARGB(0xFF55FF55), ARGB(0xFF55FFFF),
    ARGB(0xFFFF5555), ARGB(0xFFFF55FF), ARGB(0xFFFFFF55), ARGB(0xFFFFFFFF),
    )

EGAPALETTE = (
    ARGB(0xFF000000), ARGB(0xFF0000AA), ARGB(0xFF00AA00), ARGB(0xFF00AAAA),
    ARGB(0xFFAA0000), ARGB(0xFFAA00AA), ARGB(0xFFAAAA00), ARGB(0xFFAAAAAA),
    ARGB(0xFF000055), ARGB(0xFF0000FF), ARGB(0xFF00AA55), ARGB(0xFF00AAFF),
    ARGB(0xFFAA0055), ARGB(0xFFAA00FF), ARGB(0xFFAAAA55), ARGB(0xFFAAAAFF),
    ARGB(0xFF005500), ARGB(0xFF0055AA), ARGB(0xFF00FF00), ARGB(0xFF00FFAA),
    ARGB(0xFFAA5500), ARGB(0xFFAA55AA), ARGB(0xFFAAFF00), ARGB(0xFFAAFFAA),
    ARGB(0xFF005555), ARGB(0xFF0055FF), ARGB(0xFF00FF55), ARGB(0xFF00FFFF),
    ARGB(0xFFAA5555), ARGB(0xFFAA55FF), ARGB(0xFFAAFF55), ARGB(0xFFAAFFFF),
    ARGB(0xFF550000), ARGB(0xFF5500AA), ARGB(0xFF55AA00), ARGB(0xFF55AAAA),
    ARGB(0xFFFF0000), ARGB(0xFFFF00AA), ARGB(0xFFFFAA00), ARGB(0xFFFFAAAA),
    ARGB(0xFF550055), ARGB(0xFF5500FF), ARGB(0xFF55AA55), ARGB(0xFF55AAFF),
    ARGB(0xFFFF0055), ARGB(0xFFFF00FF), ARGB(0xFFFFAA55), ARGB(0xFFFFAAFF),
    ARGB(0xFF555500), ARGB(0xFF5555AA), ARGB(0xFF55FF00), ARGB(0xFF55FFAA),
    ARGB(0xFFFF5500), ARGB(0xFFFF55AA), ARGB(0xFFFFFF00), ARGB(0xFFFFFFAA),
    ARGB(0xFF555555), ARGB(0xFF5555FF), ARGB(0xFF55FF55), ARGB(0xFF55FFFF),
    ARGB(0xFFFF5555), ARGB(0xFFFF55FF), ARGB(0xFFFFFF55), ARGB(0xFFFFFFFF),
    )

WEBPALETTE = (
    ARGB(0xFFFFFFFF), ARGB(0xFFFFFFCC), ARGB(0xFFFFFF99), ARGB(0xFFFFFF66),
    ARGB(0xFFFFFF33), ARGB(0xFFFFFF00), ARGB(0xFFFFCCFF), ARGB(0xFFFFCCCC),
    ARGB(0xFFFFCC99), ARGB(0xFFFFCC66), ARGB(0xFFFFCC33), ARGB(0xFFFFCC00),
    ARGB(0xFFFF99FF), ARGB(0xFFFF99CC), ARGB(0xFFFF9999), ARGB(0xFFFF9966),
    ARGB(0xFFFF9933), ARGB(0xFFFF9900), ARGB(0xFFFF66FF), ARGB(0xFFFF66CC),
    ARGB(0xFFFF6699), ARGB(0xFFFF6666), ARGB(0xFFFF6633), ARGB(0xFFFF6600),
    ARGB(0xFFFF33FF), ARGB(0xFFFF33CC), ARGB(0xFFFF3399), ARGB(0xFFFF3366),
    ARGB(0xFFFF3333), ARGB(0xFFFF3300), ARGB(0xFFFF00FF), ARGB(0xFFFF00CC),
    ARGB(0xFFFF0099), ARGB(0xFFFF0066), ARGB(0xFFFF0033), ARGB(0xFFFF0000),
    ARGB(0xFFCCFFFF), ARGB(0xFFCCFFCC), ARGB(0xFFCCFF99), ARGB(0xFFCCFF66),
    ARGB(0xFFCCFF33), ARGB(0xFFCCFF00), ARGB(0xFFCCCCFF), ARGB(0xFFCCCCCC),
    ARGB(0xFFCCCC99), ARGB(0xFFCCCC66), ARGB(0xFFCCCC33), ARGB(0xFFCCCC00),
    ARGB(0xFFCC99FF), ARGB(0xFFCC99CC), ARGB(0xFFCC9999), ARGB(0xFFCC9966),
    ARGB(0xFFCC9933), ARGB(0xFFCC9900), ARGB(0xFFCC66FF), ARGB(0xFFCC66CC),
    ARGB(0xFFCC6699), ARGB(0xFFCC6666), ARGB(0xFFCC6633), ARGB(0xFFCC6600),
    ARGB(0xFFCC33FF), ARGB(0xFFCC33CC), ARGB(0xFFCC3399), ARGB(0xFFCC3366),
    ARGB(0xFFCC3333), ARGB(0xFFCC3300), ARGB(0xFFCC00FF), ARGB(0xFFCC00CC),
    ARGB(0xFFCC0099), ARGB(0xFFCC0066), ARGB(0xFFCC0033), ARGB(0xFFCC0000),
    ARGB(0xFF99FFFF), ARGB(0xFF99FFCC), ARGB(0xFF99FF99), ARGB(0xFF99FF66),
    ARGB(0xFF99FF33), ARGB(0xFF99FF00), ARGB(0xFF99CCFF), ARGB(0xFF99CCCC),
    ARGB(0xFF99CC99), ARGB(0xFF99CC66), ARGB(0xFF99CC33), ARGB(0xFF99CC00),
    ARGB(0xFF9999FF), ARGB(0xFF9999CC), ARGB(0xFF999999), ARGB(0xFF999966),
    ARGB(0xFF999933), ARGB(0xFF999900), ARGB(0xFF9966FF), ARGB(0xFF9966CC),
    ARGB(0xFF996699), ARGB(0xFF996666), ARGB(0xFF996633), ARGB(0xFF996600),
    ARGB(0xFF9933FF), ARGB(0xFF9933CC), ARGB(0xFF993399), ARGB(0xFF993366),
    ARGB(0xFF993333), ARGB(0xFF993300), ARGB(0xFF9900FF), ARGB(0xFF9900CC),
    ARGB(0xFF990099), ARGB(0xFF990066), ARGB(0xFF990033), ARGB(0xFF990000),
    ARGB(0xFF66FFFF), ARGB(0xFF66FFCC), ARGB(0xFF66FF99), ARGB(0xFF66FF66),
    ARGB(0xFF66FF33), ARGB(0xFF66FF00), ARGB(0xFF66CCFF), ARGB(0xFF66CCCC),
    ARGB(0xFF66CC99), ARGB(0xFF66CC66), ARGB(0xFF66CC33), ARGB(0xFF66CC00),
    ARGB(0xFF6699FF), ARGB(0xFF6699CC), ARGB(0xFF669999), ARGB(0xFF669966),
    ARGB(0xFF669933), ARGB(0xFF669900), ARGB(0xFF6666FF), ARGB(0xFF6666CC),
    ARGB(0xFF666699), ARGB(0xFF666666), ARGB(0xFF666633), ARGB(0xFF666600),
    ARGB(0xFF6633FF), ARGB(0xFF6633CC), ARGB(0xFF663399), ARGB(0xFF663366),
    ARGB(0xFF663333), ARGB(0xFF663300), ARGB(0xFF6600FF), ARGB(0xFF6600CC),
    ARGB(0xFF660099), ARGB(0xFF660066), ARGB(0xFF660033), ARGB(0xFF660000),
    ARGB(0xFF33FFFF), ARGB(0xFF33FFCC), ARGB(0xFF33FF99), ARGB(0xFF33FF66),
    ARGB(0xFF33FF33), ARGB(0xFF33FF00), ARGB(0xFF33CCFF), ARGB(0xFF33CCCC),
    ARGB(0xFF33CC99), ARGB(0xFF33CC66), ARGB(0xFF33CC33), ARGB(0xFF33CC00),
    ARGB(0xFF3399FF), ARGB(0xFF3399CC), ARGB(0xFF339999), ARGB(0xFF339966),
    ARGB(0xFF339933), ARGB(0xFF339900), ARGB(0xFF3366FF), ARGB(0xFF3366CC),
    ARGB(0xFF336699), ARGB(0xFF336666), ARGB(0xFF336633), ARGB(0xFF336600),
    ARGB(0xFF3333FF), ARGB(0xFF3333CC), ARGB(0xFF333399), ARGB(0xFF333366),
    ARGB(0xFF333333), ARGB(0xFF333300), ARGB(0xFF3300FF), ARGB(0xFF3300CC),
    ARGB(0xFF330099), ARGB(0xFF330066), ARGB(0xFF330033), ARGB(0xFF330000),
    ARGB(0xFF00FFFF), ARGB(0xFF00FFCC), ARGB(0xFF00FF99), ARGB(0xFF00FF66),
    ARGB(0xFF00FF33), ARGB(0xFF00FF00), ARGB(0xFF00CCFF), ARGB(0xFF00CCCC),
    ARGB(0xFF00CC99), ARGB(0xFF00CC66), ARGB(0xFF00CC33), ARGB(0xFF00CC00),
    ARGB(0xFF0099FF), ARGB(0xFF0099CC), ARGB(0xFF009999), ARGB(0xFF009966),
    ARGB(0xFF009933), ARGB(0xFF009900), ARGB(0xFF0066FF), ARGB(0xFF0066CC),
    ARGB(0xFF006699), ARGB(0xFF006666), ARGB(0xFF006633), ARGB(0xFF006600),
    ARGB(0xFF0033FF), ARGB(0xFF0033CC), ARGB(0xFF003399), ARGB(0xFF003366),
    ARGB(0xFF003333), ARGB(0xFF003300), ARGB(0xFF0000FF), ARGB(0xFF0000CC),
    ARGB(0xFF000099), ARGB(0xFF000066), ARGB(0xFF000033), ARGB(0xFF000000),
    )

RGB3PALETTE = (
    ARGB(0xFF000000), ARGB(0xFF0000FF), ARGB(0xFF00FF00), ARGB(0xFF00FFFF),
    ARGB(0xFFFF0000), ARGB(0xFFFF00FF), ARGB(0xFFFFFF00), ARGB(0xFFFFFFFF),
    )

VGAPALETTE = (
    ARGB(0xFF000000), ARGB(0xFF0000AA), ARGB(0xFF00AA00), ARGB(0xFF00AAAA),
    ARGB(0xFFAA0000), ARGB(0xFFAA00AA), ARGB(0xFFAA5500), ARGB(0xFFAAAAAA),
    ARGB(0xFF555555), ARGB(0xFF5555FF), ARGB(0xFF55FF55), ARGB(0xFF55FFFF),
    ARGB(0xFFFF5555), ARGB(0xFFFF55FF), ARGB(0xFFFFFF55), ARGB(0xFFFFFFFF),
    ARGB(0xFF000000), ARGB(0xFF101010), ARGB(0xFF202020), ARGB(0xFF353535),
    ARGB(0xFF454545), ARGB(0xFF555555), ARGB(0xFF656565), ARGB(0xFF757575),
    ARGB(0xFF8A8A8A), ARGB(0xFF9A9A9A), ARGB(0xFFAAAAAA), ARGB(0xFFBABABA),
    ARGB(0xFFCACACA), ARGB(0xFFDFDFDF), ARGB(0xFFEFEFEF), ARGB(0xFFFFFFFF),
    ARGB(0xFF0000FF), ARGB(0xFF4100FF), ARGB(0xFF8200FF), ARGB(0xFFBE00FF),
    ARGB(0xFFFF00FF), ARGB(0xFFFF00BE), ARGB(0xFFFF0082), ARGB(0xFFFF0041),
    ARGB(0xFFFF0000), ARGB(0xFFFF4100), ARGB(0xFFFF8200), ARGB(0xFFFFBE00),
    ARGB(0xFFFFFF00), ARGB(0xFFBEFF00), ARGB(0xFF82FF00), ARGB(0xFF41FF00),
    ARGB(0xFF00FF00), ARGB(0xFF00FF41), ARGB(0xFF00FF82), ARGB(0xFF00FFBE),
    ARGB(0xFF00FFFF), ARGB(0xFF00BEFF), ARGB(0xFF0082FF), ARGB(0xFF0041FF),
    ARGB(0xFF8282FF), ARGB(0xFF9E82FF), ARGB(0xFFBE82FF), ARGB(0xFFDF82FF),
    ARGB(0xFFFF82FF), ARGB(0xFFFF82DF), ARGB(0xFFFF82BE), ARGB(0xFFFF829E),
    ARGB(0xFFFF8282), ARGB(0xFFFF9E82), ARGB(0xFFFFBE82), ARGB(0xFFFFDF82),
    ARGB(0xFFFFFF82), ARGB(0xFFDFFF82), ARGB(0xFFBEFF82), ARGB(0xFF9EFF82),
    ARGB(0xFF82FF82), ARGB(0xFF82FF9E), ARGB(0xFF82FFBE), ARGB(0xFF82FFDF),
    ARGB(0xFF82FFFF), ARGB(0xFF82DFFF), ARGB(0xFF82BEFF), ARGB(0xFF829EFF),
    ARGB(0xFFBABAFF), ARGB(0xFFCABAFF), ARGB(0xFFDFBAFF), ARGB(0xFFEFBAFF),
    ARGB(0xFFFFBAFF), ARGB(0xFFFFBAEF), ARGB(0xFFFFBADF), ARGB(0xFFFFBACA),
    ARGB(0xFFFFBABA), ARGB(0xFFFFCABA), ARGB(0xFFFFDFBA), ARGB(0xFFFFEFBA),
    ARGB(0xFFFFFFBA), ARGB(0xFFEFFFBA), ARGB(0xFFDFFFBA), ARGB(0xFFCAFFBA),
    ARGB(0xFFBAFFBA), ARGB(0xFFBAFFCA), ARGB(0xFFBAFFDF), ARGB(0xFFBAFFEF),
    ARGB(0xFFBAFFFF), ARGB(0xFFBAEFFF), ARGB(0xFFBADFFF), ARGB(0xFFBACAFF),
    ARGB(0xFF000071), ARGB(0xFF1C0071), ARGB(0xFF390071), ARGB(0xFF550071),
    ARGB(0xFF710071), ARGB(0xFF710055), ARGB(0xFF710039), ARGB(0xFF71001C),
    ARGB(0xFF710000), ARGB(0xFF711C00), ARGB(0xFF713900), ARGB(0xFF715500),
    ARGB(0xFF717100), ARGB(0xFF557100), ARGB(0xFF397100), ARGB(0xFF1C7100),
    ARGB(0xFF007100), ARGB(0xFF00711C), ARGB(0xFF007139), ARGB(0xFF007155),
    ARGB(0xFF007171), ARGB(0xFF005571), ARGB(0xFF003971), ARGB(0xFF001C71),
    ARGB(0xFF393971), ARGB(0xFF453971), ARGB(0xFF553971), ARGB(0xFF613971),
    ARGB(0xFF713971), ARGB(0xFF713961), ARGB(0xFF713955), ARGB(0xFF713945),
    ARGB(0xFF713939), ARGB(0xFF714539), ARGB(0xFF715539), ARGB(0xFF716139),
    ARGB(0xFF717139), ARGB(0xFF617139), ARGB(0xFF557139), ARGB(0xFF457139),
    ARGB(0xFF397139), ARGB(0xFF397145), ARGB(0xFF397155), ARGB(0xFF397161),
    ARGB(0xFF397171), ARGB(0xFF396171), ARGB(0xFF395571), ARGB(0xFF394571),
    ARGB(0xFF515171), ARGB(0xFF595171), ARGB(0xFF615171), ARGB(0xFF695171),
    ARGB(0xFF715171), ARGB(0xFF715169), ARGB(0xFF715161), ARGB(0xFF715159),
    ARGB(0xFF715151), ARGB(0xFF715951), ARGB(0xFF716151), ARGB(0xFF716951),
    ARGB(0xFF717151), ARGB(0xFF697151), ARGB(0xFF617151), ARGB(0xFF597151),
    ARGB(0xFF517151), ARGB(0xFF517159), ARGB(0xFF517161), ARGB(0xFF517169),
    ARGB(0xFF517171), ARGB(0xFF516971), ARGB(0xFF516171), ARGB(0xFF515971),
    ARGB(0xFF000041), ARGB(0xFF100041), ARGB(0xFF200041), ARGB(0xFF310041),
    ARGB(0xFF410041), ARGB(0xFF410031), ARGB(0xFF410020), ARGB(0xFF410010),
    ARGB(0xFF410000), ARGB(0xFF411000), ARGB(0xFF412000), ARGB(0xFF413100),
    ARGB(0xFF414100), ARGB(0xFF314100), ARGB(0xFF204100), ARGB(0xFF104100),
    ARGB(0xFF004100), ARGB(0xFF004110), ARGB(0xFF004120), ARGB(0xFF004131),
    ARGB(0xFF004141), ARGB(0xFF003141), ARGB(0xFF002041), ARGB(0xFF001041),
    ARGB(0xFF202041), ARGB(0xFF282041), ARGB(0xFF312041), ARGB(0xFF392041),
    ARGB(0xFF412041), ARGB(0xFF412039), ARGB(0xFF412031), ARGB(0xFF412028),
    ARGB(0xFF412020), ARGB(0xFF412820), ARGB(0xFF413120), ARGB(0xFF413920),
    ARGB(0xFF414120), ARGB(0xFF394120), ARGB(0xFF314120), ARGB(0xFF284120),
    ARGB(0xFF204120), ARGB(0xFF204128), ARGB(0xFF204131), ARGB(0xFF204139),
    ARGB(0xFF204141), ARGB(0xFF203941), ARGB(0xFF203141), ARGB(0xFF202841),
    ARGB(0xFF2D2D41), ARGB(0xFF312D41), ARGB(0xFF352D41), ARGB(0xFF3D2D41),
    ARGB(0xFF412D41), ARGB(0xFF412D3D), ARGB(0xFF412D35), ARGB(0xFF412D31),
    ARGB(0xFF412D2D), ARGB(0xFF41312D), ARGB(0xFF41352D), ARGB(0xFF413D2D),
    ARGB(0xFF41412D), ARGB(0xFF3D412D), ARGB(0xFF35412D), ARGB(0xFF31412D),
    ARGB(0xFF2D412D), ARGB(0xFF2D4131), ARGB(0xFF2D4135), ARGB(0xFF2D413D),
    ARGB(0xFF2D4141), ARGB(0xFF2D3D41), ARGB(0xFF2D3541), ARGB(0xFF2D3141),
    ARGB(0xFF000000), ARGB(0xFF000000), ARGB(0xFF000000), ARGB(0xFF000000),
    ARGB(0xFF000000), ARGB(0xFF000000), ARGB(0xFF000000), ARGB(0xFF000000),
    )
