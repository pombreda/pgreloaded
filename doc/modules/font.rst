.. module:: pygame2.font
   :synopsis: Font dectection helpers

:mod:`pygame2.font` - Font detection helpers
============================================

.. data:: STYLE_NORMAL

   Indicates a normal font style.

.. data:: STYLE_BOLD

   Indicates a bold font style.

.. data:: STYLE_ITALIC

   Indicates an italic font style.

.. function:: init() -> None

   Initializes the internal font cache.

.. function:: get_font(name : string[, style=STYLE_NORMAL[, \
                       ftype=None]]) -> string

   Gets a font matching
.. function:: get_fonts(name : string[, style=STYLE_NORMAL[, \
                        ftype=None]]) -> string

.. function:: list_fonts() -> iterator

   Retrieves an iterator over all found fonts. The values of the
   iterator will be tuples, containing the following information:
   *(family, font name, font style, font type, filename)*

   * family: string, denotes the font family
   * font name: string, the name of the font
   * font style: int, a combination of the different ``STYLE_`` values
   * font type: string, the font file type (e.g. TTF, OTF, ...)
   * filename: the name of the physical file


