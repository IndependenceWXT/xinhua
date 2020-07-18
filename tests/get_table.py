from pprint import pprint
from collections import Counter
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Map
from pyecharts import options as opts

from spider.network.selector import Selector
from spider.db import DB

db = DB().create("mysql://xinhuaspider:toor@localhost:3306/shangjian")

url = "http://10.40.35.103:8090/rest/api/content/328080?expand=body.storage"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "seraph.confluence=360461%3Ad8989475925afb34f076f55ae6ad0593ba430cba; JSESSIONID=AEA6E70EDBB99064A4ED5FA0FEBD55E1",
    "DNT": "1",
    "Host": "10.40.35.103:8090",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}

users = {
    "2c918083730fcf020173135f0972000d": "张豹",
    "2c918083730fcf020173102e65b8000b": "柯玉强",
    "2c918083730fcf020173102de444000a": "石张毅",
    "2c918083730fcf020173102d487d0009": "王尚文",
    "2c918083730fcf020173135fb401000e": "胡涛涛",
}

res = requests.get(url, headers=headers)
data = res.json()["body"]["storage"]["value"]
# print(data)
soup = BeautifulSoup(data, "html.parser")
web_sites = soup.find_all("tr")

data = Counter()
china = Map()
conf_completed = Counter()
submit_completed = Counter()
approved_completed = Counter()
online_completed = Counter()
for each in web_sites:
    td = each.find_all("td")
    if not td:
        continue
    _id = td[0].text
    web_site = td[1].text
    conf_task = td[2].find("ac:task-status")
    if conf_task:
        conf_status = True if conf_task.text == "complete" else False
    else:
        continue
    conf_date = td[2].find("time").get("datetime")
    submit_status = True if td[4].find("ac:task-status").text == "complete" else False
    submit_date = td[4].find("time").get("datetime")
    configer = td[5].find("ri:user").get("ri:userkey")
    user = users[configer]
    approved_status = True if td[8].find("ac:task-status").text == "complete" else False
    approved_date = td[8].find("time").get("datetime")
    online_status = True if td[9].find("ac:task-status").text == "complete" else False
    online_date = td[9].find("time").get("datetime")
    print(
        _id,
        web_site,
        conf_status,
        conf_date,
        submit_status,
        submit_date,
        user,
        approved_status,
        approved_date,
        online_status,
        online_date,
    )
    city = web_site.replace("市政府", "").replace("市发改委", "")
    # if conf_status:
    #     conf_completed.append((city, 1))
    # if submit_status:
    #     submit_completed.append((city, 1))
    # if approved_status:
    #     approved_completed.append((city, 1))
    # if online_status:
    #     online_completed.append((city, 1))
    data.update()

    conf_completed.update({city: conf_status if conf_status else 0})
    submit_completed.update({city: submit_status if submit_status else 0})
    approved_completed.update({city: approved_status if approved_status else 0})
    online_completed.update({city: online_status if online_status else 0})
    record = {
        "web_site": web_site,
        "user": user,
        "if_configured": conf_status,
        "conf_date": conf_date,
        "if_submit": submit_status,
        "submit_date": submit_date,
        "if_approved": approved_status,
        "approved_date": approved_date
    }
    db.add(record, table_name="progress")


china.add(
    "配置完成",
    [(k, v) for k, v in conf_completed.items()],
    "china-cities",
    label_opts=opts.LabelOpts(is_show=False),
)
china.add(
    "提交完成",
    [(k, v) for k, v in submit_completed.items()],
    "china-cities",
    label_opts=opts.LabelOpts(is_show=False),
)
china.add(
    "审核完成",
    [(k, v) for k, v in approved_completed.items()],
    "china-cities",
    label_opts=opts.LabelOpts(is_show=False),
)
china.add(
    "上线完成",
    [(k, v) for k, v in online_completed.items()],
    "china-cities",
    label_opts=opts.LabelOpts(is_show=False),
)
china.set_global_opts(
    title_opts=opts.TitleOpts(title="地级市"), visualmap_opts=opts.VisualMapOpts(),
)
china.render("china.html")
