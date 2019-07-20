import requests

url="http://www.baidu.com/"
headers = {"User-Agent": "Mozilla/5.0"}

res=requests.get(url,headers=headers)
# print(res.encoding)  #ISO-8859-1
res.encoding='utf-8'  #显示自负编码
# print(res.text)#.text 直接就是字符串类型
print(res.content) #字节流
print(res.status_code) #http响应吗
print(res.url) #实际数据的url地址


