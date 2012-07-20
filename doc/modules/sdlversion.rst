.. module:: pygame2.sdl.version
   :synopsis: SDL2 version wrapper

:mod:`pygame2.sdl.version` - SDL2 version wrapper
=================================================

.. class:: SDL_version(major=0, minor=0, patch=0)

   A SDL_version instance containing the SDL library version.

   .. attribute:: major

      The major version of the SDL library.

   .. attribute:: minor

      The minor version of the SDL library.


   .. attribute:: patch

      The patchlevel of the SDL library.

.. function:: SDL_VERSIONNUM(major : int, minor : int, patch : int) -> int

   alculates the passed version number as integer in the form
   ``major * 1000 + minor * 100 + patch``.

   This wraps `SDL_VERSIONNUM`.

.. function:: SDL_VERSION_ATLEAST(major : int, minor : int, patch : int) -> bool

   Checks, if the used SDL library has at least the passed version.

   This wraps `SDL_VERSION_ATLEAST`.

.. function:: get_version() -> SDL_version

   Returns a :class:`SDL_version` object containing the version of the used SDL
   library.

   This wraps `SDL_GetVersion`.

.. function:: get_revision() -> string

   Returns the unique revision of the used SDL library.

   This wraps `SDL_GetRevision`.

.. function:: get_revision_number() -> int

   Returns the revision number of the used SDL library.

   This wraps `SDL_GetRevisionNumber`.
