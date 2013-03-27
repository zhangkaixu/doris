#!/usr/bin/python3
import os
import collections
import random
from multiprocessing import Pool
import time
import subprocess



def job(filename):
    #wash
    #command=(r"7z e -so %s | ./wash.py | 7z a -si  %s"
    #        %('sogout/'+filename,'washed/'+filename))

    #1gram
    #command=(r"7z e -so %s | sed 's/^[^\ ]*\ //g' | sed 's/\ /\n/g' | ./ngram.py > %s"
    #        %('sogout/'+filename,'1gram/'+filename.rpartition('.')[0]))
    #2gram
    command=(r"7z e -so %s | sed 's/^[^\ ]*\ //g' | sed 's/\ /\n/g' | ./ngram.py --historyfile 1gram.txt > %s"
            %('sogout/'+filename,'2gram/'+filename.rpartition('.')[0]))
    #2gram
    #command=(r"7z e -so %s | sed 's/^[^\ ]*\ //g' | sed 's/\ /\n/g' | ./ngram.py --historyfile 2gram1.txt > %s"
    #        %('sogout/'+filename,'3gram1/'+filename.rpartition('.')[0]))
    #print(command)
    p=subprocess.Popen(command,shell=True)
    p.wait()

if __name__ == '__main__':

    files=sorted(os.listdir('sogout'))
    #files=files[:1]
    print(files)

    p = Pool(10)
    
    for res in p.imap_unordered(job,files):
    #for res in map(job,files):
        pass

