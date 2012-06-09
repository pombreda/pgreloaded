"""Thin wrapper around the Ogg Vorbis libraries."""

__all__ = ["OggError"]


class OggError(Exception):
    """An Ogg-Vorbis specific exception class."""
    def __init__(self, msg=None):
        """Creates a new OggVorbisError instance with the specified message.
        """
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
