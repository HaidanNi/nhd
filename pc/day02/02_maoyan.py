import re
from urllib import request
import time
import csv
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class maoyan():
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
        self.page=1

    def get_page(self,url):
        req=request.Request(url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode("utf-8")
        #直接来调用解析函数
        self.parse_page(html)


    def parse_page(self,html):
        pattren=re.compile('<div class="movie-item-info">.*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        film_list=pattren.findall(html)
        # print(film_list)
        self.write_csv(film_list)

    def write_csv(self,film_list):
            film_last_list=[]
            for film in film_list:
                L=(film[0],film[1].strip(),film[2])
                film_last_list.append(L)

            with open("maoyan.csv", 'a') as f:
                writer = csv.writer(f)
                writer.writerow(film_last_list)

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
