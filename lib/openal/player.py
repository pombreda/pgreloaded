##    pygame - Python Game Library
##    Copyright (C) 2010 Marcus von Appen
##
##    This library is free software; you can redistribute it and/or
##    modify it under the terms of the GNU Library General Public
##    License as published by the Free Software Foundation; either
##    version 2 of the License, or (at your option) any later version.
##
##    This library is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
##    Library General Public License for more details.
##
##    You should have received a copy of the GNU Library General Public
##    License along with this library; if not, write to the Free
##    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##

import pygame2.openal as openal
import pygame2.openal.constants as const

class AudioPlayer (object):

    # Relevant for streaming sources.
    _minbuffersize = 512
    _defaultbuffersize = 16384

    def __init__ (self, format):
        self._format = format
        self._channels = None
        self._samplesize = None

        self._source = None

    def is_playing (self):
        pass

    def play (self):
        pass

    def stop (self):
        pass

    def pause (self):
        pass
    
    def queue (self, data):
        pass

    def clear (self):
        pass

    def set_volume (self, volume):
        pass

    def set_position (self, position):
        pass

    def __del__ (self):
        pass

    playing = property (lambda self: self.is_playing (),
                        doc = """Gets, whether the AudioPlayer is currently
 playing any audio data""")
    channels = property (lambda self: self._channels,
                         doc = "Gets the used audio channels")
    samplesize = property (lambda self: self._samplesize,
                           doc = "Gets the sample size")
    format = property (lambda self: self._format, doc = "Gets the format");
