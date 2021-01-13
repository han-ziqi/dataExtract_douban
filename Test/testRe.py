#-*- codeing = utf-8 -*-
#@Time : 2021/1/11 11:43 上午
#@Author : Han
#@File : testRe.py
#@Software : PyCharm

# 正则表达式：字符串模式（判断字符串是否符合某种标准）
import re

# 创建模式对象
# pat = re.compile("AA") #此处的AA是正则表达式，是用来验证其他字符串
# m=pat.search("ABCAA") #search方法进行比对

# 没有模式对象
# m = re.search("asd","Aasd") #前面是规则(模板)，后面是要校验的对象
# print(m)

# print(re.findall("a","ADSahkhga")) #前面是规则（正则表达式），后面是要校验的字符串

# print(re.findall("[A-Z]+","ADSahkGhga"))

# sub
print(re.sub("a","A","abcdcasd")) # 在第三个字符串中找到a，用A替换

# 建议在正则表达式中，被比较的字符串前面加r，不用担心转义字符的问题