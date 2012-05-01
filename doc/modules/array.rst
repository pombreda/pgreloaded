.. module:: pygame2.array
   :synopsis: Conversion routines for sequences.

:mod:`pygame2.array` - Converting sequences
===========================================

Various pygame2 modules extensively use :mod:`ctypes` to access 3rd
party libraries.

TODO

Providing read-write access for sequential data
-----------------------------------------------

.. class:: CTypesView(obj : iterable[, itemsize=1[, docopy=False]])

   A proxy class for byte-wise accessible data types to be used in
   ctypes bindings. The CTypesView provides a read-write access to
   arbitrary objects that are iterable.

   In case the object does not provide a :func:`buffer()` interface for
   direct access, the CTypesView can copy the object's contents into an
   internal buffer, from which data can be retrieved, once the necessary
   operations have been performed.

   Depending on the item type stored in the iterable object, you might
   need to provide a certain ``itemsize``, which denotes the size per
   item in bytes.

   .. attribute:: bytesize

      Returns the length of the encapsuled object in bytes.

   .. attribute:: is_shared

      Indicates, if changes on the CTypesView data effect the encapsuled
      object directly. if not, this means that the object was copied
      internally and needs to be updated by the user code outside of the
      CtypesView.

   .. attribute:: object

      The encapsuled object.

   .. attribute:: view

      Provides a read-write aware view of the encapsuled object data
      that is suitable for usage from :mod:`ctypes`.

   .. method:: to_bytes() -> ctypes.POINTER

      Returns a byte representation of the encapsuled object. The return
      value allows a direct read-write access to the object data, if it
      is not copied. The :func:`ctypes.POINTER` points to an array of
      :class:`ctypes.c_ubyte`.

   .. method:: to_uint16() -> ctypes.POINTER

      Returns a 16-bit representation of the encapsuled object. The return
      value allows a direct read-write access to the object data, if it
      is not copied. The :func:`ctypes.POINTER` points to an array of
      :class:`ctypes.c_ushort`.

   .. method:: to_uint32() -> ctypes.POINTER

      Returns a 32-bit representation of the encapsuled object. The return
      value allows a direct read-write access to the object data, if it
      is not copied. The :func:`ctypes.POINTER` points to an array of
      :class:`ctypes.c_uint`.

   .. method:: to_uint64() -> ctypes.POINTER

      Returns a 64-bit representation of the encapsuled object. The return
      value allows a direct read-write access to the object data, if it
      is not copied. The :func:`ctypes.POINTER` points to an array of
      :class:`ctypes.c_ulonglong`.

.. class:: MemoryView(source : object, itemsize : int, strides : tuple[,
                      getfunc=None[, setfunc=None[, srcsize=None]]])

   The :class:`MemoryView` provides a read-write access to arbitrary
   data objects, which can be indexed.

   ``itemsize`` denotes the size of a single item. ``strides`` defines
   the dimensions and the length (n items * ``itemsize``) for each
   dimension. ``getfunc`` and ``setfunc`` are optional parameters to
   provide specialised read and write access to the underlying
   ``source``. ``srcsize`` can be used to provide the correct source
   size, if ``len(source)`` does not return the absolute size of the
   source object in all dimensions.

   .. note::

      The MemoryView is a pure Python-based implementation and makes
      heavy use of recursion for multi-dimensional access. If you aim
      for speed on accessing a n-dimensional object, you want to
      consider using a specialised library such as numpy. If you need
      n-dimensional access support, where such a library is not
      supported, or if you need to provide access to objects, which do
      not fulfill the requirements of that particular libray,
      :class:`MemoryView` can act as solid fallback solution.

   .. attribute:: itemsize

      The size of a single item in bytes.

   .. attribute:: ndim

      The number of dimensions of the :class:`MemoryView`.

   .. attribute:: size

      The size in bytes of the underlying source object.

   .. attribute:: source

      The underlying data source.

   .. attribute:: strides

      A tuple defining the length in bytes for accessing all
      elements in each dimension of the :class:`MemoryView`.

.. function:: to_bytes(dataseq : iterable, dtype) -> data, int

   Converts an arbitrary sequence to a ctypes array of the specified
   type and returns the ctypes array and amount of items as two-value
   tuple.

   Raises a :exc:`TypeError`, if one or more elements in the passed
   sequence do not match the passed type.
