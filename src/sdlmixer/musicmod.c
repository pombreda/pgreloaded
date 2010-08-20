/*
  pygame - Python Game Library
  Copyright (C) 2000-2001 Pete Shinners, 2008 Marcus von Appen

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
#define PYGAME_SDLMIXER_INTERNAL

#include "pgmixer.h"
#include "pgsdl.h"
#include "sdlmixermusic_doc.h"

static PyObject* _music_setvolume (PyObject *self, PyObject *args);
static PyObject* _music_getvolume (PyObject *self);
static PyObject* _music_pause (PyObject *self);
static PyObject* _music_resume (PyObject *self);
static PyObject* _music_halt (PyObject *self);
static PyObject* _music_rewind (PyObject *self);
static PyObject* _music_fadeout (PyObject *self, PyObject *args);
static PyObject* _music_playing (PyObject *self);
static PyObject* _music_paused (PyObject *self);
static PyObject* _music_fading (PyObject *self);
static PyObject* _music_setposition (PyObject *self, PyObject *args);
static PyObject* _music_getdecoders (PyObject *self);

static PyMethodDef _music_methods[] = {
    { "set_volume", _music_setvolume, METH_O, DOC_MUSIC_SET_VOLUME },
    { "get_volume", (PyCFunction) _music_getvolume, METH_NOARGS,
      DOC_MUSIC_GET_VOLUME },
    { "pause", (PyCFunction) _music_pause, METH_NOARGS, DOC_MUSIC_PAUSE },
    { "resume", (PyCFunction) _music_resume, METH_NOARGS, DOC_MUSIC_RESUME },
    { "halt", (PyCFunction) _music_halt, METH_NOARGS, DOC_MUSIC_HALT },
    { "rewind", (PyCFunction) _music_rewind, METH_NOARGS, DOC_MUSIC_REWIND},
    { "fade_out", _music_fadeout, METH_O, DOC_MUSIC_FADE_OUT },
    { "playing", (PyCFunction) _music_playing, METH_NOARGS, DOC_MUSIC_PLAYING },
    { "paused", (PyCFunction) _music_paused, METH_NOARGS, DOC_MUSIC_PAUSED },
    { "fading", (PyCFunction) _music_fading, METH_NOARGS, DOC_MUSIC_FADING },
    { "set_position", _music_setposition, METH_O, DOC_MUSIC_SET_POSITION },
    { "get_decoders", (PyCFunction)_music_getdecoders, METH_NOARGS,
      DOC_MUSIC_GET_DECODERS },
    { NULL, NULL, 0, NULL },
};

static PyObject*
_music_setvolume (PyObject *self, PyObject *args)
{
    int volume, result;
    
    ASSERT_MIXER_OPEN (NULL);
    
    if (!IntFromObj (args, &volume))
        return NULL;
    if (volume < 0 || volume > MIX_MAX_VOLUME)
    {
        PyErr_SetString (PyExc_ValueError, "volume must be in the range 0-128");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS;
    result = Mix_VolumeMusic (volume);
    Py_END_ALLOW_THREADS
    return PyInt_FromLong ((long)result);
}

static PyObject*
_music_getvolume (PyObject *self)
{
    int volume;
    ASSERT_MIXER_OPEN (NULL);

    Py_BEGIN_ALLOW_THREADS;
    volume = Mix_VolumeMusic (-1);
    Py_END_ALLOW_THREADS;

    return PyInt_FromLong ((long)volume);
}

static PyObject*
_music_pause (PyObject *self)
{
    ASSERT_MIXER_OPEN (NULL);
    
    Py_BEGIN_ALLOW_THREADS;
    if (Mix_PlayingMusic ())
        Mix_PauseMusic ();
    Py_END_ALLOW_THREADS;

    Py_RETURN_NONE;
}

static PyObject*
_music_resume (PyObject *self)
{
    ASSERT_MIXER_OPEN (NULL);

    Py_BEGIN_ALLOW_THREADS;
    Mix_ResumeMusic ();
    Py_END_ALLOW_THREADS;

    Py_RETURN_NONE;
}

static PyObject*
_music_halt (PyObject *self)
{
    ASSERT_MIXER_OPEN (NULL);

    Py_BEGIN_ALLOW_THREADS;
    Mix_HaltMusic ();
    Py_END_ALLOW_THREADS;

    Py_RETURN_NONE;
}

static PyObject*
_music_rewind (PyObject *self)
{
    ASSERT_MIXER_OPEN (NULL);

    Py_BEGIN_ALLOW_THREADS;
    Mix_RewindMusic ();
    Py_END_ALLOW_THREADS;

    Py_RETURN_NONE;
}

static PyObject*
_music_fadeout (PyObject *self, PyObject *args)
{
    int ms, fadeout;

    ASSERT_MIXER_OPEN (NULL);

    if (!IntFromObj (args, &ms))
        return NULL;

    if (ms < 0)
    {
        PyErr_SetString (PyExc_ValueError, "ms must not be negative");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS;
    fadeout = Mix_FadeOutMusic (ms);
    Py_END_ALLOW_THREADS;

    if (!fadeout)
    {
        PyErr_SetString (PyExc_PyGameError, Mix_GetError ());
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject*
_music_playing (PyObject *self)
{
    int playing;
    ASSERT_MIXER_OPEN (NULL);

    Py_BEGIN_ALLOW_THREADS;
    playing = Mix_PlayingMusic ();
    Py_END_ALLOW_THREADS;

    return PyBool_FromLong ((long)playing);
}

static PyObject*
_music_paused (PyObject *self)
{
    int paused;
    ASSERT_MIXER_OPEN (NULL);

    Py_BEGIN_ALLOW_THREADS;
    paused = Mix_PausedMusic ();
    Py_END_ALLOW_THREADS;

    return PyBool_FromLong ((long)paused);
}

static PyObject*
_music_fading (PyObject *self)
{
    Mix_Fading fading;
    ASSERT_MIXER_OPEN (NULL);

    Py_BEGIN_ALLOW_THREADS;
    fading = Mix_FadingMusic ();
    Py_END_ALLOW_THREADS;

    return PyLong_FromUnsignedLong ((unsigned long)fading);
}

static PyObject*
_music_setposition (PyObject *self, PyObject *args)
{
    double pos;
    int result;

    ASSERT_MIXER_OPEN (NULL);
    
    if (!DoubleFromObj (args, &pos))
        return NULL;
    if (pos < 0)
    {
        PyErr_SetString (PyExc_ValueError, "pos must not be negative");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS;
    result = Mix_SetMusicPosition (pos);
    Py_END_ALLOW_THREADS;

    if (result == -1)
    {
        PyErr_SetString (PyExc_PyGameError, Mix_GetError ());
        return NULL;
    }

    Py_RETURN_NONE;
}

static PyObject*
_music_getdecoders (PyObject *self)
{
    int i, count = 0;
    PyObject *list;

    ASSERT_MIXER_OPEN (NULL);

    list = PyList_New (0);
    if (!list)
        return NULL;

    count = Mix_GetNumMusicDecoders ();
    if (count <= 0)
        return list;

    for (i = 0; i < count; i++)
    {
        const char *name = Mix_GetMusicDecoder (i);
        PyObject *item = Text_FromUTF8 (name);
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
    }
    return list;
}

#ifdef IS_PYTHON_3
PyMODINIT_FUNC PyInit_music (void)
#else
PyMODINIT_FUNC initmusic (void)
#endif
{
    PyObject *mod;

#ifdef IS_PYTHON_3
    static struct PyModuleDef _module = {
        PyModuleDef_HEAD_INIT,
        "music",
        DOC_MUSIC,
        -1,
        _music_methods,
         NULL, NULL, NULL, NULL
   };
    mod = PyModule_Create (&_module);
#else
    mod = Py_InitModule3 ("music", _music_methods, DOC_MUSIC);
#endif
    if (!mod)
        goto fail;

    if (import_pygame2_base () < 0)
        goto fail;
    if (import_pygame2_sdl_base () < 0)
        goto fail;
    if (import_pygame2_sdl_rwops () < 0)
        goto fail;
    if (import_pygame2_sdlmixer_base () < 0)
        goto fail;
    MODINIT_RETURN(mod);
fail:
    Py_XDECREF (mod);
    MODINIT_RETURN (NULL);
}
