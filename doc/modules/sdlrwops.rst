.. module:: pygame2.sdl.rwops
   :synopsis: SDL2 RWops wrapper

:mod:`pygame2.sdl.rwops` - SDL2 RWops wrapper
=============================================

.. data:: RW_SEEK_SET

   Indicates a search relative to the start position of the SDL_RWops

.. data:: RW_SEEK_CUR

   Indicates a search relative to the current position within the SDL_RWops
   
.. data:: RW_SEEK_END

   Indicates a search relative to the end position of the SDL_RWops

.. class:: SDL_RWops()

   An arbitrary object capable of byte-wise read and write access.

   This wraps `SDL_RWops`.
   
.. function:: rw_from_file(filename : str, mode : str) -> SDL_RWops   
   
   Creates a new :class:`SDL_RWops` from a file. *mode* specifies the access
   mode for the file and as such is similar to what you can pass to
   :func:`open()`.

.. function:: rw_from_fp(fp : object, autoclose : bool) -> SDL_RWops

   Creates a new :class:`SDL_RWops` from a file handle (``FILE*``). *autoclose*
   indicates, if the file handle should be closed automatically.

.. function:: rw_from_mem(mem : object, size : int) -> SDL_RWops

   Creates a new :class:`SDL_RWops` from a contiguous memory region. *size*
   denotes the size of the memory region in bytes.

.. function:: rw_from_const_mem(mem : object, size : int) -> SDL_RWops

   Creates a new :class:`SDL_RWops` from a contiguous memory region. *size*
   denotes the size of the memory region in bytes.

.. function:: rw_from_object(obj : object) -> SDL_RWops

   Creats a SDL_RWops from any Python object. The Python object must at least
   support the following methods:

   read(length) -> data
   
     length is the size in bytes to be read. A call to len(data) must
     return the correct amount of bytes for the data, so that
     len(data) / [size in bytes for a single element from data] returns
     the amount of elements. Must raise an error on failure.

   seek(offset, whence) -> int
   
     offset denotes the offset to move the read/write pointer of the
     object to. whence indicates the movement behaviour and can be one
     of the following values:
                
     * RW_SEEK_SET - move to offset from the start of the file
     * RW_SEEK_CUR - move by offset from the relative location
     * RW_SEEK_END - move to offset from the end of the file
     
     If it could not move read/write pointer to the desired location,
     an error must be raised.

   tell() -> int
   
     Must return the current offset. This method must only be
     provided, if seek() does not return any value.

   close() -> None
   
     Closes the object(or its internal data access methods). Must raise
     an error on failure.

   write(data) -> None
   
     Writes the passed data(which is a string of bytes) to the object.
     Must raise an error on failure.

     .. note::

        The write() method is optional and only necessary, if the passed
        object should be able to write data.

   The returned :class:`SDL_RWops` is a pure Python object and **must not** be
   freed via :func:`free_rw()`.

.. function:: rw_seek(ctx : SDL_RWops, offset : int, whence : int) -> int

   Moves the read/write offset marker of the :class:`SDL_RWops` to the passed
   *offset*. *whence* indicates the direction for moving and can be one
   of the ``RW_SEEK_*`` constants.

.. function:: rw_tell(ctx : SDL_RWops) -> int

   Returns the current position of the offset marker for the
   :class:`SDL_RWops`.

.. function:: rw_read(ctx : SDL_RWops, ptr : object, size : int, n : int) -> int

   Reads up to ``n * size`` bytes from the passed :class:`SDL_RWops` and stores
   them in *ptr*. *size* denotes the size in bytes of a single chunk and *n*
   the amount of chunks to read.

.. function:: rw_write(ctx : SDL_RWops, ptr : object, size : int, n : int) -> int

   Writes up to ``n * size`` bytes to the passed :class:`SDL_RWops`. The data
   to write is to be provided by *ptr*. *size* denotes the size in bytes of a
   single chunk and *n* the amount of chunks to write.

.. function:: rw_close(ctx : SDL_RWops) -> int

   Closes the passed :class:`SDL_RWops`.

.. function:: alloc_rw() -> SDL_RWops

   Allocates an empty :class:`SDL_RWops` instance. This function is mainly for
   use with unmanaged code, which should gain full access to the SDL features.
   It should not be used within Python.

   The return value must be freed using :func:`free_rw()`.

.. function:: free_rw(rwops : SDL_RWops) -> None

   Frees a SDL_RWops, which was allocated by :func:`alloc_rw()`.
   
.. function:: read_le_16(rwops : SDL_RWops) -> int

   Reads a single 16-bit value from the underlying :class:`SDL_RWops` in
   little-endian byte order.

.. function:: read_be_16(rwops : SDL_RWops) -> int

   Reads a single 16-bit value from the underlying :class:`SDL_RWops` in
   big-endian byte order.

.. function:: read_le_32(rwops : SDL_RWops) -> int

   Reads a single 32-bit value from the underlying :class:`SDL_RWops` in
   little-endian byte order.

.. function:: read_be_32(rwops : SDL_RWops) -> int

   Reads a single 32-bit value from the underlying :class:`SDL_RWops` in
   big-endian byte order.

.. function:: read_le_64(rwops : SDL_RWops) -> int

   Reads a single 64-bit value from the underlying :class:`SDL_RWops` in
   little-endian byte order.

.. function:: read_be_64(rwops : SDL_RWops) -> int

   Reads a single 64-bit value from the underlying :class:`SDL_RWops` in
   big-endian byte order.

.. function:: write_le_16(rwops : SDL_RWops, value : int) -> int

   Writes a single 16-bit to the underlying :class:`SDL_RWops` in
   little-endian byte order.

.. function:: write_be_16(rwops : SDL_RWops, value : int) -> int

   Writes a single 16-bit to the underlying :class:`SDL_RWops` in
   big-endian byte order.

.. function:: write_le_32(rwops : SDL_RWops, value : int) -> int

   Writes a single 32-bit to the underlying :class:`SDL_RWops` in
   little-endian byte order.

.. function:: write_be_32(rwops : SDL_RWops, value : int) -> int

   Writes a single 32-bit to the underlying :class:`SDL_RWops` in
   big-endian byte order.

.. function:: write_le_64(rwops : SDL_RWops, value : int) -> int

   Writes a single 64-bit to the underlying :class:`SDL_RWops` in
   little-endian byte order.

.. function:: write_be_64(rwops : SDL_RWops, value : int) -> int

   Writes a single 64-bit to the underlying :class:`SDL_RWops` in
   big-endian byte order.
