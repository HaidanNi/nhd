import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# url="http://httpbin.org/get"
# headers={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
# #创建一个请求对象
# request=urllib.request.Request(url,headers=headers)
# #获取响应对象
# response=urllib.request.urlopen(request)
# #获取信息
# html=response.read().decode("utf-8")
# print(html)
# print(response.geturl())
# print(response.getcode())


import urllib.parse

headers={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
#编码，拼接url
name=input("请输入贴吧名:")
begin=int(input("请输入开始页码"))
end=int(input("请输入结束页码"))

kw={"kw":name}
kw=urllib.parse.urlencode(kw)

for page in range(begin,end+1):
    pn=(page-1)*50
    url="https://tieba.baidu.com/f?{}&pn={}".format(kw,pn)
    print(url)
    #构建请求对象
    req=urllib.request.Request(url,headers=headers)
    #获取响应对象
    res=urllib.request.urlopen(req)
    html=res.read().decode("utf-8")
    #写文件保存到本地
    filename="第"+str(page)+"页.html"
    with open(filename,"w",encoding="utf-8") as f:
        print("正在下载第%d页"%page)
        f.write(html)
        print("第%d页下载成功"%page)
        print("*"*30)

