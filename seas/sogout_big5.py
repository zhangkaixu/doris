#!/usr/bin/python3
import sys
import os
import subprocess
import time

"""
基本操作：用这个命令来调用
7z e -so sogout/SogouT.011.txt.7z | ./sogout.py > test.txt
"""

folder='sogout'


def read_lines():
    files=[os.path.join(folder,f) for f in os.listdir(folder)]
    for file in files:
        print(file,file=sys.stderr)
        p=subprocess.Popen(["7z","e","-so","sogout/SogouT.011.txt.7z"],
                stdout=subprocess.PIPE)
        yield p.stdout 


def read_lines_stdin():
    bstdin=sys.stdin.detach()
    id=0
    cor=0
    for doc in gen_docs(bstdin):
        id+=1
        if not doc : continue
        doc=try_decode(doc)
        if not doc : continue
        cor+=1
        print(id,cor)
        pass
    
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



if __name__ == '__main__':
    bstdin=sys.stdin.detach()
    for url,doc in read_files(bstdin):
        if any( b'charset=big5' in x for x in doc[:10]) :
            if b'.hk' not in url and b'.tw' not in url : continue
            for l in doc:
                l=l.strip()
                print(l.decode('big5',errors="ignore"))
            print(b'#!url='+url)




