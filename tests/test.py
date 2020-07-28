import requests
import demjson
import json

url = "http://www.fuzhou.gov.cn/was5/web/search?channelid=290792&templet=&sortfield=-docorderpri%2C-docreltime&classsql=chnlid%3D5727&random=0.12469431547384024&prepage=10&page=3"

res = requests.get(url)
text = res.text
# text = text.replace("'###pypy###'", '""')
# text = text.replace("'###dydy###'", '""')
print(text)
# res = demjson.decode(text, encoding="urf-8")
res = json.loads(text, encoding="utf-8")
print(res)