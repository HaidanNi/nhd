from lxml import etree
import time
import requests
import random
from fake_useragent import UserAgent

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
ua=UserAgent()
print(ua.random)


class lianjiaSpider():
    def __init__(self):
        self.baseurl = "https://tieba.baidu.com/f?kw=%E9%AD%94%E9%81%93%E7%A5%96%E5%B8%88&pn={}"
        self.headers = {"User-Agent":str(ua)}
        self.page=1


    def get_page(self,url):
        html=requests.get(url,headers=self.headers).text
        parse_html=etree.HTML(html)
        t_list=parse_html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href')
        for t in t_list:
            #拼接每个帖子的链接
            t_link='http://tieba.baidu.com'+t
            # print(t_link)
            self.get_img(t_link)

    def get_img(self,t):
        html=requests.get(t,headers=self.headers).text
        img_html=etree.HTML(html)
        img_list=img_html.xpath('//*[@id="j_p_postlist"]/div[1]/div[2]/div[1]/cc/div/img/@src')
        for i in img_list:
            html=requests.get(i,headers=self.headers).content
            filename=i[-10:]
            with open(filename,"wb") as f:
                f.write(html)








if __name__=='__main__':
    mao=lianjiaSpider()
    mao.get_page(mao.baseurl)