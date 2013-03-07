#!/usr/bin/python3
import json
import crawler
import time

if __name__=="__main__":
    group='sina.news'
    for line in open(group,encoding="utf8"):
        print(line)
        input()
        name,rss=line.split()
        #print("crawling",name)
        data=crawler.crawl(rss)
        if data is None:continue
        items=json.loads(data.decode())['items']
        print(len(items))
        print(items[-1])
        input()
        break
