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
    "2c918083730fcf0201731025c8800003": "房天生",
}
tasks = {
    "dijishi": 328080,
    "wangxinban": 3212315,
}


def main(table_name="dijishi"):
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
            conf_status = True if conf_task.text == "complete" else False
        else:
            continue
        conf_date = td[2].find("time").get("datetime")
        print(td[4])

        submit_status = True if td[3].find("ac:task-status").text == "complete" else False
        submit_date = td[3].find("time").get("datetime")
        configer = td[4].find("ri:user").get("ri:userkey")
        user = users[configer]

        approved_status = True if td[7].find("ac:task-status").text == "complete" else False
        approved_date = td[7].find("time").get("datetime")
        online_status = True if td[8].find("ac:task-status").text == "complete" else False
        online_date = td[8].find("time").get("datetime")

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
        condition = {"web_site": web_site}
        # db.add(record, condition=condition, table_name=table_name)
        db.update(record, condition=condition, table_name=table_name)
    db.close()


if __name__ == "__main__":
    fire.Fire(main)
