"""General purpose event handling routines"""
from pygame2.compat import *

# _HASMP = True
# try:
#     from multiprocessing import Pool
# except:
#     _HASMP = False


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


# class MPEventHandler(EventHandler):
#     """TODO"""
#     def __init__(self, sender, procs=5):
#         if not _HASMP:
#             # TODO: define an appropriate UnsupportedError somewhere
#             raise Exception("no multiprocessing support found")
#         self.procs = procs
#
#     def __call__(self, *args):
#         pool = Pool(processes=procs)
#         pool.map(lambda cb, args: cb(*args), self.callbacks)
