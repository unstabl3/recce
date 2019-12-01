#!/usr/bin/env bash

if [ ! -x "$(command -v pip3)" ];
then
	echo "[!] It looks you don't have pip3..looking for pip installation.."
	exit 1
elif [ ! -x "$(command -v pip)" ];
then
	echo "[!] You must need pip respective of your python version to run this script.."
	exit 1
else
	echo "running installation.."
fi

if [ $? -eq 0 ];
then
	pip3 install -r requirements.txt
else
	pip install -r requirements.txt
fi

if [ $? -eq 0 ];
then
	echo "creating a command for you.."
	cp recce.py /usr/local/bin/recce >&2
fi
if [ $? -eq 0 ];
then
	echo "Done"
else
	echo "Some error occured"
fi

