from selenium import webdriver
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class JdSpider(object):
    def __init__(self):
        #创建浏览器对象
        self.url='https://www.jd.com'
        self.browser=webdriver.Firefox()
        self.i=0

    #打开京东，输入搜索内容，点击搜索
    def get_page(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys("爬虫书籍")
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)

    #提取商品信息
    def parse_page(self):
        li_list=self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        #li_list:[]
        for li in li_list:
            product_list=li.text.split("\n")
            if product_list[0]=='单价':
                price = product_list[2]
                # 名字
                name = product_list[3]
                # 商家
                market = product_list[5]
            else:
                #价格
                price=product_list[0]
                #名字
                name=product_list[1]
                #商家
                market=product_list[2]
            print([price,name,market])
            self.i+=1
            print("*"*50)
    def main(self):
        self.get_page()
        self.parse_page()
if __name__=="__main":
    spider=JdSpider()
    spider.get_page()
    spider.parse_page()