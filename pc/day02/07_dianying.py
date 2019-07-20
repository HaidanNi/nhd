from urllib import request,parse
import re
import time
import random
import pymongo
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Film(object):
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['dianying']
        self.myset = self.db['films']

    #获取响应内容（两级页面）
    def get_papg(self,url):
        req=request.Request(url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode("gb2312","ignore")
        return html

    def parser_one_page(self,html):
        pattern=re.compile('<table width="100%" .*?<a href="(.*?)".*?>(.*?)</a>',re.S)
        film_list=pattern.findall(html)
        # print(film_list)
        for film in film_list:
            nama=film[1].strip()
            link='https://www.dytt8.net'+film[0].strip()
            #向link发请求，获取下载链接（二级页面）
            download_link=self.get_two_page(link)

    def get_two_page(self,link):
        #发请求
        html=self.get_papg(link)
        #解析
        pattern=re.compile('<td style="WORD-WRAP.*?<a href="(.*?)"',re.S)
        print(pattern.findall(html)[0])


    def main(self):
        url = "https://www.dytt8.net/html/gndy/dyzz/index.html"
        html=self.get_papg(url)
        self.parser_one_page(html)


if __name__=="__main__":
    # url="https://www.dytt8.net/html/gndy/dyzz/index.html"
    f=Film()
    f.main()
    # html=f.get_papg(url)
    # f.parser_one_page(html)

