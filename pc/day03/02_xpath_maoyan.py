from lxml import etree
import time
import requests
import random
import pymysql
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class maoyan():
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
        self.page=1


    def get_page(self,url):
        res=requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        html=res.text
        # print(html)
        #直接来调用解析函数
        self.parse_page(html)

    #用xpath数据提取
    def parse_page(self,html):
        parse_page=etree.HTML(html)
        dd_list=parse_page.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
        for dd in dd_list:
            #电影名称
            name=dd.xpath('./div/div/div[1]/p[1]/a/text()')
            if name:
                name=name[0].strip()
            else:
                name='null'
            #主演
            star=dd.xpath('./div/div/div[1]/p[2]/text()')
            if star:
                star=star[0].strip()
            else:
                star='null'
            #时间
            time= dd.xpath('./div/div/div[1]/p[3]/text()')
            if time:
                time=time[0].strip()[5:15]
            else:
                time='null'
            print({'名称':name,'主演':star,'时间':time})




    def main(self):
        for offset in range(0,21,10):
            url=self.baseurl.format(str(offset))
            self.get_page(url)
            print("第%d页完成"%self.page)
            self.page+=1
            time.sleep(random.randint(1,3))


if __name__=='__main__':
    mao=maoyan()
    mao.main()
