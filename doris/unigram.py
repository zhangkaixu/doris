#!/usr/bin/python3
import collections
import argparse
import sys


def line_numbered(instream):
    for ln,line in enumerate(instream):
        if ln%100000==0 : 
            print(ln,file=sys.stderr)
        yield line

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input',type=str, help='')
    parser.add_argument('--output',type=str, help='')
    args = parser.parse_args()

    instream=open(args.input) if args.input else sys.stdin
    outstream=open(args.output,'w') if args.output else sys.stdout

    counter=collections.Counter()

    for line in line_numbered(instream) :
        counter.update(line.strip())

    for k,v in counter.most_common():
        print(k,v,file=outstream)

