#!/bin/bash
7z e -so $1 | sed 's/^[^\ ]*\ //g' | sed 's/\ /\n/g'
