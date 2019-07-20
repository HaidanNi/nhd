from lxml import etree
import time
import requests
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class lianjiaSpider():
    def __init__(self):
        self.baseurl = "https://hz.lianjia.com/ershoufang/pg{}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
        self.page=1


    def get_page(self,url):
        res=requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        html=res.text
        #直接来调用解析函数
        self.parse_page(html)

    #用xpath数据提取
    def parse_page(self,html):
        parse=etree.HTML(html)
        r_list=parse.xpath('//*[@id="content"]/div[1]/ul/li')
        for dd in r_list:
            name = dd.xpath('./div[1]/div[2]/div/a/text()')
            if name:
                name = name[0].strip()
            else:
                name = 'null'

            price = dd.xpath('./div[1]/div[6]/div[2]/span/text()')
            if price:
                price = price[0].strip()
            else:
                price = 'null'

            total_price = dd.xpath('./div[1]/div[6]/div[1]/span/text()')
            if price:
                total_price = total_price[0].strip()+"万"
            else:
                total_price = 'null'

            print({'小区': name, '单价': price, '总价': total_price})



    def main(self):
        for offset in range(1,3):
            url=self.baseurl.format(str(offset))
            self.get_page(url)
            print("第%d页完成"%self.page)
            self.page+=1
            time.sleep(random.randint(1,3))


if __name__=='__main__':
    mao=lianjiaSpider()
    mao.main()
