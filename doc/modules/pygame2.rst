.. module:: pygame2
   :synopsis: Core information for all modules.

:mod:`pygame2` - Core configuration
===================================

This module contains the version information and lets you define the
path, from which DLLs should be loaded.

Version information
-------------------

.. data:: __version__

   The version of the pygame2 package as string.

.. data:: version_info

   The version of the pygame2 package as value tuple. The tuple is of
   the form ``('major', 'minor', 'micro', 'releaselevel')``, where all
   values except the *releaselevel* are integers.

Setting the DLL path
--------------------

Various :mod:`pygame2` modules, such as TODO utilise :mod:`ctypes` to
interact with specific 3rd party libraries. Since system configurations
and distribution policies can vary, it might be necessary to provide an
explicit location, from which the DLLs to be used should be loaded.

.. note::
   If a DLL could not be found in the set DLL path, pygame2 will
   use :func:`ctypes.util.find_library` to find the required library.

.. function:: get_dll_path() -> str

   Returns the path to the DLLs to be used. The path does not include
   any DLL but points to the location at which the DLLs are expected to
   be found for *all* modules.

   .. note::
      On Win32 platforms, a set of prebuilt DLLs for 32-bit and 64-bit
      systems will be installed by default. The DLLs are mostly standard
      builds of the open-source libraries, which are used by pygame2 and
      not optimised in any way.
      
      On Win32 platforms the DLL path is automatically set to the
      **dll** folder of pygame2, so that the DLLs within that folder are
      used ina first place. If you want to ship your own DLLs or rely on
      the system environment, either

      * reset the DLL path by passing **None** to :func:`set_dll_path()`
        *before* loading any other package or module *or*
      * remove the DLLs from the **dll** folder before distributing your
        application
      
.. function:: set_dll_path(path) -> None

   Sets the path to the DLLs to be used.
