@rem In case you are using the VC++ Toolkit
@rem --------------------------------------
@rem Set the PATH, INCLUDE and LIB to include the Platform SDK and VC++ Toolkit,
@rem and .NET Framework SDK 1.1 VC++ library paths of your system, in case they
@rem are not already.
@rem

@Set MSSdk=C:\Program Files\Microsoft Platform SDK
@Set NETSdk=C:\Program Files\Microsoft Visual Studio .NET 2003

@Set PATH=%VCToolkitInstallDir%\bin;%MSSdk%\Bin;%MSSdk%\Bin\win64;%PATH%
@Set INCLUDE=%VCToolkitInstallDir%\include;%MSSdk%\Include;%INCLUDE%
@Set LIB=%NETSdk%\Vc7\lib;%VCToolkitInstallDir%\lib;%MSSdk%\Lib;%LIB%

@rem Delete the previous builds
@del /S /Q build

@if "%1" == "package" (
    echo Executing packaging: 'PYTHON setup.py build bdist_XXX'
    Set WITH_OPENMP=0
    \Python24\python.exe setup.py build bdist_wininst || goto failure
    Set WITH_OPENMP=1
    \Python25\python.exe setup.py build bdist_msi || goto failure
    \Python26\python.exe setup.py build bdist_msi || goto failure
    \Python27\python.exe setup.py build bdist_msi || goto failure
    \Python31\python.exe setup.py build bdist_msi || goto failure
) else if "%1" == "buildall" (
    echo Executing buildall: 'PYTHON setup.py build install'
    Set WITH_OPENMP=0
    \Python24\python.exe setup.py build install || goto failure
    \Python25\python.exe setup.py build install || goto failure
    Set WITH_OPENMP=1
    \Python26\python.exe setup.py build install || goto failure
    \Python27\python.exe setup.py build install || goto failure
    \Python31\python.exe setup.py build install || goto failure
) else (
    echo Executing single build: 'python.exe setup.py build install'
    python.exe setup.py build install || goto failure
)

:failure:
    @echo An error occured on building
pause
