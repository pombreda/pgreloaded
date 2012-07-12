.. module:: pygame2.ogg.vorbisfile
   :synopsis: Vorbisfile library wrapper

:mod:`pygame2.ogg.vorbisfile` - Vorbisfile library wrapper
==========================================================

Vorbisfile API
--------------

.. class:: OggVorbis_File()

   Represents an Ogg Vorbis audio file.

   This wraps :c:func:`OggVorbis_File`.

.. class:: vorbis_file()

   TODO
   
   This wraps :c:func:`vorbis_info`.
   
.. function:: get_dll_file() -> str

   Gets the name of the loaded vorbisfile dll file.
   
.. function:: clear(ovfilep : OggVorbis_File) -> None

   TODO

   This wraps :c:func:`ov_clear`.

.. function:: fopen(fname : string) -> OggVorbis_File

   TODO

   This wraps :c:func:`ov_fopen`.

.. function:: info(ovfilep : OggVorbis_File[, bstream=-1]) -> vorbis_info

   TODO

   This wraps :c:func:`ov_info`.

.. function:: pcm_total(ovfilep : OggVorbis_File[, bstream=-1]) -> int

   TODO

   This wraps :c:func:`ov_pcm_total`.

.. function:: read(ovfilep : OggVorbis_File, length : int[, outbuf=None, \
                   [bigendian=False[, word=2[, signed=True]]]]) -> (bytes, int, int)

   TODO

   This wraps :c:func:`ov_read`.
