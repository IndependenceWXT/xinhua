"""
TODO: 解析配置, 用新模板升级配置
    〇用新模板加载字段xpath和测试用例的备注链接
    10387无配置异常
    √ 输出其中字段配置的xpath, 功能还是可以试试的
    √ 输出测试用例中的备注和链接
"""
import requests
import json
from time import sleep
from pathlib import Path
import yaml
from pprint import pprint
import fire

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "username=fangtiansheng; remember_token=18|3c0e4afbacb93a873a5e93388b0a6d35159f2516fdb56dbfa8cc7a6454f01316b34e9e6721414c272430c7a2ffc426278ce8e2d5f3eaca3746afef6452167041; session=.eJw1zjFuwzAMQNG7cA4CkpJIy5cxJIpEO9gN5GQqevcYAbr-v7xf2GL6-QXrc778Btv3gBUallY1K7NIEUYehGZG7G30moUL5UgqoShNKgfVjOmayNjRsgw1X5JEteuZpbBmfWjC4gtJiqqSowYWasm1i1bybN2aKvEocEEePvd2-PH8p03ffe8-t9Pt5xgnrItkxDve4HVe-SOnBf7eKeQ93w.EZeaMw.rns4ayA-ciY47zFHl0q2lIfkUc0; baelish_username=fangtiansheng; baelish_remember_token=10|c0c87feee015ce01a645312214eaa4d8e50e9f905c30d61929069ae417101c4284ce5c92ce116f4b18d4e274e543100d3f5a8d77c6178ea575688cab1c382c89; baelish_session=.eJw1zjFuwzAMAMC_aA4KUpQo0p8xKIlEOtgt5GQq-vcGBbLedD9pj-XXPW2P9fRb2j9n2lIINRbrbIIUnVyBMmnXHoWJ2hx9NAIJEDJqNUqhVriiAOZpqOQ4qOFgVTCwyDWosmixOhWDW2md-1DBpjQ8Ss7VTTz7zBI1vSLfvg47_Xy8a8sPP7qv_fLxdc4rbcIF4ANu6Xm9-H-OkH7_AOphPRk.XrYUPw.IdH7ibUktSYBC9jsTRjMwFC_FaU",
    "DNT": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
}

proxies = {"http": None, "https": None}


def download_rule(rule_id):
    """
    根据页面规则编号下载配置yml
    """
    url = f"http://spider.vpc.shangjian.tech/crawl/crawl/rule/{rule_id}/"
    for i in range(5):
        try:
            print(f"[+]【{rule_id}】下载配置...")
            res = requests.get(url, headers=headers)
        except:
            print(f"[{i}]【{rule_id}】下载失败, 10秒后重试...")
            sleep(10)
            continue
        else:
            print(f"[+]【{rule_id}】下载完成")
            return res.json()["rule_yml"]
    else:
        print(f"[!]【{rule_id}】下载失败: 看看是不是泛采系统挂了...")
        return ""


def load_template():
    with open("新闻详情页配置模板.yml", mode="r", encoding="utf-8") as stream:
        text = stream.read()


def parse_yml(rule_id, text):
    """
    加载yml配置解析为python字典
    """
    if not text.strip():
        return
    try:
        print(f"[+]【{rule_id}】加载配置...")
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        print(f"[-]【{rule_id}】加载失败")
        pprint(exc)
    else:
        print(f"[+]【{rule_id}】加载成功, 转为python字典")
        return data


def filter_xpath(rule_id, data):
    """
    从解析好的python字典中获取字段的xpath配置
    """
    print(f"[+]【{rule_id}】开始过滤不需要的配置...")
    out_put_list = []

    rows = data["rows"] or []
    if not rows:
        print(f"[+]【{rule_id}】没有配置可用, 联系配置人员, 备注情况")
        return

    examples = data["examples"]

    for each in rows:
        row_name = each["name"]
        fields = each["fields"]
        links = each["links"]
        row_expression = each["expression"] if each["expression"] else "无"
        out_put_list.append(f"【{row_name}】行定位xpath:\n{row_expression}\n" + "_" * 100)

        for field in fields:
            field_name = field["name"]
            field_description = field["description"]
            locator = field["locator"]
            expression = field["expression"]
            if (
                not expression.strip()
                or locator != "xpath"
                or field_name.startswith("article_file_")
            ):
                continue
            out_put_list.append(
                f"\t【{field_name}:{field_description}】:\n{expression}\n" + "_" * 100
            )

        for link in links:
            page_rule_id = link["page_rule_id"]
            link_expression = link["expression"]
            out_put_list.append(
                f"\t【{row_name}】行新增链接解析到{page_rule_id}>:\n{link_expression}\n" + "_" * 100
            )

    for each in examples:
        url = each["url"]
        description = each["description"]
        if not url:
            continue
        out_put_list.append(f"【测试用例】:\n\n{url}\n" + "_" * 100)

    print("\n".join(out_put_list) + "\n")
    print(f"[+]【{rule_id}】过滤完成, 双击选中后右键复制需要的配置")


def main(rule_id):
    yml = download_rule(rule_id)
    data = parse_yml(rule_id, yml)
    filter_xpath(rule_id, data)


if __name__ == "__main__":
    fire.Fire(main)
