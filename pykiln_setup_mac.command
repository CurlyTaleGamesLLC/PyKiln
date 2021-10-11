#!/bin/bash
BASEDIR=$(dirname "$0")
echo "$BASEDIR"
cd $BASEDIR

# I haven't tested this code on a mac or linux computer it probably doesn't work

if [[ "$(python3 -V)" =~ "Python 3" ]]
then
	echo "Running PyKiln Setup Utility"
	python3 pykiln_setup.py
else
	echo "Python 3 is not installed"
	echo "Please download and install it from https://www.python.org/downloads/"
	if [ "$(uname)" == "Darwin" ]
		then
		open 'https://www.python.org/downloads/'
	else
		xdg-open 'https://www.python.org/downloads/'
	fi
fi