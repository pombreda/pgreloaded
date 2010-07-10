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
#define PYGAME_OPENALCONTEXT_INTERNAL

#include "pgbase.h"
#include "openalmod.h"
#include "pgopenal.h"
#include "openalbase_doc.h"

static int _context_init (PyObject *self, PyObject *args, PyObject *kwds);
static void _context_dealloc (PyContext *self);
static PyObject* _context_repr (PyObject *self);

static PyObject* _context_createbuffers (PyObject *self, PyObject *args);
static PyObject* _context_createsources (PyObject *self, PyObject *args);
static PyObject* _context_makecurrent (PyObject *self);
static PyObject* _context_suspend (PyObject *self);
static PyObject* _context_process (PyObject *self);
static PyObject* _context_enable (PyObject *self, PyObject *args);
static PyObject* _context_disable (PyObject *self, PyObject *args);
static PyObject* _context_isenabled (PyObject *self, PyObject *args);
static PyObject* _context_getprop (PyObject *self, PyObject *args);

static PyObject* _context_iscurrent (PyObject* self, void *closure);
static PyObject* _context_getlistener (PyObject* self, void *closure);
static PyObject* _context_getdevice (PyObject* self, void *closure);
static PyObject* _context_getdistancemodel (PyObject* self, void *closure);
static int _context_setdistancemodel (PyObject* self, PyObject *value,
    void *closure);
static PyObject* _context_getdopplerfactor (PyObject* self, void *closure);
static int _context_setdopplerfactor (PyObject* self, PyObject *value,
    void *closure);
static PyObject* _context_getspeedofsound (PyObject* self, void *closure);
static int _context_setspeedofsound (PyObject* self, PyObject *value,
    void *closure);

/**
 */
static PyMethodDef _context_methods[] = {
    { "make_current", (PyCFunction)_context_makecurrent, METH_NOARGS,
      DOC_BASE_CONTEXT_MAKE_CURRENT },
    { "create_buffers", (PyCFunction) _context_createbuffers, METH_O,
      DOC_BASE_CONTEXT_CREATE_BUFFERS },
    { "create_sources", (PyCFunction) _context_createsources, METH_O,
      DOC_BASE_CONTEXT_CREATE_SOURCES },
    { "suspend", (PyCFunction) _context_suspend, METH_NOARGS,
      DOC_BASE_CONTEXT_SUSPEND },
    { "process", (PyCFunction) _context_process, METH_NOARGS,
      DOC_BASE_CONTEXT_PROCESS },
    { "enable", (PyCFunction) _context_enable, METH_O,
      DOC_BASE_CONTEXT_ENABLE },
    { "disable", (PyCFunction) _context_disable, METH_O,
      DOC_BASE_CONTEXT_DISABLE },
    { "is_enabled", (PyCFunction) _context_isenabled, METH_O,
      DOC_BASE_CONTEXT_IS_ENABLED },
    /*{ "get_prop", (PyCFunction) _context_getprop, METH_VARARGS, "" },*/
    { NULL, NULL, 0, NULL }
};

/**
 */
static PyGetSetDef _context_getsets[] = {
    { "is_current", _context_iscurrent, NULL, DOC_BASE_CONTEXT_IS_CURRENT,
      NULL },
    { "device", _context_getdevice, NULL, DOC_BASE_CONTEXT_DEVICE, NULL },
    { "listener", _context_getlistener, NULL, DOC_BASE_CONTEXT_LISTENER, NULL },
    { "distance_model", _context_getdistancemodel, _context_setdistancemodel,
      DOC_BASE_CONTEXT_DISTANCE_MODEL, NULL },
    { "doppler_factor", _context_getdopplerfactor, _context_setdopplerfactor,
      DOC_BASE_CONTEXT_DOPPLER_FACTOR, NULL }, 
    { "speed_of_sound", _context_getspeedofsound, _context_setspeedofsound,
      DOC_BASE_CONTEXT_SPEED_OF_SOUND, NULL },
    { NULL, NULL, NULL, NULL, NULL }
};

/**
 */
PyTypeObject PyContext_Type =
{
    TYPE_HEAD(NULL, 0)
    "base.Context",             /* tp_name */
    sizeof (PyContext),         /* tp_basicsize */
    0,                          /* tp_itemsize */
    (destructor) _context_dealloc, /* tp_dealloc */
    0,                          /* tp_print */
    0,                          /* tp_getattr */
    0,                          /* tp_setattr */
    0,                          /* tp_compare */
    (reprfunc)_context_repr,    /* tp_repr */
    0,                          /* tp_as_number */
    0,                          /* tp_as_sequence */
    0,                          /* tp_as_mapping */
    0,                          /* tp_hash */
    0,                          /* tp_call */
    0,                          /* tp_str */
    0,                          /* tp_getattro */
    0,                          /* tp_setattro */
    0,                          /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /* tp_flags */
    DOC_BASE_CONTEXT,
    0,                          /* tp_traverse */
    0,                          /* tp_clear */
    0,                          /* tp_richcompare */
    0,                          /* tp_weaklistoffset */
    0,                          /* tp_iter */
    0,                          /* tp_iternext */
    _context_methods,           /* tp_methods */
    0,                          /* tp_members */
    _context_getsets,           /* tp_getset */
    0,                          /* tp_base */
    0,                          /* tp_dict */
    0,                          /* tp_descr_get */
    0,                          /* tp_descr_set */
    0,                          /* tp_dictoffset */
    (initproc) _context_init,   /* tp_init */
    0,                          /* tp_alloc */
    0,                          /* tp_new */
    0,                          /* tp_free */
    0,                          /* tp_is_gc */
    0,                          /* tp_bases */
    0,                          /* tp_mro */
    0,                          /* tp_cache */
    0,                          /* tp_subclasses */
    0,                          /* tp_weaklist */
    0,                          /* tp_del */
#if PY_VERSION_HEX >= 0x02060000
    0                           /* tp_version_tag */
#endif
};


static void
_context_dealloc (PyContext *self)
{
    if (self->context)
    {
        ALCcontext *ctxt = alcGetCurrentContext ();
        
        /* Make sure, the context is not current. */
        if (ctxt == self->context)
            alcMakeContextCurrent (NULL);
        alcDestroyContext (self->context);
    }
    Py_XDECREF (self->device);
    Py_XDECREF (self->listener);
    self->listener = NULL;
    self->device = NULL;
    self->context = NULL;
    ((PyObject*)self)->ob_type->tp_free ((PyObject *) self);
}

static int
_context_init (PyObject *self, PyObject *args, PyObject *kwds)
{
    PyObject *device;
    PyObject *attrlist = NULL;
    ALCint *attrs = NULL;
    
    if (!PyArg_ParseTuple (args, "O|O", &device, &attrlist))
        return -1;

    if (!PyDevice_Check (device))
    {
        PyErr_SetString (PyExc_TypeError, "device must be a Device");
        return -1;
    }
    
    if (attrlist)
    {
        ALCint attr;
        if (PySequence_Check (attrlist))
        {
            PyObject *item;
            Py_ssize_t i;
            Py_ssize_t count = PySequence_Size (attrlist);
            if (count == -1)
                return -1;
            if (count > 0)
                attrs = PyMem_New (ALCint, (count * 2) + 1);
            else
                attrs = NULL;
            for (i = 0; i < (count * 2); i += 2)
            {
                item = PySequence_ITEM (attrlist, i);
                if (!item)
                {
                    PyMem_Free (attrs);
                    return -1;
                }

                if (!IntFromSeqIndex (item, (Py_ssize_t)0, (int*)&attr))
                {
                    PyMem_Free (attrs);
                    return -1;
                }
                attrs[i] = attr;
                if (!IntFromSeqIndex (item, (Py_ssize_t)1, (int*)&attr))
                {
                    PyMem_Free (attrs);
                    return -1;
                }
                attrs[i+1] = attr;
            }
            attrs[(count*2)] = 0;
        }
        else
        {
            PyErr_Clear ();
            PyErr_SetString (PyExc_TypeError,
                "attrs must be a sequence of attibute/value pairs");
            return -1;
        }
    }

    CLEAR_ALCERROR_STATE ();
    ((PyContext*)self)->context = alcCreateContext (PyDevice_AsDevice (device),
        attrs);
    if (attrs)
        PyMem_Free (attrs);
    if (((PyContext*)self)->context == NULL)
    {
        SetALCErrorException (alcGetError (PyDevice_AsDevice (device)), 1);
        return -1;
    }
    Py_INCREF (device);
    ((PyContext*)self)->device = device;
    return 0;
}

static PyObject*
_context_repr (PyObject *self)
{
    /* TODO */
    return Text_FromUTF8 ("<Context>");
}

/* Context getters/setters */
static PyObject*
_context_iscurrent (PyObject* self, void *closure)
{
    return PyBool_FromLong (CONTEXT_IS_CURRENT (self));
}

static PyObject*
_context_getdevice (PyObject* self, void *closure)
{
    PyContext *ctxt = (PyContext*)self;
    Py_INCREF (ctxt->device);
    return ctxt->device;
}

static PyObject*
_context_getlistener (PyObject* self, void *closure)
{
    PyContext *ctxt = (PyContext*)self;

    if (!ctxt->listener)
    {
        ctxt->listener = PyListener_New (self);
        if (!ctxt->listener)
            return NULL;
    }
    Py_INCREF (ctxt->listener);
    return ctxt->listener;
}

static PyObject*
_context_getdistancemodel (PyObject* self, void *closure)
{
    ALint model;
    
    ASSERT_CONTEXT_IS_CURRENT (self, NULL);
    CLEAR_ALERROR_STATE ();
    model = alGetInteger (AL_DISTANCE_MODEL);
    if (SetALErrorException (alGetError (), 0))
        return NULL;
    return PyInt_FromLong ((long)model);
}

static int
_context_setdistancemodel (PyObject* self, PyObject *value, void *closure)
{
    int model;
    
    ASSERT_CONTEXT_IS_CURRENT (self, -1);
    
    if (!IntFromObj (value, &model))
        return -1;
    CLEAR_ALERROR_STATE ();
    alDistanceModel ((ALenum)model);
    if (SetALErrorException (alGetError (), 0))
        return -1;
    return 0;
}

static PyObject*
_context_getdopplerfactor (PyObject* self, void *closure)
{
    ALfloat factor;
    
    ASSERT_CONTEXT_IS_CURRENT (self, NULL);
    CLEAR_ALERROR_STATE ();
    factor = alGetFloat (AL_DOPPLER_FACTOR);
    if (SetALErrorException (alGetError (), 0))
        return NULL;
    return PyFloat_FromDouble ((double)factor);
}

static int
_context_setdopplerfactor (PyObject* self, PyObject *value, void *closure)
{
    double factor;
    
    ASSERT_CONTEXT_IS_CURRENT (self, -1);
    
    if (!DoubleFromObj (value, &factor))
        return -1;
    CLEAR_ALERROR_STATE ();
    alDopplerFactor ((ALfloat)factor);
    if (SetALErrorException (alGetError (), 0))
        return -1;
    return 0;
}

static PyObject*
_context_getspeedofsound (PyObject* self, void *closure)
{
    ALfloat speed;
    
    ASSERT_CONTEXT_IS_CURRENT (self, NULL);
    CLEAR_ALERROR_STATE ();
    speed = alGetFloat (AL_SPEED_OF_SOUND);
    if (SetALErrorException (alGetError (), 0))
        return NULL;
    return PyFloat_FromDouble ((double)speed);
}

static int
_context_setspeedofsound (PyObject* self, PyObject *value, void *closure)
{
    double speed;
    
    ASSERT_CONTEXT_IS_CURRENT (self, -1);
    
    if (!DoubleFromObj (value, &speed))
        return -1;
    CLEAR_ALERROR_STATE ();
    alSpeedOfSound ((ALfloat)speed);
    if (SetALErrorException (alGetError (), 0))
        return -1;
    return 0;
}


/* Context methods */
static PyObject*
_context_makecurrent (PyObject *self)
{
    PyContext *ctxt = (PyContext*) self;
    
    CLEAR_ALCERROR_STATE ();
    if (alcMakeContextCurrent (ctxt->context) == AL_TRUE)
        Py_RETURN_TRUE;
    if (SetALCErrorException (alcGetError
        (PyDevice_AsDevice (ctxt->device)), 0))
        return NULL;
    Py_RETURN_FALSE;
}

static PyObject*
_context_createbuffers (PyObject *self, PyObject *args)
{
    unsigned int bufnum;

    ASSERT_CONTEXT_IS_CURRENT(self, NULL);
    if (!UintFromObj (args, &bufnum))
        return NULL;
    return PyBuffers_New (self, (ALsizei) bufnum);
}

static PyObject*
_context_createsources (PyObject *self, PyObject *args)
{
    unsigned int bufnum;

    ASSERT_CONTEXT_IS_CURRENT(self, NULL);
    if (!UintFromObj (args, &bufnum))
        return NULL;
    return PySources_New (self, (ALsizei) bufnum);
}

static PyObject*
_context_suspend (PyObject *self)
{
    PyContext *ctxt = (PyContext*) self;
    
    CLEAR_ALCERROR_STATE ();
    alcSuspendContext (ctxt->context);
    if (SetALCErrorException (alcGetError
        (PyDevice_AsDevice (ctxt->device)), 0))
        return NULL;
    Py_RETURN_NONE;
}

static PyObject*
_context_process (PyObject *self)
{
    PyContext *ctxt = (PyContext*) self;

    CLEAR_ALCERROR_STATE ();
    alcProcessContext (ctxt->context);
    if (SetALCErrorException (alcGetError
        (PyDevice_AsDevice (ctxt->device)), 0))
        return NULL;
    Py_RETURN_NONE;
}

static PyObject*
_context_enable (PyObject *self, PyObject *args)
{
    ALenum val;

    ASSERT_CONTEXT_IS_CURRENT(self, NULL);

    if (!IntFromObj (args, (int*) &val))
        return NULL;
    CLEAR_ALERROR_STATE ();
    alEnable (val);
    if (SetALErrorException (alGetError (), 0))
        return NULL;
    Py_RETURN_NONE;
}

static PyObject*
_context_disable (PyObject *self, PyObject *args)
{
    ALenum val;

    ASSERT_CONTEXT_IS_CURRENT(self, NULL);

    if (!IntFromObj (args, (int*) &val))
        return NULL;
    CLEAR_ALERROR_STATE ();
    alDisable (val);
    if (SetALErrorException (alGetError (), 0))
        return NULL;
    Py_RETURN_NONE;
}

static PyObject*
_context_isenabled (PyObject *self, PyObject *args)
{
    ALenum val;
    ALboolean ret;

    ASSERT_CONTEXT_IS_CURRENT(self, NULL);

    if (!IntFromObj (args, (int*) &val))
        return NULL;
    CLEAR_ALERROR_STATE ();
    ret = alIsEnabled (val);
    if (SetALErrorException (alGetError (), 0))
        return NULL;
    if (ret == AL_TRUE)
        Py_RETURN_TRUE;
    Py_RETURN_FALSE;
}

static PyObject*
_context_getprop (PyObject *self, PyObject *args)
{
    /* TODO */
    Py_RETURN_NONE;
}

void
context_export_capi (void **capi)
{
    capi[PYGAME_OPENALCONTEXT_FIRSTSLOT] = &PyContext_Type;
}
