PYTHON = python
EXPERIMENTAL = 1
top_srcdir = `pwd`
SUBDIRS = \
	$(top_srcdir)/doc \
	$(top_srcdir)/examples \
	$(top_srcdir)/examples/resources \
	$(top_srcdir)/test \
	$(top_srcdir)/test/resources \
	$(top_srcdir)/test/util \
	$(top_srcdir)/lib \
	$(top_srcdir)/lib/dll \
	$(top_srcdir)/lib/dll/32bit \
	$(top_srcdir)/lib/dll/64bit \
	$(top_srcdir)/lib/openal \
	$(top_srcdir)/lib/sdl \
	$(top_srcdir)/lib/video \
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
	@rm -rf build dist

	@for dir in $(SUBDIRS); do \
		if test -f $$dir/Makefile; then \
			make -C $$dir clean; \
		else \
			cd $$dir; \
			echo "Cleaning up in $$dir..."; \
			rm -f *~ *.cache *.core *.pyc *.orig; \
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
	@$(PYTHON) test/util/runtests.py

# Do not run these in production environments! They are for testing
# purposes only!

buildall: clean
	@python2.7 setup.py build
	@python3.1 setup.py build
	@python3.2 setup.py build
	@pypy1.8 setup.py build


installall:
	@python2.7 setup.py install
	@python3.1 setup.py install
	@python3.2 setup.py install
	@pypy1.8 setup.py install

testall:
	@-python2.7 test/util/runtests.py
	@rm -rf test/*.pyc
	@-python3.1 test/util/runtests.py
	@rm -rf test/*.pyc
	@-python3.2 test/util/runtests.py
	@rm -rf test/*.pyc
	@-pypy1.8 test/util/runtests.py
	@rm -rf test/*.pyc

testall2:
	@python2.7 -c "import pygame2.test; pygame2.test.run ()"
	@python3.1 -c "import pygame2.test; pygame2.test.run ()"
	@python3.2 -c "import pygame2.test; pygame2.test.run ()"
	@pypy1.8 -c "import pygame2.test; pygame2.test.run ()"

purge_installs:
	rm -rf /usr/local/lib/python2.7/site-packages/pygame2*
	rm -rf /usr/local/lib/python3.1/site-packages/pygame2*
	rm -rf /usr/local/lib/python3.2/site-packages/pygame2*
	rm -rf /usr/local/pypy-1.8/site-packages/pygame2*

