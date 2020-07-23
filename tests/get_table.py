from collections import Counter
from pprint import pprint
from urllib.parse import quote_plus, unquote_plus

import requests
from atlassian import Confluence
from bs4 import BeautifulSoup
from pyecharts import options as opts
from pyecharts.charts import Map

from spider.db import DB
from spider.network.selector import Selector


mysql_uri = "mysql://xinhuaspider:xinhuaspider@123@rm-2ze3450z16n1c2msxco.mysql.rds.aliyuncs.com:3306/xinhuaspider"
# mysql_uri = "mysql://root:toor@localhost:3306/shangjian"
db = DB().create(mysql_uri)

confluence = Confluence(
    url="http://10.40.35.103:8090/", username="fangtiansheng", password="fangtiansheng123"
)

users = {
    "2c918083730fcf020173135f0972000d": "张豹",
    "2c918083730fcf020173102e65b8000b": "柯玉强",
    "2c918083730fcf020173102de444000a": "石张毅",
    "2c918083730fcf020173102d487d0009": "王尚文",
    "2c918083730fcf020173135fb401000e": "胡涛涛",
    "2c918083730fcf0201736a0de66d000f": "江港林",
}

res = confluence.get_page_by_id(328080, expand="body.storage")
data = res["body"]["storage"]["value"]
soup = BeautifulSoup(data, "html.parser")
web_sites = soup.find_all("tr")

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

    record = {
        "web_site": web_site,
        "user": user,
        "if_configured": conf_status,
        "conf_date": conf_date,
        "if_submit": submit_status,
        "submit_date": submit_date,
        "if_approved": approved_status,
        "approved_date": approved_date,
        "if_online": online_status,
        "online_date": online_date,
    }
    db.add(record, table_name="progress")
    condition = {"web_site": web_site}
    db.update(record, condition=condition, table_name="progress")
db.close()
