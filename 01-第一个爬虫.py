# 爬虫：通过编写程序来获取互联网上的资源
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容

# （1）导入Python的一个包
from urllib.request import urlopen
# 准备要抓取的网址
url = "http://www.jd.com"
# 打开网址得到响应
resp = urlopen(url)

# 从响应读取内容主体，将字节转字符串，解码使用utf-8字符集
# print(resp.read().decode("utf8"))

# 把获取的内容保存到一个文件里面去
# 爬京东网站：报'gbk'代表国标字符集，将“.decode("utf-8")删除；报'\ue600'代表二进制，将mode="w"改为mode="wb"”
with open("myjd.html", mode="wb") as f:
    f.write(resp.read())   #读取到网页的源代码
print("over!")

# 爬百度网站
# with open("mybaidu.html", mode="w") as f:
#     f.write(resp.read().decode("utf-8"))    #读取到网页的源代码
# print("over!")