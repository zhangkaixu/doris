#!/usr/bin/python3
import collections
import sys
import argparse

def count_lines(instream):
    for ln,line in enumerate(instream):
        if ln%100000==0 : 
            print(ln,file=sys.stderr)
        yield line

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--words',type=str, help='')
    parser.add_argument('--words_threshold',type=int,default=10, help='')
    parser.add_argument('--characters',type=str, help='')
    parser.add_argument('--characters_threshold',type=int,default=1000, help='')
    parser.add_argument('--input',type=str, help='')
    parser.add_argument('--output',type=str, help='')
    args = parser.parse_args()

    instream=open(args.input) if args.input else sys.stdin
    outstream=open(args.output,'w') if args.output else sys.stdout

    cs=set()
    for line in open(args.words):
        c,v=line.split()
        if int(v)<args.words_threshold : break
        cs.add(c)

    chs=set('#')
    if args.characters: 
        for line in open(args.characters):
            line=line.split()
            if len(line)!=2 : continue
            c,v=line
            if int(v)<args.characters_threshold : break
            chs.add(c)


    j=collections.Counter()
    for line in count_lines(instream):
        line=line.strip()
        line='#'+line+'#'
        s2=[(line[i],line[i+3])for i in range(len(line)-3)if line[i+1:i+3] in cs and line[i] in chs and line[3] in chs] 
        s3=[(line[i],line[i+4])for i in range(len(line)-4)if line[i+1:i+4] in cs and line[i] in chs and line[4] in chs] 
        s4=[(line[i],line[i+5])for i in range(len(line)-5)if line[i+1:i+5] in cs and line[i] in chs and line[5] in chs] 
        j.update(s2)
        j.update(s3)
        j.update(s4)

    for k,v in j.most_common():
        if v<100 : break
        print(k[0],k[1],v,file=outstream)
