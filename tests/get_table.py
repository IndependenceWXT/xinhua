from spider.network.selector import Selector
from pprint import pprint
from bs4 import BeautifulSoup

import requests

url = "http://10.40.35.103:8090/rest/api/content/328080?expand=body.storage"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "confluence.list.pages.cookie=list-content-tree; JSESSIONID=90D9150FC370C2C161A7416582D4173E",
    "DNT": "1",
    "Host": "10.40.35.103:8090",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
res = requests.get(url, headers=headers)
data = res.json()["body"]["storage"]["value"]
# print(data)
soup = BeautifulSoup(data, 'html.parser')
print(soup)
web_sites = soup.find_all("tr")
for each in web_sites:
    td = each.find_all("td")
    for each in td:
        print(each.text)