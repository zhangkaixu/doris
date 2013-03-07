#!/usr/bin/python3
import json
import crawler
import time


def gen_time_str(t):
    t=time.localtime(t)
    t=(str(t[0]),str(t[1]),str(t[2]))
    st=t[0]+"-"+('0'+t[1] if len(t[1])==1 else t[1])+"-"+('0'+t[2] if len(t[2])==1 else t[2])
    return st
if __name__=="__main__":
    group='sina.news'
    cache=json.load(open(group+'.cache',encoding="utf8"))
    for line in open(group,encoding="utf8"):
        name,rss=line.split()
        #print("crawling",name)
        data=crawler.crawl(rss)
        if data is None:continue

        items=json.loads(data.decode())['items']

        urls={item['alternate']['href']:gen_time_str(item['published']) for item in items}

        old_urls=set(cache.get(name,list()))
        print("new items",len(urls.keys()-old_urls))
        for url in urls.keys()-old_urls:
            urls_file=open(group+'.'+urls[url]+'.urls','a',encoding="utf8")
            print(name,url,file=urls_file)
            urls_file.close()
        cache[name]=list(urls.keys())
        
        json.dump(cache,open(group+'.cache','w',encoding="utf8"),ensure_ascii=False)


