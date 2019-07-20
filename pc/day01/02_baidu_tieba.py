from urllib import request,parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class BaiduSpider(object):
    def __init__(self):
        self.baseurl = "https://tieba.baidu.com/f?{}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}

    #获取页面
    def get_page(self,url):
        req=request.Request(url,headers=self.headers)
        res=request.urlopen(req,timeout=10)
        html=res.read().decode("utf-8")
        return html

    #解析页面
    def parse_page(self):
        pass

    #保存信息
    def wirte_page(self,filename,html):
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)


    #主函数
    def main(self):
        name=input("请输入要查询的贴吧名")
        startpage=int(input("请输入查询的起始页"))
        endpage=int(input("请输入查询的结束页"))

        for page in range(startpage,endpage+1):
            pn=(startpage-1)*50
            query_string={'kw':name,
                          'pn':str(pn)}
            query_string=parse.urlencode(query_string)
            url=self.baseurl.format(query_string)

            html=self.get_page(url)
            print("第{}页正在下载".format(page))
            self.wirte_page("第%s页"%page,html)
            print("第{}页下载成功".format(page))

if __name__=="__main__":
    spider=BaiduSpider()
    spider.main()
