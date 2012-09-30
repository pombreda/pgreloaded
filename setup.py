#!/usr/bin/env python
import sys
import platform
from distutils.core import setup
from distutils.command.install_data import install_data

VERSION = "2.0.0-beta2"

if __name__ == "__main__":

    if "--format=msi" in sys.argv or "bdist_msi" in sys.argv:
        # hack the version name to a format msi doesn't have trouble with
        VERSION = VERSION.replace("-alpha", "a")
        VERSION = VERSION.replace("-beta", "b")
        VERSION = VERSION.replace("-rc", "r")

    packages = ["pygame2",
                "pygame2.audio",
                "pygame2.ogg",
                "pygame2.openal",
                "pygame2.dll",
                "pygame2.dll.32bit",
                "pygame2.dll.64bit",
                "pygame2.examples",
                "pygame2.sdl",
                "pygame2.test",
                "pygame2.test.util",
                "pygame2.video",
                ]
    package_dir = {"pygame2": "pygame2",
                   "pygame2.examples": "examples",
                   }

    package_data = {"pygame2.test": ["resources/*.*"],
                    "pygame2.examples": ["resources/*.*"],
                    "pygame2.dll.32bit": ["*.dll"],
                    "pygame2.dll.64bit": ["*.dll"],
                    }

    setupdata = {
        "name":  "pygame2",
        "version": VERSION,
        "description": "Python Multimedia Development Library",
        "author": "Marcus von Appen",
        "author_email": "marcus@sysfault.org",
        "license": "Public Domain / zlib",
        "url": "http://code.google.com/p/pgreloaded",
        "packages": packages,
        "package_dir": package_dir,
        "package_data": package_data,
        "classifiers": [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: Public Domain",
            "License :: OSI Approved :: zlib/libpng License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.1",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: IronPython",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Topic :: Multimedia",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        }
    setup(**setupdata)
