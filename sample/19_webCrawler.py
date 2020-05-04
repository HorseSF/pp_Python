import urllib.request as req

# 跳过ssl证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url="https://www.ptt.cc/bbs/movie/index.html"

# 建立一个Request，附加request.headers
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

# 解析HTML
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)