.. module:: pygame2.resources
   :synopsis: Resource management.

:mod:`pygame2.resources` - Resource management
==============================================

.. class:: Resources([path=None[, excludepattern=None]])

   The Resources class manages a set of file resources and eases
   accessing them by using relative paths, scanning archives
   automatically and so on.

   .. todo::

      Improve the class documentation

   .. method:: add(filename : string)
   
      Adds a file to the resource container. Depending on the
      file type (determined by the file suffix or name) the file will be
      automatically scanned (if it is an archive) or checked for
      availability (if it is a stream or network resource).

   .. method:: add_archive(filename : string[, typehint="zip"])

      Adds an archive file to the resource container. This will scan the
      passed archive and add its contents to the list of available and
      accessible resources.

   .. method:: add_file(filename : string)

      Adds a file to the resource container. This will only add the
      passed file and do not scan an archive or check the file for
      availability.

   .. method:: get(filename : string) -> StringIO

      Gets a specific file from the resource container.

      Raises a :exc:`KeyError`, if the ``filename`` could not be found.

   .. method:: get_filelike(filename : string) -> file object

      Similar to :meth:`get()`, but tries to return the original file
      handle, if possible. If the found file is only available within an
      archive, a :class:`StringIO` instance will be returned.

      Raises a :exc:`KeyError`, if the ``filename`` could not be found.

   .. method:: get_path(filename : string) -> string

      Gets the path of the passed ``filename``. If ``filename`` is only
      available within an archive, a string in the form
      ``filename@archivename`` will be returned.

      Raises a :exc:`KeyError`, if the ``filename`` could not be found.

   .. method:: scan(path : string[, excludepattern=None])

      Scans a path and adds all found files to the resource
      container. If a file within the path is a supported archive (ZIP
      or TAR), its contents will be indexed aut added automatically.

      ``excludepattern`` can be a regular expression to skip directories,
      which match the pattern.

.. function:: open_tarfile(archive : string, filename : string \
                           [, directory=None[, ftype=None]]) -> StringIO

   Opens and reads a certain file from a TAR archive. The result is
   returned as :class:`StringIO` stream. ``filename`` can be a relative
   or absolute path within the TAR archive. The optional ``directory``
   argument can be used to supply a relative directory path, under which
   ``filename`` will be searched.

   ``ftype`` is used to supply additional compression information, in
   case the system cannot determine the compression type itself, and can
   be either **"gz"** for gzip compression or **"bz2"** for bzip2
   compression.

   If the filename could not be found or an error occured on reading it,
   ``None`` will be returned.

   Raises a :exc:`TypeError`, if ``archive`` is not a valid TAR archive or
   if ``ftype`` is not a valid value of ("gz", "bz2").

   .. note::
   
      If ``ftype`` is supplied, the compression mode will be enforced for
      opening and reading.

.. function:: open_url(filename : string[, basepath=None]) -> file object

    Opens and reads a certain file from a web or remote location. This
    function utilizes the :mod:`urllib2` module for Python 2.7 and
    :mod:`urllib` for Python 3.x, which means that it is restricted to
    the types of remote locations supported by the module.

    ``basepath`` can be used to supply an additional location prefix.

.. function:: open_zipfile(archive : string, filename : string \
                           [, directory : string]) -> StringIO

   Opens and reads a certain file from a ZIP archive. The result is
   returned as :class:`StringIO` stream. ``filename`` can be a relative
   or absolute path within the ZIP archive. The optional ``directory``
   argument can be used to supply a relative directory path, under which
   ``filename`` will be searched.

   If the filename could not be found, a :exc:`KeyError` will be raised.
   Raises a :exc:`TypeError`, if ``archive`` is not a valid ZIP archive.
