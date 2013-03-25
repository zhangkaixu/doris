#!/bin/bash
for file in `ls sogout/SogouT.${1}*`
do
    echo $file
    7z e -so ${file} | ./sogout.py | 7z a raw/${file##*/} -si
done
