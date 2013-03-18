#!/usr/bin/python3

import collections
import sys



if __name__ == '__main__':
    cs=set('#')
    for line in open("data/high_freq.words"):
        c,v=line.split()
        cs.add(c)


    ln=0
    j=collections.Counter()
    for line in open('data/sina.news.txt'):
        ln+=1
        if ln%100000==0 : 
            #12243297
            #  100000
            print(ln,file=sys.stderr)
            #break
        line=line.strip()
        line='#'+line+'#'
        s2=[(line[i],line[i+3])for i in range(len(line)-3)if line[i+1:i+3] in cs] 
        s3=[(line[i],line[i+4])for i in range(len(line)-4)if line[i+1:i+4] in cs] 
        s4=[(line[i],line[i+5])for i in range(len(line)-5)if line[i+1:i+5] in cs] 
        j.update(s2)
        j.update(s3)
        j.update(s4)

    for k,v in j.most_common():
        if v<100 : break
        print(k[0],k[1],v)
