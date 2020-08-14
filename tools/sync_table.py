import os

import fire
from atlassian import Confluence
from bs4 import BeautifulSoup
from colorama import Fore
from tqdm import tqdm

from spider.db import DB

usr = os.getenv("mysql_usr")
pwd = os.getenv("mysql_pwd")
mysql_uri = f"mysql://{usr}:{pwd}@rm-2ze3450z16n1c2msxco.mysql.rds.aliyuncs.com:3306/xinhuaspider"
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
tasks = {
    "dijishi": 328080,
    "wangxinban": 329573,
}

# 地级市
# res = confluence.get_page_by_id(328080, expand="body.storage")

# 网信办
# res = confluence.get_page_by_id(329573, expand="body.storage")


def main(table_name="wangxinban"):
    page_id = tasks[table_name]
    res = confluence.get_page_by_id(page_id, expand="body.storage")

    data = res["body"]["storage"]["value"]
    soup = BeautifulSoup(data, "html.parser")
    web_sites = soup.find_all("tr")

    for each in tqdm(web_sites, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):
        td = each.find_all("td")
        if not td:
            continue
        _id = td[0].text
        web_site = td[1].text
        conf_task = td[2].find("ac:task-status")
        if conf_task:
            conf_status = True if conf_task.text == "complete" else 2
        else:
            continue
        conf_date = td[2].find("time").get("datetime")
        submit_status = True if td[4].find("ac:task-status").text == "complete" else 2
        submit_date = td[4].find("time").get("datetime")
        configer = td[5].find("ri:user").get("ri:userkey")
        user = users[configer]
        approved_status = True if td[8].find("ac:task-status").text == "complete" else 2
        approved_date = td[8].find("time").get("datetime")
        online_status = True if td[9].find("ac:task-status").text == "complete" else 2
        online_date = td[9].find("time").get("datetime")

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
        # db.add(record, table_name="progress")
        condition = {"web_site": web_site}
        # db.update(record, condition=condition, table_name="progress")
        db.update(record, condition=condition, table_name=table_name)
    db.close()


if __name__ == "__main__":
    fire.Fire(main)
