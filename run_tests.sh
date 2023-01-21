#!/usr/bin/bash

read -p "Run tests? [Y/n]:  "

if [[ $REPLY =~ ^[Yy]$ ]]
then
	python2 -m unittest discover . -v
else
	exit 999
fi

read -p "Run coverage? [Y/n]:  "

if [[ $REPLY =~ ^[Yy]$ ]]
then
	coverage run -m unittest discover . -v
else
	exit 998
fi

read -p "Coverage Report? [Y/n]:  "

if [[ $REPLY =~ ^[Yy]$ ]]
then
	coverage report
else
	exit 997
fi

read -p "Confirm exit, please: [Y/n]:"

if [[ $REPLY =~ ^[Yy]$ ]]
then
	echo Exit confirmed...
	exit 0
fi
