import requests
url="http://wx2.sinaimg.cn/large/61e7f4aaly1g0qsmz73juj20iv0iv4h0.jpg"
headers = {"User-Agent": "Mozilla/5.0"}

html=requests.get(url,headers=headers).content
#非结构化数据保存
with open("赵丽颖.jpg",'wb') as f:
    f.write(html)


