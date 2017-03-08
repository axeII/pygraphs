#
# Makefile for Python3
#
# Interpreter: python34
# Author: Ales Lerch
#

all:
	for pyfile in $$(ls -d ./tasks/*.py) ; do \
		FILENAME=$$(echo $$pyfile | cut -d / -f3 | cut -d . -f1) ; \
	    touch $$FILENAME ; \
	    chmod a+x $$FILENAME ; \
		echo "#!/bin/bash" > $$FILENAME ; \
		echo "$$(which python3) $$pyfile" >> $$FILENAME ; \
	done


clean:
	for pyfile in $$(ls -d ./tasks/*.py) ; do \
		FILENAME=$$(echo $$pyfile | cut -d / -f3 | cut -d . -f1) ; \
		rm -f $$FILENAME ; \
	done

clr:
	clear
fresh : clean all clr
