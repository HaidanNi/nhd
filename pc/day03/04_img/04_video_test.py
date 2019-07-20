from lxml import etree
import time
import requests
import random

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from fake_useragent import UserAgent
ua=UserAgent()



class BaiduSpider():
    def __init__(self):
        self.url = "https://tieba.baidu.com/f?"
        self.headers = {"User-Agent":str(ua)}
        self.page=1

    def get_tlink(self,params):
        html=requests.get(self.url,params=params,headers=self.headers).text
        parse_html=etree.HTML(html)
        t_lish=parse_html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href')
        for t in t_lish:
            t_link="https://tieba.baidu.com"+t
            print(t_lish)

    def main(self):
        name=input("请输入贴吧名")
        begin=int(input("请输入起始页"))
        end=int(input("请输入结束页"))
        for page in range(begin,end+1):
            params={
                'kw':name,
                'pn':str((page-1)*50)}
            self.get_tlink(params)


if __name__=='__main__':
    spider=BaiduSpider()
    spider.main()