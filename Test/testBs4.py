''#-*- codeing = utf-8 -*-
#@Time : 2021/1/8 5:14 下午
#@Author : Han
#@File : testBs4.py
#@Software : PyCharm

'''BeautifulSoup4将复杂html文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为四种：

-Tag
-NavigableString
-BeautifulSoup
-Comment
'''

from bs4 import BeautifulSoup
import re
# 1、Tag 标签及其内容：拿到它所找到的第一个内容
# 2、NavigableString：标签里的内容（字符串）
# 3、BeautifulSoup表示整个文档，可以直接进行内容访问
# 4、Comment是一个特殊的NavigableString，输出的内容不包含注释符号

# ----------------------------------------实际应用----------------
# 文档的遍历Contents:获取Tag里所有子节点，返回列表
# print(bs.head.contents)
# print(bs.head.contents[1])


# 文档的搜索
# 1.1find_all   会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")

# 1.2正则表达式搜索：使用search（）方法来匹配内容
# import re
# t_list = bs.find_all(re.compile("a"))

# 1.3方法：传入一个函数（方法），根据函数要求来搜索
# def name_is_exist(tag):
#     return tag.has.attr("name")
# t_list = bs.find_all(name_is_exist())
#
# print(t_list)

# 2、kwargs 参数
# t_list = bs.findall(id="head")

# 3、text参数
t_list = bs.find_all(text=re.compile("/d"))  #应用正则表达式来查找包含特定文本内容（标签里的字符串）

for item in t_list:
    print(item)

# 4、limit参数
t_list = bs.find_all("a",limit=3)

# css选择器
t_list=bs.select('title') #通过标签查找
t_list = bs.select(".nmav") #通过类名来查找
t_list = bs.select(".#u1") #通过id来查找
t_list = bs.select("a[class='bri']") #通过属性来查找
t_list = bs.select("head>title") #通过子标签来查找