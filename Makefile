#
# Makefile for Python3
#
# Interpreter: python34
# Author: Ales Lerch
#

all:
	for pyfile in $$(ls -d ./src/*.py) ; do \
		FILENAME=$$(printf $$pyfile | cut -d / -f3 | cut -d . -f1) ; \
	    touch $$FILENAME ; \
	    chmod a+x $$FILENAME ; \
		printf "#!$$(which bash)\n" > $$FILENAME ; \
		printf "\tEditing $$FILENAME - python3 and script source path\n" ; \
		printf "\"$$(which python3)\" \"$$pyfile\"" >> $$FILENAME ; \
	done


clean:
	for pyfile in $$(ls -d ./src/*.py) ; do \
		FILENAME=$$(printf $$pyfile | cut -d / -f3 | cut -d . -f1) ; \
		rm -f $$FILENAME ; \
	done

clr:
	clear

install:
	cp ./src/new_task.sh ./src/new_task
	chmod a+x ./src/new_task

fresh : clean all clr
