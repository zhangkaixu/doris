#!/usr/bin/python3

import os
import sys


files=[file for file in os.listdir(sys.path[0]) if 'sina.news.20' in file]

urls=[file for file in files if file[-4:]=='urls'
        and file[:-4]+'pages' not in files]

urls=sorted(urls)

if len(urls)<2:
    print("do not need to download")
    exit()
urls=urls[:-1]
urls=urls[:min(len(urls),5)]
for url in urls:
   
    print("./url_to_pages.sh "+url.rpartition(".")[0])
    os.system("./url_to_pages.sh "+url.rpartition(".")[0])

