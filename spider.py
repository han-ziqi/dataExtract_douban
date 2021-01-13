# -*- codeing = utf-8 -*-
# @Time : 2021/1/7 5:43 下午
# @Author : Han
# @File : spider.py
# @Software : PyCharm


from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式进行文字匹配
import urllib.request, urllib.error  # 指定url获取网页数据
import xlwt  # 进行Excel操作
import sqlite3 # 进行SQlite数据库操作




def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1、爬取网页
    datalist = getData(baseurl)
    # savepath = "豆瓣电影Top250.xls"
    dbpath = "movie.db"
    # 3、保存数据
    # saveData(datalist, savepath)
    saveData2DB(datalist, dbpath)



# 影片链接的规则
findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S作用是让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 1、爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码

# 2、逐一解析数据
        soup = BeautifulSoup(html, "html.parser")  # parser是一个解析器
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item) #测试：查看电影全部信息
            data = []  # 保存一部电影全部信息
            item = str(item)
        

            link = re.findall(findLink, item)[0]  # re库通过正则表达式查找字符串
            data.append(link)  # 添加链接

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片

            titles = re.findall(findTitle, item)  # 片名可能只有一个中文名，没有外国名，也有可能都有
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)  # 添加中文名
                otitle = titles[1].replace("/", "")  # 去掉无关符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')  # 外国名留空，保证格式整齐

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的一部电影放进list中

    # print(datalist)

    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    # 用户代理，表示告诉豆瓣服务器，我们是什么浏览器，本质是告诉浏览器，我们可以接受什么水平的内容
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 3、保存数据
def saveData(datalist,savapath):
    print("开始储存数据")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接：", "图片链接", "影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i]) #列名
    for i in range(0, 250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #数据

    book.save(savapath)

# 4、保存数据到数据库
def saveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index ==4 or index ==5:             #分数、评价人数不用加引号
                continue
            data[index] = '"'+data[index]+'"'  #作用：把每一个内容都加上双引号

        sql = '''
        insert into movie250(
        info_link,pic_link,cname,ename,score,rated,introduction,info)
        values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250 
        (
          id integer primary key autoincrement,
          info_link text,
          pic_link text,
          cname varchar,
          ename varchar,
          score numeric ,
          rated numeric ,
          introduction text,
          info text
        )
    ''' #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":  # 当程序执行时# 调用函数
    main()
    print("爬取完毕")