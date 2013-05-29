#!/usr/bin/python3
import os
import collections
import argparse
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input',type=str, help='')
    parser.add_argument('--output',type=str, help='')
    args = parser.parse_args()

    instream=open(args.input) if args.input else sys.stdin
    outstream=open(args.output,'w') if args.output else sys.stdout

    counter=collections.Counter()
    for line in instream:
        k,_,v=line.rpartition(' ')
        counter.update({k : int(v)})
    s=0
    for k,v in counter.most_common():
        s+=v
        print(k,v,file=outstream)
    print('token %i'%(s),file=sys.stderr)


