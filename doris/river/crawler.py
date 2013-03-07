#!/usr/bin/python3
from urllib.request import urlopen
import re
import os
import sys
"""
Crawler
"""
def crawl(url):
    data=None
    try:
        data=urlopen(url,timeout=30).read()
    except:
        print("something wrong?")
        pass

    """links=set()
    for link in re.findall(r'''<a[^>]*>'''.encode(),data):
        rst=re.search(r'''href=["'\ ]http:\/\/([^"'\ ]*)["'\ ]'''.encode(),link)

        if rst is not None and rst.groups():
            links.add(rst.groups()[0])"""
    return data



if __name__ == '__main__':
    #data,links=crawl("http://www.sina.com.cn/")
    #print(sys.argv)
    if len(sys.argv)==1:quit()
    encoding='utf8'
    data=crawl(sys.argv[1])
    if len(sys.argv)>=3:encoding=sys.argv[2]
    file=sys.stdout
    if len(sys.argv)>=4:file=open(sys.argv[3],"w")
    if data==None:quit()
    file.write(data.decode(encoding))
    file.write("\n")


    #print(len(links))
    #links=[link.decode('gbk',errors='replace') for link in links if link.decode('gbk',errors='replace').partition('/')[0].endswith('sina.com.cn')]
    #print(*links)
    #print(len(links))
