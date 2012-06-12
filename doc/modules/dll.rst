.. module:: pygame2.dll
   :synopsis: DLL loading

:mod:`pygame2.dll` - DLL loading
================================

The :mod:`pygame2.dll` module is not intended for consumers of
Pygame2. It is a helper module for loading the 3rd party libraries used by
Pygame2.

.. class:: DLL(libname : string)

   Function wrapper around the different DLL functions. Do not use or
   instantiate this one directly from your user code.

   .. method:: add_function(name : string, func : function)

      Adds the passed ``function`` to the DLL instance. The function
      will be identified by the passed ``name``, so that a invocation of
      ``mydll.name (...)`` will invoke the bound function.

   .. method:: get_decorator() -> decorator class instance

      Gets a  decorator binding for the DLL. The decorator can be used
      to bind module level functions to their corresponding DLL
      function. ::

        mydll = DLL("mylibrary", ["libmylib", "mylib"])
        mydecorator = mydll.get_decorator()

        @mydecorator("LibraryFunction", [ctypes.c_int], ctypes.c_int)
        def libary_function(argument=0):
            return mydll.LibraryFunction(argument)

   .. method:: get_dll_function(name : string) -> function

      Tries to retrieve the function identified by name from the bound
      DLL.

   .. method:: has_dll_function(name : string) -> bool

      Checks, if a function identified by ``name`` exists in the bound
      DLL.
