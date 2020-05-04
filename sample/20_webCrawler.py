# 抓取ptt八卦版的内容
def getData(url):
    # 跳过ssl证书验证
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    import urllib.request as req

    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)

    # 抓取上一页连接
    nextLink=root.find("a",string="‹ 上頁")
    return nextLink["href"]

# 抓取多页
pageUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
x=input("抓取几页：")
x=int(x)
while count<x:
    pageUrl="https://www.ptt.cc"+getData(pageUrl)
    count+=1