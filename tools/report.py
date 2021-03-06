"""

"""

import base64
import hashlib
import hmac
import json
import time
from datetime import datetime, timedelta
from pprint import pprint
from time import sleep
from urllib.parse import quote_plus, urlsplit

import requests
import yaml
from tqdm import tqdm, trange
import fire

users_db = {
    20: "陈亚飞",
    19: "江港林",
    17: "胡涛涛",
    16: "张豹",
    15: "柯玉强",
    14: "石张毅",
    13: "王尚文",
    10: "房天生",
    7: "王小婷",
    6: "唐浩",
}
cookies = {
    'username': 'fangtiansheng',
    'remember_token': '18|3c0e4afbacb93a873a5e93388b0a6d35159f2516fdb56dbfa8cc7a6454f01316b34e9e6721414c272430c7a2ffc426278ce8e2d5f3eaca3746afef6452167041',
    'session': '.eJw1zjFuwzAMQNG7cA4CiqZEypcxRJFCO9gN5GQKeve6Bbp-_OG9YRszzg9Yn_MVN9g-HVZYUkWvKTqzm4W7-ggfvVgyymN0jaVWRey_l5ANtiEsqQhzaaSaRHUgtsq8hEUll9BsQhmlLTk4KzJZqqpNXYlz1ZyblU5EAhfkEXNvRxzPf9qMPXaLuZ3Rvw4_YdXCiHe8weu88p88KXz_AMadPeo.Eo9lVQ.6jkpWl4TNzk4lkPibDvWAHqW_Fc',
    'baelish_session': '.eJw1zkEKAjEQRNG79FqkOyadZC4zJOkKuphRMroS724Q3H6q4L1p7QPHlZbneOFE681oIS8ucxHjEpr00JxzXSp7WDfVojWJqGivihDqxdcABppVlpCMkVk0exetx2xx7vXC85PMpSZaYuPmEwo6I8WOXFqQ2diCOmdaaEIeGFvZsT__tIENW8VYD7T7bgctST3zmU_0Omb-yYXp8wXEbj7h.X63T1g.Y8grWioF-5GultKs1ZbTGDxViMo',
}
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "DNT": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.129 Safari/537.36",
}

proxies = {"http": None, "https": None}


def get_rule_list(group_id):
    """
    create_time: "2019-11-18T14:10:01+08:00"
    extra: {}
    group: 980
    group_name: "Arava Institute"
    id: 7139
    last_run_time: null
    modify_time: "2019-11-18T14:24:11+08:00"
    name: "blog_详情规则"
    next_run_time: null
    project_id: 43
    project_name: "智库项目"
    rule_type: 2
    rule_yml: ""
    status: 1 未启用 0 启用
    user: null
    """
    url = f"https://spider.vpc.shangjian.tech/crawl/crawl/rule/?group__id={group_id}&rule_type=1&fields=id,name,project_name,status,user,rule_type,project_id,create_time,extra,group,group_name"
    while 1:
        try:
            res = requests.get(url, headers=headers, proxies=proxies, cookies=cookies)
        except Exception as e:
            sleep(10)
            continue
        try:
            data = res.json()["results"]
        except Exception as e:
            sleep(2)
        else:
            break
    return data


def get_lastest_batch_result(plan_id):
    """
    config: ""
    done_count: 49
    enqueue_time: "2019-11-18T17:33:54+08:00"
    extra: {}
    finish_time: null
    id: 310670561724338200
    plan: 7098
    priority: 0
    run_id: "310670561724338176"
    start_time: "2019-11-18T17:33:55+08:00"
    status: 1
    total_count: 49
    update_count_time: "2019-12-02T11:10:03+08:00"
    """
    url = f"https://spider.vpc.shangjian.tech/crawl/crawl/run/?plan__id={plan_id}&limit=1&offset=0&sort=-id"
    while 1:
        try:
            res = requests.get(url, headers=headers, proxies=proxies, cookies=cookies)
        except:
            sleep(10)
            continue
        try:
            data = res.json()["results"]
        except:
            sleep(2)
        else:
            break
    return data


def count_configured(users, today=True, ago=False, section=(1565, 1858), notify=False, _type=""):
    """
    {
        1: [275],
        6: [207, 210],
        10: [612, 655]
    }
    today=True: 扫描当前日期的批次记录
    ago=True: 扫描历史调度
    section: 组ID的范围
    """
    res = {k: [] for k in users_db}
    _type = _type + "更新" if not ago else _type + "历史"

    report = []
    ctime = datetime.now().isoformat(sep=" ", timespec="seconds")

    if today and not ago:
        now = datetime.now().date()
        kind = "日报"
        report.append(f"日报[{now.isoformat()}]\n")
    elif not today and ago == False:
        now = datetime.now()
        kind = "扫描报告"
        report.append(f"{_type}调度扫描报告[{now.isoformat()}]\n")
    elif not today and ago:
        now = datetime.now().date()
        user_id = users_db[users[0]]
        kind = f"配置"
        report.append(f"[{kind}]{_type}调度扫描报告\n")

    thead = ["配置者", "完成时间", f"{_type}进度", "网站名"]
    report.append(f"|\t{thead[0]}\t|\t{thead[1]}\t|\t{thead[2]}\t|\t{thead[3]}\t|")
    report.append("|----" * 4 + "|")

    bar = trange(*section)
    for group_id in bar:
        bar.set_description(desc=f"{group_id:0>4}")
        rules = get_rule_list(group_id)
        sleep(1)
        if len(rules) < 1:
            continue
        for rule in rules:
            if _type[-2:] in rule["name"] and rule["user"] in users and rule["status"] == 0:
                plan_id = rule["id"]
                user = rule["user"]
                batches = get_lastest_batch_result(plan_id)
                if len(batches) < 1:
                    tqdm.write(f"调度编号【{plan_id}】没有批次记录")
                    continue
                batch_result = {
                    k: v
                    for k, v in batches[0].items()
                    if k in ["plan", "status", "done_count", "total_count", "start_time"]
                }
                start_time = (
                    batch_result["start_time"]
                    if batch_result["start_time"]
                    else "1970-01-01 00:00:00"
                )
                start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                passed = datetime.now() - start_time
                if today and passed > timedelta(hours=15):
                    continue

                if today and now != start_time.date():
                    continue
                group_name = rule["group_name"]
                total = batch_result["total_count"]
                done = batch_result["done_count"]
                if int(done) == int(total) == 0:
                    tqdm.write(f"{group_name} 调度异常...")
                    continue
                if max(int(total), int(done)) == 0:
                    tqdm.write(f"{group_name} 调度正在启动稍后再试...")
                    continue
                start_time = batch_result["start_time"]
                start_time = start_time.strip() if start_time else "0000-00-00 00:00:00"
                group_name = group_name.split("_")[-1].strip()
                res[user].append(group_name)
                progress = int((done / total) * 100)
                space = " "
                msg = f"|\t{users_db[user]}\t|\t{start_time}\t|\t{progress:>3}%\t|\t{group_name}\t|"
                report.append(msg)
                tqdm.write(msg)
                break
    if len(report) < 2:
        msg = "无新增配置"
        report.append(msg)
        tqdm.write(msg)
    report = "\n".join(report)
    if notify:
        send(report)
    else:
        with open(
            f"../reports/{now.isoformat()}_{_type}调度扫描报告.md", mode="w", encoding="utf-8"
        ) as f:
            f.write(report)
    return {k: v for k, v in res.items() if v}


def check_disable():
    "rule的status为1表示未启用, 0表示启用"
    for group_id in range(200, 1354):
        rules = get_rule_list(group_id)
        if len(rules) < 1:
            continue
        for rule in rules:
            if "更新" in rule["name"] and rule["status"] == 1:
                user = rule["user"]
                print(group_id, user)
                break


def send(text):
    timestamp = int(round(time.time() * 1000))
    secret = "SEC5c93eacdb28c4b23b338a84458483bc275ce8488e42452743a9b20bee402d250"
    secret_enc = bytes(secret, encoding="utf-8")
    string_to_sign = "{}\n{}".format(timestamp, secret)
    string_to_sign_enc = bytes(string_to_sign, encoding="utf-8")
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = quote_plus(base64.b64encode(hmac_code))

    token = "56bf232dc2f33f9f112792b714add24953996b17789e44b4b8ec3b9fafd61a1f"
    headers = {"Content-Type": "application/json"}

    url = f"https://oapi.dingtalk.com/robot/send?access_token={token}&timestamp={timestamp}&sign={sign}"

    data = {
        "msgtype": "text",
        "text": {"content": text},
        "at": {"atMobiles": ["13683084457",], "isAtAll": False},
    }
    s = requests.Session()

    res = s.post(url=url, headers=headers, data=json.dumps(data))
    sleep(3)
    return res.json()


def report_for_user(user_id, section=(1369, 3209)):
    """
    配置人员扫描历史配置的历史调度进度
    """
    users = [k for k in users_db if k == user_id]
    res = count_configured(users, today=False, section=section)


def check_today():
    """
    配置人员扫描今天开始的更新调度进度

    """
    users = [k for k in users_db]
    res = count_configured(users, today=True, ago=False)


def check_update():
    """
    配置人员查看自己的历史配置的更新调度进度
    """
    users = [k for k in users_db]
    res = count_configured(users, today=True)


def report_for_progress():
    """
    生成markdown表格源码格式日报, 用机器人发送到叮叮群
    """
    users = [k for k in users_db]
    res = count_configured(users, today=True)


def report_all_history(index):
    """
    扫描全部开启计划的历史调度
    (1369, 1565)   6月底前完成的配置
    (1565, 1857)   地级市
    (1888, 2253)   附件B等
    (2253, 2905)   网信办
    (2905, 3446)   附件A等
    """
    tasks = [
        {"前期配置": (1369, 1565)},
        {"地级市": (1565, 1857)},
        {"附件B等": (1888, 2253)},
        {"网信办": (2253, 2905)},
        {"附件A等": (2905, 3446)},
    ]
    task = tasks[index]
    (_type,) = task
    section = task[_type]
    print(_type, section)

    users = [k for k in users_db]
    res = count_configured(users, today=False, ago=True, section=section, _type=_type)


def report_all_update(index):
    """
    扫描全部开启计划的更新调度
    (1369, 1565)   6月底前完成的配置
    (1565, 1857)   地级市
    (1888, 2253)   附件B等
    (2253, 2905)   网信办
    (2905, 3446)   附件A等
    """
    tasks = [
        {"前期配置": (1369, 1565)},
        {"地级市": (1565, 1857)},
        {"附件B等": (1888, 2253)},
        {"网信办": (2253, 2905)},
        {"附件A等": (2905, 3446)},
    ]
    task = tasks[index]
    (_type,) = task
    section = task[_type]
    print(_type, section)
    users = [k for k in users_db]
    res = count_configured(users, today=False, section=section, _type=_type)


if __name__ == "__main__":
    fire.Fire(
        {
            "today": report_for_progress,
            "check_today": check_today,
            "check": report_for_user,
            "all": report_all_history,
            "update": report_all_update,
        }
    )
