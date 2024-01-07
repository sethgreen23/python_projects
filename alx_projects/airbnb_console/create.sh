#!/usr/bin/env bash

if [ -z "$1" ]
then
	echo "./create.sh {FILE_NAME}"
else
	touch "$1" &&chmod u+x "$1" && code "$1"
fi
