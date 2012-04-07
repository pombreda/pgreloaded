"""Unit tests for Pygame2.

This package contains the unit tests for Pygame2. You can execute the
unit tests using

    python -c "import pygame2.test; pygame2.test.run()"

"""
import os
from pygame2.test.util.runtests import run
from pygame2.resources import Resources

__all__ = ["run", "RESOURCES"]


RESOURCES = Resources(os.path.dirname(os.path.abspath(__file__)), ".*py*")
