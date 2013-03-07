#!/bin/bash
sed 's/^.*\ //g' ${1}.urls | python3 ./page_downloader.py ${1}.pages > ${1}.remains

