/*
  pygame - Python Game Library
  Copyright (C) 2008 Marcus von Appen

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Library General Public
  License as published by the Free Software Foundation; either
  version 2 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Library General Public License for more details.

  You should have received a copy of the GNU Library General Public
  License along with this library; if not, write to the Free
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

*/
#ifndef _PYGAME_SDLGFX_H_
#define _PYGAME_SDLGFX_H_

#include <SDL.h>
#include <SDL_framerate.h>

#include "pgbase.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct
{
    PyObject_HEAD
    FPSmanager *fps;
} PyFPSmanager;
#define PyFPSmanager_AsFPSmanager(x) (((PyFPSmanager*)x)->fps)
#define PYGAME_SDLGFXFPS_FIRSTSLOT 0
#define PYGAME_SDLGFXFPS_NUMSLOTS 2
#ifndef PYGAME_SDLGFXFPS_INTERNAL
#define PyFPSmanager_Type \
    (*(PyTypeObject*)PyGameSDLGFX_C_API[PYGAME_SDLGFXFPS_FIRSTSLOT+0])
#define PyFPSmanager_Check(x)                                          \
    (PyObject_TypeCheck(x,                                              \
        (PyTypeObject*)PyGameSDLGFX_C_API[PYGAME_SDLGFXFPS_FIRSTSLOT+0]))
#define PyFPSmanager_New                                               \
    (*(PyObject*(*)(void))PyGameSDLGFX_C_API[PYGAME_SDLGFXFPS_FIRSTSLOT+1])
#endif /* PYGAME_SDLGFXFPS_INTERNAL */

/**
 * C API export.
 */
#ifdef PYGAME_INTERNAL
void **PyGameSDLGFX_C_API;
#else
static void **PyGameSDLGFX_C_API;
#endif

#define PYGAME_SDLGFX_SLOTS                                    \
    (PYGAME_SDLGFXFPS_FIRSTSLOT + PYGAME_SDLGFXFPS_NUMSLOTS)
#define PYGAME_SDLGFX_ENTRY "_PYGAME_SDLGFX_CAPI"
#define PYGAME_CSDLGFX_ENTRY "pygame2.sdlgfx.base._PYGAME_SDLGFX_CAPI"

static int
import_pygame2_sdlgfx_base (void)
{
#if PY_VERSION_HEX >= 0x03010000
    PyObject *_module = PyImport_ImportModule ("pygame2.sdlgfx.base");
    if (_module == NULL)
        return -1;
    PyGameSDLGFX_C_API = (void**) PyCapsule_Import(PYGAME_CSDLGFX_ENTRY, 0);
    return (PyGameSDLGFX_C_API != NULL) ? 0 : -1;
#else
    PyObject *_module = PyImport_ImportModule ("pygame2.sdlgfx.base");
    if (_module != NULL)
    {
        PyObject *_capi = PyObject_GetAttrString(_module, PYGAME_SDLGFX_ENTRY);
        if (!PyCObject_Check (_capi))
        {
            Py_DECREF (_module);
            return -1;
        }
        PyGameSDLGFX_C_API = (void**) PyCObject_AsVoidPtr (_capi);
        Py_DECREF (_capi);
        return 0;
    }
    return -1;
#endif
}

#ifdef __cplusplus
}
#endif

#endif /* _PYGAME_SDLGFX_H_ */
