import os
import json
from urllib.parse import urlsplit, urlunsplit, urljoin, SplitResult, parse_qs, urlencode
import re
import requests
import time
from dateutil.parser import parse as datetime_parse


def process_url(text):
    """规范化非法url"""
    import re
    from urllib.parse import urlsplit, urlunsplit, urljoin, SplitResult, parse_qs, urlencode

    p = re.compile(r"(https?:.*\.pdf)")
    url = p.findall(text)[0]
    query = urlsplit(url)

    scheme = query.scheme
    if scheme in {"http", "https"}:
        return url
    else:
        if "s" in scheme:
            return urlunsplit(SplitResult("https", *[*query][1:]))
        else:
            return urlunsplit(SplitResult("http", *[*query][1:]))


def process_time_template(text):
    """Version: 2020_07_25
    时间提取脚本模版
    """
    import re
    from datetime import datetime

    text = text.strip()

    rules = [
        r"(\d{2}\d{2}([\.\-/|年月\s]{1,3}\d{1,2}){2}日?(\s?\d{1,2}:\d{1,2}(:\d{1,2})?)?)|(\d{1,2}\s?(分钟|小时|天|周)前)|昨天|前天",  # 常见中文日期格式, 网上找的
        # r"\d{10}",  # 处理时间戳, 遇到再加: 15开头的10或13位数字, 其实匹配前10个就够了
        # r"",  # 如有不是常见的日期时间格式，此处替换成案例
    ]
    # 预处理，替换掉会影响正则提取的固定字符串, 如点击量的数字
    if "-" in text:
        text = "2020-" + text
    flags = [
        "发布时间",
    ]
    for each in flags:
        text = text.replace(each, "")
    # 无内容时间返回空
    length = len(re.sub(r"\s+", "", text))
    if length < 2:
        return f"error:{text}"
    # 提取日期时间
    for each in rules:
        p = re.compile(each)
        res = p.findall(text)
        if res:
            res = sorted([i for i in res[0]], key=len, reverse=True)
            return parse(res[0])
        else:
            continue
    else:
        return f"error:{text}"


def get_current_date(date_format="%Y-%m-%d %H:%M:%S"):
    import datetime

    return datetime.datetime.now().strftime(date_format)


def parse(text):
    import re
    import datetime

    release_time = text.strip()

    if "年前" in release_time:
        years = re.compile(r"(\d+)年前").findall(release_time)
        years_ago = datetime.datetime.now() - datetime.timedelta(days=int(years[0]) * 365)
        release_time = years_ago.strftime("%Y-%m-%d %H:%M:%S")

    elif "月前" in release_time:
        months = re.compile(r"(\d+)月前").findall(release_time)
        months_ago = datetime.datetime.now() - datetime.timedelta(days=int(months[0]) * 30)
        release_time = months_ago.strftime("%Y-%m-%d %H:%M:%S")

    elif "周前" in release_time:
        weeks = re.compile(r"(\d+)周前").findall(release_time)
        weeks_ago = datetime.datetime.now() - datetime.timedelta(days=int(weeks[0]) * 7)
        release_time = weeks_ago.strftime("%Y-%m-%d %H:%M:%S")

    elif "天前" in release_time:
        ndays = re.compile(r"(\d+)天前").findall(release_time)
        days_ago = datetime.datetime.now() - datetime.timedelta(days=int(ndays[0]))
        release_time = days_ago.strftime("%Y-%m-%d %H:%M:%S")

    elif "小时前" in release_time:
        nhours = re.compile(r"(\d+)小时前").findall(release_time)
        hours_ago = datetime.datetime.now() - datetime.timedelta(hours=int(nhours[0]))
        release_time = hours_ago.strftime("%Y-%m-%d %H:%M:%S")

    elif "分钟前" in release_time:
        nminutes = re.compile(r"(\d+)分钟前").findall(release_time)
        minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=int(nminutes[0]))
        release_time = minutes_ago.strftime("%Y-%m-%d %H:%M:%S")

    elif "昨天" in release_time or "昨日" in release_time:
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        release_time = release_time.replace("昨天", str(yesterday))

    elif "今天" in release_time:
        release_time = release_time.replace("今天", get_current_date("%Y-%m-%d"))

    elif "刚刚" in release_time:
        release_time = get_current_date()

    elif re.search(r"^\d\d:\d\d", release_time):
        release_time = get_current_date("%Y-%m-%d") + " " + release_time

    elif not re.compile(r"\d{4}").findall(release_time):
        month = re.compile(r"\d{1,2}").findall(release_time)
        if month:
            if int(month[0]) <= int(get_current_date("%m")):
                release_time = get_current_date("%Y") + "-" + release_time
            else:
                release_time = str(int(get_current_date("%Y")) - 1) + "-" + release_time

    return release_time


def process_timestamp(text):
    "时间戳转字符串"
    from datetime import datetime

    return datetime.fromtimestamp(int(text)).strftime("%Y-%m-%d %H:%M:%S")


def process_title_from_url(text):
    from urllib.parse import unquote

    return unquote(text)


def process_url_query(text):
    """url参数过滤：处理url参数不同但页面相同的情况"""
    from urllib.parse import urlsplit, urlunsplit, SplitResult, parse_qs, urlencode

    res = urlsplit(text)
    query = parse_qs(res.query)
    query = {k: v[0] for k, v in query.items() if k not in ["p", "ret"]}
    return urlunsplit(SplitResult(*res[:3], urlencode(query), *res[4:]))


def process_request(text):
    """
    处理会跳转的链接：在列表页新链接处理器中处理得到跳转后的真实链接地址
    修改site_root
    """
    import pycurl
    from urllib.parse import urljoin
    from io import BytesIO

    buffer = BytesIO()
    ch = pycurl.Curl()
    url = urljoin("site_root", text)
    url = url.replace("http://", "https://")
    ch.setopt(ch.URL, url)
    ch.setopt(ch.WRITEDATA, buffer)
    ch.setopt(ch.SSL_VERIFYPEER, 0)
    ch.setopt(ch.SSL_VERIFYHOST, 2)
    # ch.setopt(ch.FOLLOWLOCATION, True) # 设置是否跳转
    ch.perform()
    try:
        new_url = ch.getinfo(ch.REDIRECT_URL)
    except:
        return url
    else:
        if new_url.endswith(".pdf") or "cnn.com" in new_url or "facebook.com" in new_url:
            return "search_link" + new_url
        else:
            return new_url


def process_time_ambiguous(text):
    "歧义时间格式08/03/2019"
    parts = text.split("/")
    parts = reversed(parts)
    return "/".join(parts)


def process_author_template(text):
    """Version: 2020_07_21
    作者提取脚本模版
    returns:
        [error:text]: 正则提取失败
        []: 无作者
    """
    import re

    # 按需排序
    rules = [
        r"\b([\u4e00-\u9fa5]\s?[\u4e00-\u9fa5]+)\b",  # 常见中文作者格式
        r"([a-zA-Z0-9]+)",  # 作者为字母和数字组合
        # r"",  # 如有不是常见的作者格式，此处替换成案例
    ]
    # 预处理，替换掉会影响正则提取的固定字符串, 从验证器中更新
    text = text.replace("  ", " ")
    flags = ["作者", "记者", "撰文", "通讯员", "责任编辑", "编辑", "通讯中", "发布者"]
    punctuations = ["【", "】", "（", "）"]
    flags.extend(punctuations)
    for each in flags:
        text = text.replace(each, "")
    # 无作者
    if len(re.sub(r"\s+", "", text)) < 2:
        return []
    # 提取作者
    for each in rules:
        p = re.compile(each)
        res = p.findall(text)
        if res:
            return [i.replace(" ", "") for i in res if 1 < len(i) < 5]
        else:
            continue
    else:
        return [f"error:{text}"]


def process_author_test(text):
    """Version: 2020_07_11
    从有不同分隔符的作者字符串中提取人名：
        *请先去除非人名汉字*:
        记者, 撰文, 编辑, 责任编辑等
    """
    import re

    p = re.compile(r"([\u4e00-\u9fa5]+)")
    res = p.findall(text)
    return res


def process_publish_org_template(text):
    """Version: 2020_07_18
    来源提取
    """
    import re

    # 按需排序
    rules = [
        r"([\u4e00-\u9fa5]+)",  # 默认提取中文, 其它格式卡住后处理
        # r"", # 自定义
        # r"([^\s/$.?].[^\s]*)", # www.railwaygazette.com
    ]
    # 预处理，替换掉会影响正则提取的固定字符串, 从验证器中更新
    flags = ["文章来源", "信息来源", "文字来源", "来源", "转自", "发文机关", "发布人", "发布者"]
    for each in flags:
        text = text.replace(each, "")
    # 来源为空
    if len(re.sub(r"\s+", "", text)) < 2:
        return ""
    # 提取来源
    for each in rules:
        p = re.compile(each)
        res = p.findall(text)
        if res:
            res = sorted(res, key=len, reverse=True)
            return res[0]
        else:
            continue
    else:
        return f"error:[{text}]"


def process_publish_org_test(text):
    """
    去掉flag中文字符后用正则提取组织
    """
    import re

    p = re.compile(r"([\u4e00-\u9fa5]+)")
    # p = re.compile(r"([\w]+)")
    res = p.findall(text)
    if res:
        return res
    else:
        return ""


def process_tag_template(text):
    """Version: 2020_07_18
    标签提取脚本模版
    returns:
        []: 无
        ["error:text"]: 提取失败
    """
    import re

    text = text.strip()
    # 按需排序
    rules = [
        r"\b([\u4e00-\u9fa5]+)\b",  # 连续中文字符
        r"\w+",  # 如有不是常见的格式，此处替换成案例
    ]
    # 预处理，替换掉会影响正则提取的固定字符串, 从验证器中更新
    flags = ["标签", "关键字", "主题分类"]
    for each in flags:
        text = text.replace(each, "")
    # 无内容返回空列表
    if len(re.sub(r"\s+", "", text)) < 2:
        return []
    # 提取
    for each in rules:
        p = re.compile(each)
        res = p.findall(text)
        if res:
            return res
        else:
            continue
    else:
        return [f"error:{text}"]


def process_news_type_template(text):
    """Version: 2020_07_14
    来源新闻类型
    """
    import re

    # 为空
    if len(text.strip()) < 2:
        return ""

    # 按需排序
    rules = [
        r"([\u4e00-\u9fa5]+)",  # 默认提取中文, 其它格式卡住后处理
        # r"", # 自定义
        # r"([^\s/$.?].[^\s]*)", # www.railwaygazette.com
    ]

    # 提取
    for each in rules:
        p = re.compile(each)
        res = p.findall(text)
        if res:
            return res[0]
        else:
            continue
    else:
        return f"error:[{text}]"


def update_url_query(text, **kwargs):
    from urllib.parse import urlsplit, urlunsplit, SplitResult, parse_qs, urlencode

    res = urlsplit(text)
    query = parse_qs(res.query)
    query = {k: v[0] for k, v in query.items()}
    query.update(kwargs)
    return urlunsplit(SplitResult(*res[:3], urlencode(query), *res[4:]))


def process_time_in_url(text):
    import re

    p = re.compile(r"/(?P<year>\d{4})/(?P<month>\d{2})(?P<day>\d{2})/")
    res = p.findall(text)
    if res:
        return "-".join(res[0])
    return ""


def process_title_template(text):
    """Version: 2020_07_18
    处理标题，取一个稍微小的平均的标题长度
    """
    import re

    if len(re.sub(r"\s+", "", text)) < 2:
        return f"error:{text}"
    return text


# 计算content_md5, 数组字段去重
import hashlib
from itertools import zip_longest


def md5(text):
    return hashlib.md5(str(text).encode()).hexdigest()


def process(data):
    """Version: 2020_07_18
    - 计算 网站名 发布时间 标题 内容详情 的MD5
    - 数组字段去重复
    """
    keys = ["web_site", "publish_time", "title", "content"]
    values = [data.get(k) or "" for k in keys]

    data["content_md5"] = md5("".join(values))
    # 数组字段去重, 去空
    if data.get("tag"):
        data["tag"] = list(set([tag for tag in data["tag"] if tag]))
    if data.get("author"):
        data["author"] = list(set([author for author in data["author"] if author]))
    # 附件根据链接去重复
    dedup = {}
    for filename, url in zip_longest(
        data["article_file_name"], data["article_file_url"], fillvalue=""
    ):
        filename = filename or ""
        if not dedup.get(url) or len(filename) > len(url):
            dedup[url] = filename
    else:
        data["article_file_name"] = [v for k, v in dedup.items()]
        data["article_file_url"] = [k for k, v in dedup.items()]

    return data


def process_files(filenames, links):
    data = {}
    for filename, link in zip(filenames, links):
        if not data.get(link) and len(filename) > len(data.get(link)):
            data[link] = filename
    else:
        return [v for k, v in data.items()], [k for k, v in data.items()]


def process_short_content(text):
    """Version: 2020_07_23
    返回的html，提取其文字内容
    短正文置空处理
    """
    import re
    from lxml import etree

    root = etree.HTML(text)
    text = root.xpath("string(.)")
    if len(re.sub(r"\s+", "", text)) < 80:
        return ""
    return text


def process_hits(text):
    """Version: 2020_07_25
    提取点击量数字
    """
    import re

    p = re.compile(r"(\d+)")
    res = p.findall(text)
    if res:
        return res[0]
    else:
        return f"error:{text}"


def process_hits_test(text):
    """Version: 2020_07_26
    测试库不开启浏览器下载，忽略采集点击量验证
    上线需删除
    """
    return "0" if text.startswith("error:") else text


def check_publish_org():
    with open("publish_org.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            text = line.strip()
            res = process_publish_org_template(text)
            print(f"/{res}/")


def check_author():
    with open("author.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            text = line.strip()
            res = process_author_template(text)
            print(f"/{res}/")

def process_article_file_name(text):
    """Version: 2020_08_04
    文件名处理，提取链接中的文件名
    """
    if text.endswith(".mp4"):
        return text.split("/")[-1]
    return text

def process_dem_json(text):
    import demjson
    import json
    data = demjson.decode(text, encoding="unicode")
    res = []
    for each in data["list"]:
        item = {
            "columnName": each["columnName"],
            "desc": each["desc"],
            "time": each["time"],
            "title": each["title"],
            "titleLink": each["titleLink"],
        }
    return data

if __name__ == "__main__":
    # print(process_url("mailto:http://www.foeg.uzh.ch/analyse/politischekommunikation/news11/Sotomostudie.pdf"))
    # print(process_url_query("https://www.imemo.ru/en/index.php?page_id=502&id=484&p=60&ret=498"))
    # print(process("https://videos.aarp.org/detail/videos/all-videos/video/4117187433001/top-five-money-wasters?autoStart=true"))
    # print(process_time_test("1999年06月30日 17:35:00"))
    # print(process_time_template("2020-06-30 17:35"))
    # print(process_text("27November2019"))
    # print(process_request("http://www.ebrd.com/cs/Satellite?c=Content&cid=1395242494713&pagename=EBRD%2FContent%2FDownloadDocument"))
    # text = """撰文：纪晓燕 龚丽欣 黄子慢"""
    # print(process_author(text))
    # print(process_time("May 16, 2002Economic and Social Research Institute"))
    # print(process_time_in_url("http://www.gjbmj.gov.cn/n1/2018/1217/c409082-30471818.html"))
    # print(process_author("(：test2)"))
    # print(process_author_template("（编辑：）"))
    # print(process_tag_template("主题分类：其他"))
    # print(process_publish_org_template("来源 中关村"))
    # print(process_time_template("2017/1/11 9:12:55"))
    # import requests
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    # }
    # url = "http://roll.hexun.com/roolNews_listRool.action?type=all&ids=100,101,103,125,105,124,162,194,108,122,121,119,107,116,114,115,182,120,169,170,177,180,118,190,200,155,130,117,153,106&page=493&tempTime="

    # res = requests.get(url, headers=headers)
    # print(
    #     process_dem_json(res.text)
    # )
    print(process_time_template("08-13"))

