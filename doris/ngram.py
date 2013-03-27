#!/usr/bin/python3
import collections
import sys
import argparse

"""
7z e -so sogout/SogouT.011.txt.7z| sed 's/^[^\ ]*\ //g' | sed 's/\ /\n/g' | ./ngram.py > 1gram.txt
"""

def count_lines(instream):
    for ln,line in enumerate(instream):
        if ln%1000000==0 : 
            print(ln,file=sys.stderr)
            #if ln>3000000 : return
        yield line

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--words',type=str, help='')
    parser.add_argument('--words_threshold',type=int,default=10, help='')
    parser.add_argument('--characters',type=str, help='')
    parser.add_argument('--characters_threshold',type=int,default=1000, help='')
    parser.add_argument('--dl',type=int,default=1, help='')
    parser.add_argument('--dr',type=int,default=1, help='')
    parser.add_argument('--historyfile',type=str, help='')
    parser.add_argument('--input',type=str, help='')
    parser.add_argument('--output',type=str, help='')
    args = parser.parse_args()

    instream=open(args.input) if args.input else sys.stdin
    outstream=open(args.output,'w') if args.output else sys.stdout

    history={''}
    hlen=0
    if args.historyfile :
        for line in open(args.historyfile):
            
            s,f=line.split()
            f=int(f)

            hlen=len(s)
            history.add(s)

    counter=collections.Counter()
    #for line in instream :
    for line in count_lines(instream):
        line='^'+line.strip()+'$'
        counter.update({line[i:i+hlen+1] for i in range(len(line)-hlen) if line[i:i+hlen] in history})

    for k,v in counter.most_common() :
        print(k,v,file=outstream)
