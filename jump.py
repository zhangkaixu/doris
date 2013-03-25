#!/usr/bin/python3

import collections
import sys



if __name__ == '__main__':
    cs=set('#')
    for line in open("unigram.txt"):
        c,v=line.split()
        if int(v) < 100 : break
        cs.add(c)


    ln=0
    j=collections.Counter()
    for line in open('cor.txt'):
        ln+=1
        if ln%1000==0 : print(ln,file=sys.stderr)
        line=line.strip()
        line='#'+line+'#'
        s2=[(line[i],line[i+3])for i in range(len(line)-3)if line[i] in cs and line[i+3] in cs] 
        s3=[(line[i],line[i+4])for i in range(len(line)-4)if line[i] in cs and line[i+4] in cs] 
        s4=[(line[i],line[i+5])for i in range(len(line)-5)if line[i] in cs and line[i+5] in cs]
        j.update(s2)
        j.update(s3)
        j.update(s4)

    for k,v in j.most_common():
        if v<100 : break
        print(k[0],k[1],v)
