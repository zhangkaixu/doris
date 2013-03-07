#!/usr/bin/python3
"""
设计：
从输入流（或文件）中得到url
下载后以类似SogouT的格式保存到指定文件
将失败的url输出到输出流（或文件）
"""
import crawler
import sys
import time
if __name__=="__main__":
    encoding="gbk"
    page_filename=sys.argv[1]

    for i,url in enumerate(sys.stdin):
        url=url.strip()
        print(url)
        data=crawler.crawl(url)
        print(i+1,file=sys.stderr)
        time.sleep(1)
        if data==None:
            print(url)
        else:
            print("writing",url,file=sys.stderr)
            file=open(page_filename,'a')
            file.write("<doc>\n")
            file.write("<url>"+url+"</url>\n")
            file.write(data.decode(encoding,"replace"))
            file.write("\n</doc>\n")
            file.close()
