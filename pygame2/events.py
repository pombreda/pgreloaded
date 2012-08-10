"""General purpose event handling routines"""
from pygame2.compat import *

__all__ = ["EventHandler", "MPEventHandler"]

_HASMP = True
try:
    from multiprocessing import Pool
except ImportError:
    _HASMP = False


class EventHandler(object):
    """A simple event handling class, which manages callbacks to be
    executed.
    """
    def __init__(self, sender):
        self.callbacks = []
        self.sender = sender

    def __call__(self, *args):
        """Executes all callbacks.

        Executes all connected callbacks in the order of addition,
        passing the sender of the EventHandler as first argument and the
        optional args as second, third, ... argument to them.
        """
        for cb in self.callbacks:
            cb(self.sender, *args)

    def __iadd__(self, callback):
        """Adds a callback to the EventHandler."""
        self.add(callback)
        return self

    def __isub__(self, callback):
        """Removes a callback from the EventHandler."""
        self.remove(callback)
        return self

    def __len__(self):
        """Gets the amount of callbacks connected to the EventHandler."""
        return len(self.callbacks)

    def add(self, callback):
        """Adds a callback to the EventHandler."""
        if not callable(callback):
            raise TypeError("callback mus be callable")
        self.callbacks.append(callback)

    def remove(self, callback):
        """Removes a callback from the EventHandler."""
        self.callbacks.remove(callback)


class MPEventHandler(EventHandler):
    """An asynchronous event handling class in which callbacks are
    executed in parallel.

    It is the responsibility of the caller code to ensure that every
    object used maintains a consistent state. The MPEventHandler class
    will not apply any locks, synchronous state changes or anything else
    to the arguments being used. Cosider it a "fire-and-forget" event
    handling strategy
    """
    def __init__(self, sender, maxprocs=5):
        if not _HASMP:
            # TODO: define an appropriate UnsupportedError somewhere
            raise UnsupportedError("no multiprocessing support found")
        self.maxprocs = maxprocs

    def __call__(self, *args):
        pool = Pool(processes=maxprocs)
        pool.map(lambda cb, args: cb(*args), self.callbacks)
