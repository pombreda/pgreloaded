/*
  pygame - Python Game Library
  Copyright (C) 2010 Marcus von Appen

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
#define PYGAME_OPENALBASE_INTERNAL

#include "pymacros.h"
#include "openalmod.h"
#include "pgbase.h"
#include "pgopenal.h"
#include "openalbase_doc.h"

static PyObject* _openal_init (PyObject *self);
static PyObject* _openal_quit (PyObject *self);
static PyObject* _openal_geterror (PyObject *self);
static PyObject* _openal_algetstring (PyObject *self, PyObject *args);
static PyObject* _openal_getenumvalue (PyObject *self, PyObject *args);
static PyObject* _openal_isextensionpresent (PyObject *self, PyObject *args);
static PyObject* _openal_setcurrentcontext (PyObject *self, PyObject *args);
static PyObject* _openal_listoutputdevices (PyObject *self);
static PyObject* _openal_listcapturedevices (PyObject *self);
static PyObject* _openal_getdefaultoutputdevicename (PyObject *self);
static PyObject* _openal_getdefaultcapturedevicename (PyObject *self);

static PyMethodDef _openal_methods[] = {
    { "init", (PyCFunction)_openal_init, METH_NOARGS, DOC_BASE_INIT },
    { "quit", (PyCFunction)_openal_quit, METH_NOARGS, DOC_BASE_QUIT },
    { "get_error", (PyCFunction)_openal_geterror, METH_NOARGS,
      DOC_BASE_GET_ERROR },
    { "is_extension_present", _openal_isextensionpresent, METH_VARARGS,
      DOC_BASE_IS_EXTENSION_PRESENT },
    { "get_enum_value", _openal_getenumvalue, METH_O,
      DOC_BASE_GET_ENUM_VALUE }, 
    { "list_output_devices", (PyCFunction)_openal_listoutputdevices,
      METH_NOARGS, DOC_BASE_LIST_OUTPUT_DEVICES },
    { "list_capture_devices", (PyCFunction)_openal_listcapturedevices,
      METH_NOARGS, DOC_BASE_LIST_CAPTURE_DEVICES },
    { "al_get_string", (PyCFunction)_openal_algetstring, METH_O,
      DOC_BASE_AL_GET_STRING },
    { "set_current_context", (PyCFunction)_openal_setcurrentcontext,
      METH_O, DOC_BASE_SET_CURRENT_CONTEXT },
    { "get_default_output_device_name",
      (PyCFunction) _openal_getdefaultoutputdevicename, METH_NOARGS,
      DOC_BASE_GET_DEFAULT_OUTPUT_DEVICE_NAME },
    { "get_default_capture_device_name",
      (PyCFunction) _openal_getdefaultcapturedevicename, METH_NOARGS,
      DOC_BASE_GET_DEFAULT_CAPTURE_DEVICE_NAME },
   
    { NULL, NULL, 0, NULL },
};

static PyObject*
_openal_init (PyObject *self)
{
    Py_RETURN_NONE;
}

static PyObject*
_openal_quit (PyObject *self)
{
    Py_RETURN_NONE;
}

static PyObject*
_openal_geterror (PyObject *self)
{
    ALenum error = alGetError ();
    switch (error)
    {
    case AL_INVALID_ENUM:
        return Text_FromUTF8 ("invalid enumeration value");
    case AL_INVALID_VALUE:
        return Text_FromUTF8 ("invalid value");
    case AL_INVALID_OPERATION:
        return Text_FromUTF8 ("invalid operation request");
    case AL_OUT_OF_MEMORY:
        return Text_FromUTF8 ("insufficient memory");
    default:
        Py_RETURN_NONE;
    }
}

static PyObject*
_openal_algetstring (PyObject *self, PyObject *args)
{
    ALenum val;
    const ALchar* retval;
    if (!IntFromObj (args, (int*) &val))
        return NULL;

    if (alcGetCurrentContext () == NULL)
    {
        PyErr_SetString (PyExc_PyGameError, "no context is currently used");
        return NULL;
    }

    CLEAR_ALERROR_STATE ();
    retval = alGetString (val);
    if (!retval)
    {
        SetALErrorException (alGetError (), 1);
        return NULL;
    }
    return Text_FromUTF8 ((const char*)retval);
}

static PyObject*
_openal_getenumvalue (PyObject *self, PyObject *args)
{
    ALenum val;
    PyObject *freeme;
    char *enumname;
    
    if (!ASCIIFromObj (args, &enumname, &freeme))
        return NULL;
    val = alGetEnumValue ((const ALchar*)enumname);
    Py_XDECREF (freeme);
    if (val == 0)
    {
        PyErr_SetString (PyExc_ValueError, "enumeration name does not exist");
        return NULL;
    }
    return PyInt_FromLong ((long)val);
}

static PyObject*
_openal_isextensionpresent (PyObject *self, PyObject *args)
{
    char *extname = NULL;
    PyObject *device = NULL;
    ALCboolean present;
    
    if(!PyArg_ParseTuple (args, "s|O", &extname, &device))
        return NULL;
    if (device && !PyDevice_Check (device))
    {
        PyErr_SetString (PyExc_TypeError, "device must be a Device");
        return NULL;
    }
    
    CLEAR_ALCERROR_STATE ();
    if (device)
        present = alcIsExtensionPresent (PyDevice_AsDevice (device),
            (const ALchar*) extname);
    else
        present = alIsExtensionPresent ((const ALchar*) extname);
    if (SetALCErrorException (alcGetError (PyDevice_AsDevice (device)), 0))
        return NULL;
    if (present == ALC_FALSE)
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}

static PyObject*
_openal_setcurrentcontext (PyObject *self, PyObject *args)
{
    if (PyContext_Check (args))
    {
        PyErr_SetString (PyExc_TypeError, "argument must be a Context");
        return NULL;
    }
    if (alcMakeContextCurrent (PyContext_AsContext (args)) == AL_TRUE)
        Py_RETURN_TRUE;
    Py_RETURN_FALSE;
}

static PyObject*
_openal_listoutputdevices (PyObject *self)
{
    PyObject *list, *item;
    const ALCchar *dptr;
    const ALCchar *devices;

    CLEAR_ALCERROR_STATE ();
    if (alcIsExtensionPresent (NULL, "ALC_ENUMERATION_EXT") == AL_FALSE)
    {
        PyErr_SetString (PyExc_PyGameError, "device listing not supported");
        return NULL;
    }

    if (alcIsExtensionPresent (NULL, "ALC_ENUMERATE_ALL_EXT") == AL_TRUE)
        devices = alcGetString (NULL, ALC_ALL_DEVICES_SPECIFIER);
    else
    {
        CLEAR_ALCERROR_STATE (); /* Ignore errors */
        devices = alcGetString (NULL, ALC_DEVICE_SPECIFIER);
    }
    
    if (!devices)
    {
        SetALCErrorException (alcGetError (NULL), 1);
        return NULL;
    }

    list = PyList_New (0);
    if (!list)
        return NULL;
    dptr = devices;
    /* According to the docs, devices will be a list of strings, seperated
     * by NULL, with two consequtive NULL bytes to mark the end */
    while (devices && *dptr)
    {
        item = Text_FromUTF8 ((const char*) dptr);
        if (!item)
        {
            Py_DECREF (list);
            return NULL;
        }
        if (PyList_Append (list, item) == -1)
        {
            Py_DECREF (item);
            Py_DECREF (list);
            return NULL;
        }
        Py_DECREF (item);
        dptr += strlen (dptr) + 1;
    }
    return list;
}

static PyObject*
_openal_listcapturedevices (PyObject *self)
{
    PyObject *list, *item;
    const ALCchar *dptr;
    const ALCchar *devices;

    CLEAR_ALCERROR_STATE ();
    if (alcIsExtensionPresent (NULL, "ALC_ENUMERATION_EXT") == AL_FALSE)
    {
        PyErr_SetString (PyExc_PyGameError, "device listing not supported");
        return NULL;
    }

    devices = alcGetString (NULL, ALC_CAPTURE_DEVICE_SPECIFIER);
    if (!devices)
    {
        SetALCErrorException (alcGetError (NULL), 1);
        return NULL;
    }
    list = PyList_New (0);
    if (!list)
        return NULL;
    dptr = devices;
    /* According to the docs, devices will be a list of strings, seperated
     * by NULL, with two consequtive NULL bytes to mark the end */
    while (devices && *dptr)
    {
        item = Text_FromUTF8 ((const char*) dptr);
        if (!item)
        {
            Py_DECREF (list);
            return NULL;
        }
        if (PyList_Append (list, item) == -1)
        {
            Py_DECREF (item);
            Py_DECREF (list);
            return NULL;
        }
        Py_DECREF (item);
        dptr += strlen (dptr) + 1;
    }
    return list;
}

static PyObject*
_openal_getdefaultoutputdevicename (PyObject *self)
{
    const ALCchar *name;
    CLEAR_ALCERROR_STATE ();
    name = alcGetString (NULL, ALC_DEFAULT_DEVICE_SPECIFIER);
    if (name)
        return Text_FromUTF8 ((const char*)name);
    SetALCErrorException (alcGetError (NULL), 1);
    return NULL;
}

static PyObject*
_openal_getdefaultcapturedevicename (PyObject *self)
{
    const ALCchar *name;
    CLEAR_ALCERROR_STATE ();
    name = alcGetString (NULL, ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER);
    if (name)
        return Text_FromUTF8 ((const char*)name);
    SetALCErrorException (alcGetError (NULL), 1);
    return NULL;
}

/* C API */
int
SetALErrorException (ALenum error, int force)
{
    switch (error)
    {
    case AL_INVALID_ENUM:
        PyErr_SetString (PyExc_PyGameError, "invalid enumeration value");
        return 1;
    case AL_INVALID_VALUE:
        PyErr_SetString (PyExc_PyGameError, "invalid value");
        return 1;
    case AL_INVALID_OPERATION:
        PyErr_SetString (PyExc_PyGameError, "invalid operation request");
        return 1;
    case AL_OUT_OF_MEMORY:
        PyErr_SetString (PyExc_PyGameError, "insufficient memory");
        return 1;
    default:
    {
        if (force)
        {
            PyErr_SetString (PyExc_PyGameError,
                "an unknown error occured for OpenAL");
        }
        return 0;
    }
    }
}

int
SetALCErrorException (ALCenum error, int force)
{
    switch (error)
    {
    case ALC_INVALID_ENUM:
        PyErr_SetString (PyExc_PyGameError, "invalid enumeration value");
        return 1;
    case ALC_INVALID_VALUE:
        PyErr_SetString (PyExc_PyGameError, "invalid value");
        return 1;
    case ALC_OUT_OF_MEMORY:
        PyErr_SetString (PyExc_PyGameError, "insufficient memory");
        return 1;
    case ALC_INVALID_DEVICE:
        PyErr_SetString (PyExc_PyGameError, "invalid device");
        return 1;
    case ALC_INVALID_CONTEXT:
        PyErr_SetString (PyExc_PyGameError, "invalid context");
        return 1;
    default:
    {
        if (force)
        {
            PyErr_SetString (PyExc_PyGameError,
                "an unknown error occured for an OpenAL context");
        }
        return 0;
    }
    }
}

PropType
GetPropTypeFromStr (char *name)
{
    size_t len;
    if (!name)
        return INVALID;

    len = strlen (name);
    if (len > 2)
        return INVALID;

    switch (name[0])
    {
    case 'b':
    {
        if (len == 2)
        {
            if (name[1] == 'a')
                return BOOLARRAY;
            return INVALID;
        }
        return BOOL;
    }
    case 'd':
    {
        if (len == 2)
        {
            if (name[1] == 'a')
                return DOUBLEARRAY;
            return INVALID;
        }
        return DOUBLE;
    }
    case 'f':
    {
        if (len == 2)
        {
            if (name[1] == '3')
                return FLOAT3;
            if (name[1] == 'a')
                return FLOATARRAY;
            return INVALID;
        }
        return FLOAT;
    }
    case 'i':
    {
        if (len == 2)
        {
            if (name[1] == '3')
                return INT3;
            if (name[1] == 'a')
                return INTARRAY;
            return INVALID;
        }
        return INT;
    }
    default:
        return INVALID;
    }

    return INVALID;
}


#ifdef IS_PYTHON_3
PyMODINIT_FUNC PyInit_base (void)
#else
PyMODINIT_FUNC initbase (void)
#endif
{
    PyObject *mod;
    PyObject *c_api_obj;
    static void *c_api[PYGAME_OPENAL_SLOTS];

#ifdef IS_PYTHON_3
    static struct PyModuleDef _module = {
        PyModuleDef_HEAD_INIT,
        "base",
        ""/*DOC_BASE*/,
        -1,
        _openal_methods,
        NULL, NULL, NULL, NULL
    };
    mod = PyModule_Create (&_module);
#else
    mod = Py_InitModule3 ("base", _openal_methods, DOC_BASE);
#endif
    if (!mod)
        goto fail;
        
    if (import_pygame2_base () < 0)
        goto fail;
    
    PyDevice_Type.tp_new = PyType_GenericNew;
    if (PyType_Ready (&PyDevice_Type) < 0)
        goto fail;
    PyCaptureDevice_Type.tp_base = &PyDevice_Type;
    if (PyType_Ready (&PyCaptureDevice_Type) < 0)
        goto fail;
    PyContext_Type.tp_new = PyType_GenericNew;
    if (PyType_Ready (&PyContext_Type) < 0)
        goto fail;
    PyBuffers_Type.tp_new = PyType_GenericNew;
    if (PyType_Ready (&PyBuffers_Type) < 0)
        goto fail;
    PySources_Type.tp_new = PyType_GenericNew;
    if (PyType_Ready (&PySources_Type) < 0)
        goto fail;
    PyListener_Type.tp_new = PyType_GenericNew;
    if (PyType_Ready (&PyListener_Type) < 0)
        goto fail;
    
    ADD_OBJ_OR_FAIL (mod, "Device", PyDevice_Type, fail);
    ADD_OBJ_OR_FAIL (mod, "CaptureDevice", PyCaptureDevice_Type, fail);
    ADD_OBJ_OR_FAIL (mod, "Context", PyContext_Type, fail);
    ADD_OBJ_OR_FAIL (mod, "Buffers", PyBuffers_Type, fail);
    ADD_OBJ_OR_FAIL (mod, "Sources", PySources_Type, fail);
    ADD_OBJ_OR_FAIL (mod, "Listener", PyListener_Type, fail);

    device_export_capi (c_api);
    capturedevice_export_capi (c_api);
    context_export_capi (c_api);
    buffers_export_capi (c_api);
    sources_export_capi (c_api);
    listener_export_capi (c_api);

    c_api_obj = PyCObject_FromVoidPtr ((void *) c_api, NULL);
    if (c_api_obj)
    {
        if (PyModule_AddObject (mod, PYGAME_OPENAL_ENTRY, c_api_obj) == -1)
        {
            Py_DECREF (c_api_obj);
            goto fail;
        }
    }

    MODINIT_RETURN(mod);
fail:
    Py_XDECREF (mod);
    MODINIT_RETURN (NULL);
}
