#!/usr/bin/python3
import collections
import sys
import argparse

def count_lines(instream):
    for ln,line in enumerate(instream):
        if ln%100000==0 : 
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

    history={('','')}
    ls,rs=0,0
    if args.historyfile :
        history=set()
        for line in open(args.historyfile):
            line=line.split()
            if len(line)!=3 : continue
            l,r,v=line
            if int(v)<args.characters_threshold : break
            ls=len(l)
            rs=len(r)
            history.add((l,r))

    dl=args.dl
    dr=args.dr
    j=collections.Counter()
    for line in count_lines(instream):
        line=line.strip()
        line='#'+line+'#'
        for wl in [2,3,4] :
            ss=[(line[i:i+dl+ls],line[i+dl+ls+wl:i+dl+ls+wl+rs+dr])
                    for i in range(len(line)-dl-dr-wl-rs-ls+1)
                    if(line[i+dl+ls:i+dl+ls+wl]in cs and
                        (line[i+dl:i+dl+ls],line[i+dl+ls+wl:i+dl+ls+wl+rs]) in history
                        )]

            j.update(ss)
            pass

    for k,v in j.most_common():
        if v<args.characters_threshold : break
        if len(k[0])!=ls+dl or len(k[1])!=rs+dr : break
        print(k[0],k[1],v,file=outstream)
    outstream.flush()
