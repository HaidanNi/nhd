
import re
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Film(object):
    def __init__(self):
        self.url="https://hz.lianjia.com/ershoufang/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}

    def get_papg(self):
        html=requests.get(self.url,headers=self.headers).text
        return html

    def parser_one_page(self,html):
        pattern=re.compile('<li class="clear LOGCLICKDATA".*?data-el="region">(.*?)</a>.*?<div class="priceInfo">.*?<span>(.*?)</span>("万")',re.S)
        film_list=pattern.findall(html)
        # print(film_list)
        for film in film_list:
            nama=[film[0].strip(),film[1].strip()]
            print(nama)


    def main(self):
        html=self.get_papg()
        self.parser_one_page(html)



if __name__=="__main__":
    f=Film()
    f.main()

