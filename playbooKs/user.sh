#!/bin/bash

if grep -q "$1" /etc/passwd; then
	echo "$1 already exists"
else
	sudo useradd "$1"
	echo "letmein" | sudo passwd --stdin "$1"
fi
