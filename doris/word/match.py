#!/usr/bin/python3
import collections
import sys
import argparse

def count_lines(instream):
    for ln,line in enumerate(instream):
        if ln%100000==0 : 
            print(ln,file=sys.stderr)
            #if ln>300000 : return
        yield line

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--words',type=str, help='')
    parser.add_argument('--words_threshold',type=int,default=10, help='')
    parser.add_argument('--historyfile',type=str, help='')
    parser.add_argument('--characters_threshold',type=int,default=1000, help='')
    parser.add_argument('--input',type=str, help='')
    parser.add_argument('--output',type=str, help='')
    args = parser.parse_args()

    instream=open(args.input) if args.input else sys.stdin
    outstream=open(args.output,'w') if args.output else sys.stdout

    words={}
    for line in open(args.words):
        c,v=line.split()
        if int(v)<args.words_threshold : break
        words[c]=collections.Counter()

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

    
    for line in count_lines(instream):
        line=line.strip()
        line='#'+line+'#'
        for wl in [2,3,4] :
            for i in range(len(line)+1-wl-ls-rs):
                word=line[i+ls:i+ls+wl]
                if word not in words : continue
                left=line[i:i+ls]
                right=line[i+ls+wl:i+ls+wl+rs]
                jump=(left,right)
                words[word].update((('',''),))
                if jump not in history : continue
                words[word].update((jump,))
    for word,counter in words.items():
        content=' '.join(jump[0]+"/"+jump[1]+"/"+str(freq) for jump,freq in counter.most_common())
        print(word,content,file=outstream)
