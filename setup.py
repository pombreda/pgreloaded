#!/usr/bin/env python
import sys
import platform
from distutils.core import setup
from distutils.command.install_data import install_data

VERSION = "2.0.0-alpha6"

if __name__ == "__main__":

    if "--format=msi" in sys.argv or "bdist_msi" in sys.argv:
        # hack the version name to a format msi doesn't have trouble with
        VERSION = VERSION.replace("-alpha", "a")
        VERSION = VERSION.replace("-rc", "r")


    packages = [ "pygame2",
                 "pygame2.openal",
                 "pygame2.dll",
                 "pygame2.sdl",
                 "pygame2.test",
                 "pygame2.test.util",
                 ]
    package_dir = { "pygame2" : "lib",
                    "pygame2.dll" : "lib/dll",
                    "pygame2.test" : "test" }

    package_data = { "pygame2.test" : ["resources/*.*"],
                     "pygame2.dll" : ["*.dll"] }
                    
    setupdata = {
        "name" :  "pygame2",
        "version" : VERSION,
        "description" : "Python Game Development Library",
        "author" : "Marcus von Appen",
        "author_email" : "marcus@sysfault.org",
        "license" : "ZLIB",
        "url" : "http://code.google.com/p/pgreloaded",
        "packages" : packages,
        "package_dir" : package_dir,
        "package_data" : package_data,
        }
    setup (**setupdata)
