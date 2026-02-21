#!/bin/bash

if [ "$1" = '' ];
then
echo "Incorrect Syntax"
echo "Usage: ./ipsweep.sh 192.168.x"

else
for ip in {1..254}; do
ping "$1.$ip" -c 1 | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
