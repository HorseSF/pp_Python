# 抓取全国城市ID
# 全国城市天气
# http://www.msece.com/waether/src/areaDate/101010100.json

import urllib.request as request
import json

# 跳过ssl证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

src="http://www.msece.com/waether/upload/weather/json/NationalUrbanData.min.json"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["province"]
with open("data_city.txt","w",encoding="utf-8") as file:
    for city in clist:
        file.write(city["province"]+"\n")