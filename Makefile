PYTHON ?= python
top_srcdir := `pwd`
PYTHONPATH ?= $(top_srcdir)
SUBDIRS = \
	$(top_srcdir)/doc \
	$(top_srcdir)/examples \
	$(top_srcdir)/examples/resources \
	$(top_srcdir)/pygame2/test \
	$(top_srcdir)/pygame2/test/resources \
	$(top_srcdir)/pygame2/test/util \
	$(top_srcdir)/pygame2 \
	$(top_srcdir)/pygame2/audio \
	$(top_srcdir)/pygame2/dll \
	$(top_srcdir)/pygame2/dll/32bit \
	$(top_srcdir)/pygame2/dll/64bit \
	$(top_srcdir)/pygame2/ogg \
	$(top_srcdir)/pygame2/openal \
	$(top_srcdir)/pygame2/sdl \
	$(top_srcdir)/pygame2/video \
	$(top_srcdir)/util

all: clean build

dist: clean docs
	@echo "Creating dist..."
	@$(PYTHON) setup.py sdist --format gztar
	@$(PYTHON) setup.py sdist --format zip

bdist: clean docs
	@echo "Creating bdist..."
	@$(PYTHON) setup.py bdist

build:
	@echo "Running build"
	@$(PYTHON) setup.py build
	@echo "Build finished, invoke 'make install' to install."


install:
	@echo "Installing..."
	@$(PYTHON) setup.py install

clean:
	@echo "Cleaning up in $(top_srcdir)/ ..."
	@rm -f *.cache *.core *~ MANIFEST *.pyc *.orig
	@rm -rf __pycache__
	@rm -rf build dist doc/html

	@for dir in $(SUBDIRS); do \
		if test -f $$dir/Makefile; then \
			make -C $$dir clean; \
		else \
			cd $$dir; \
			echo "Cleaning up in $$dir..."; \
			rm -f *~ *.cache *.core *.pyc *.orig *py.class; \
			rm -rf __pycache__; \
		fi \
	done

docs:
	@echo "Creating docs package"
	@rm -rf doc/html
	@cd doc && make html
	@mv doc/_build/html doc/html
	@rm -rf doc/_build
	@cd doc && make clean

release: dist
runtest:
	@PYTHONPATH=$(PYTHONPATH) $(PYTHON) -B pygame2/test/util/runtests.py

# Do not run these in production environments! They are for testing
# purposes only!

buildall: clean
	@python2.7 setup.py build
	@python3.1 setup.py build
	@python3.2 setup.py build
	@python3.3 setup.py build
	@pypy1.9 setup.py build


installall:
	@python2.7 setup.py install
	@python3.1 setup.py install
	@python3.2 setup.py install
	@python3.3 setup.py install
	@pypy1.9 setup.py install

testall:
	@rm -rf pygame2/test/*.pyc
	@-PYTHONPATH=$(PYTHONPATH) python2.7 pygame2/test/util/runtests.py
	@rm -rf pygame2/test/*.pyc
	@-PYTHONPATH=$(PYTHONPATH) python3.1 pygame2/test/util/runtests.py
	@rm -rf pygame2/test/*.pyc
	@-PYTHONPATH=$(PYTHONPATH) python3.2 pygame2/test/util/runtests.py
	@rm -rf pygame2/test/*.pyc
	@-PYTHONPATH=$(PYTHONPATH) python3.2 pygame2/test/util/runtests.py
	@rm -rf pygame2/test/*.pyc
	@-PYTHONPATH=$(PYTHONPATH) pypy1.9 pygame2/test/util/runtests.py
	@rm -rf pygame2/test/*.pyc

testpackage:
	@python2.7 -c "import pygame2.test; pygame2.test.run()"
	@python3.1 -c "import pygame2.test; pygame2.test.run()"
	@python3.2 -c "import pygame2.test; pygame2.test.run()"
	@python3.3 -c "import pygame2.test; pygame2.test.run()"
	@pypy1.9 -c "import pygame2.test; pygame2.test.run()"

purge_installs:
	rm -rf /usr/local/lib/python2.7/site-packages/pygame2*
	rm -rf /usr/local/lib/python3.1/site-packages/pygame2*
	rm -rf /usr/local/lib/python3.2/site-packages/pygame2*
	rm -rf /usr/local/lib/python3.3/site-packages/pygame2*
	rm -rf /usr/local/lib/pypy-1.9/site-packages/pygame2*

