#!/usr/bin/python3
import sys
import os
import subprocess
import time
import re
import collections

"""
基本操作：用这个命令来调用
7z e -so sogout/SogouT.011.txt.7z | ./sogout.py > test.txt
"""
    
def read_files(lines):
    doc=[]
    url=b''
    fid=0
    ot=time.time()
    in_doc=False
    for x in lines:
        if not in_doc and x==b'<DOC>\n':
            doc=[]
            fid+=1
            if fid%100000==0:
                t=time.time()
                print(t-ot,fid,file=sys.stderr)
                ot=t
            continue
        if not in_doc and x.startswith(b'<DOCNO>'):
            continue
        if not in_doc and x.startswith(b'<URL>'):
            url=(x[5:-7])
            in_doc=True
            continue
        if in_doc and x==b'</DOC>\n':
            in_doc=False
            yield (url,doc)
        doc.append(x)


def gen_docs():
    total,s=0,0
    bstdin=sys.stdin.detach()
    counter=collections.Counter()
    css={'gb2312','gbk','utf-8'}
    cspat=re.compile(b'<(meta|META) [^>]*charset=([a-zA-Z0-9\-]+)')
    for url,doc in read_files(bstdin):
        total+=1
        doc=[line.strip() for line in doc]
        charlines=[line for line in doc if b'charset=' in line]
        if len(charlines)!=1 : continue
        charline=charlines[0]
        res=cspat.match(charline)
        if not res : continue
        cs=res.group(2).lower().decode()

        counter.update({cs:1})
        if cs not in  css : continue
        s+=1
        doc=[line.decode(cs,errors='ignore') for line in doc]
        url=url.decode(errors='ignore')
        yield url,doc


if __name__ == '__main__':
    cspat=re.compile(r'<[^>]*>')
    chinese_characters=set(chr(i) for i in range(ord('一'),ord('鿋')+1))
    punkpat=re.compile(r'[，。？！：；“”‘’、]')
    chinese_str=re.compile(r'[a-zA-Z0-9，。？！：；“”‘’、《》\-…,.?!\"\']*[一-鿋]+[一-鿋，。？！：；“”‘’、《》\-…,.?!\"\'a-zA-Z0-9]*')
    for url,doc in gen_docs():
        doc=[line for line in doc if punkpat.search(line)]
        if not doc : continue
        doc=[cspat.sub('',line) for line in doc]
        doc=[line.strip() for line in doc if any(c in chinese_characters for c in line)]
        doc=sum([chinese_str.findall(line) for line in doc],[])
        doc=[line for line in doc if punkpat.search(line)]
        if not doc : continue
        print(url,*doc)

