#-*- codeing = utf-8 -*-
#@Time : 2021/1/8 10:42 上午
#@Author : Han
#@File : testurllib.py
#@Software : PyCharm

import urllib.request
# 获取一个get请求
#
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8")) #对获取到网页到源# 码用utf-8解码


# 获取一个post请求
'''
import urllib.parse
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
reponse = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(reponse.read().decode("utf-8"))
'''
# 超时处理
# try:
#     reponse = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(reponse.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out")

'''
url = "https://httpbin.org/post"
data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''
url = "https://www.douban.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

