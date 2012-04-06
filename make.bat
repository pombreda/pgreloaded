@SETLOCAL
@IF "%PYTHON27%" == "" (
    SET PYTHON27=c:\Python27\python.exe
)
@IF "%PYTHON31%" == "" (
    SET PYTHON31=c:\Python31\python.exe
)
@IF "%PYTHON32%" == "" (
    SET PYTHON32=c:\Python32\python.exe
)
@IF "%PYTHON%" == "" (
    SET PYTHON=%PYTHON27%
)
@IF "%PYPY18%" == "" (
    SET PYPY18=c:\pypy-1.8\pypy.exe
)
@IF "%IRONPYTHON27%" == "" (
    SET IRONPYTHON=c:\IronPython27\ipy.exe
)

@IF "%1" == "" (
    GOTO :all
)
@GOTO :%1

:all
@CALL :clean
@CALL :build
@GOTO :eof

:dist
@ECHO Creating dist...
@CALL :clean
@CALL :docs
@%PYTHON% setup.py sdist --format gztar
@%PYTHON% setup.py sdist --format zip
@GOTO :eof

:bdist
@CALL :clean
@CALL :docs
@ECHO Creating bdist...
@%PYTHON% setup.py bdist --format=msi
@GOTO :eof

:build
@ECHO Running build
@%PYTHON% setup.py build
@ECHO Build finished, invoke 'make install' to install.
@GOTO :eof

:install
@ECHO Installing...
@%PYTHON% setup.py install
@GOTO :eof

:clean
@RMDIR /S /Q build
@RMDIR /S /Q dist
@RMDIR /S /Q test\__pycache__
@DEL /Q MANIFEST
@GOTO :eof

:docs
@ECHO Creating docs package
@ECHO TODO
@GOTO :eof

:release
@CALL :dist
@GOTO :eof

:runtest
@%PYTHON% test\util\runtests.py
@GOTO :eof

@REM Do not run these in production environments. They are for testing purposes
@REM only!

:buildall
@CALL :clean
@%PYTHON27% setup.py build
@CALL :clean
@%PYTHON31% setup.py build
@CALL :clean
@%PYTHON32% setup.py build
@CALL :clean
@%PYPY18% setup.py build
@CALL :clean
@%IRONPYTHON27% setup.py build
@CALL :clean
@GOTO :eof

:installall
@CALL :clean
@%PYTHON27% setup.py install
@CALL :clean
@%PYTHON31% setup.py install
@CALL :clean
@%PYTHON32% setup.py install
@CALL :clean
@%PYPY18% setup.py install
@CALL :clean
@%IRONPYTHON27% setup.py install
@CALL :clean
@GOTO :eof

:testall
@%PYTHON27% test\util\runtests.py
@DEL /Q test\*.pyc
@%PYTHON31% test\util\runtests.py
@DEL /Q test\*.pyc  
@%PYTHON32% test\util\runtests.py
@DEL /Q test\*.pyc
@%PYPY18% test\util\runtests.py
@DEL /Q test\*.pyc
@%IRONPYTHON27% test\util\runtests.py
@DEL /Q test\*.pyc
@GOTO :eof

:testall2
@%PYTHON27% -c "import pygame2.test; pygame2.test.run ()"
@%PYTHON31% -c "import pygame2.test; pygame2.test.run ()"
@%PYTHON32% -c "import pygame2.test; pygame2.test.run ()"
@%PYPY18% -c "import pygame2.test; pygame2.test.run ()"
@%IRONPYTHON27% -c "import pygame2.test; pygame2.test.run ()"
@GOTO :eof

:purge_installs
@echo Deleting data...
@RMDIR /S /Q C:\Python27\Lib\site-packages\pygame2
@RMDIR /S /Q C:\Python31\Lib\site-packages\pygame2
@RMDIR /S /Q C:\Python32\Lib\site-packages\pygame2
@RMDIR /S /Q C:\pypy-1.8\site-packages\pygame2
@RMDIR /S /Q C:\IronPython27\Lib\site-packages\pygame2
@echo done
@GOTO :eof

@ENDLOCAL
