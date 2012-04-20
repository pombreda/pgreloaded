"""Examples for Pygame2.

This package contains the examples for Pygame2.
"""
import os
from pygame2.resources import Resources

__all__ = ["RESOURCES"]

_fpath = os.path.dirname(os.path.abspath(__file__))
RESOURCES = Resources(os.path.join(_fpath, "resources"))
