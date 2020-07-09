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
    print(query)
    if scheme in {"http", "https"}:
        return url
    else:
        if "s" in scheme:
            return urlunsplit(SplitResult("https", *[*query][1:]))
        else:
            return urlunsplit(SplitResult("http", *[*query][1:]))


def process_time_template(text):
    """时间提取脚本模版
    returns:
        9999: 正则匹配失败
        9404: xpath定位内容为空
    """
    import re

    rules = [
        r"\d{4}[-年/]\d{1,2}[-月/]\d{1,2}[-日/]?[\s\d{2}:\d{2}[:\d{2}]?]?",  # 常见中文日期格式
        r"",  # 如有不是常见的日期时间格式，此处替换成案例
    ]
    # 无内容时间返回空
    if not text.strip():
        return "9404"
    # 预处理，替换掉会影响正则提取的固定字符串
    flags = [""]
    for each in flags:
        text = text.replace(each, "")
    # 提取日期时间
    for each in rules:
        p = re.compile(each)
        res = p.findall(text)
        if res:
            return res[0]
        else:
            continue
    else:
        return "9999"


def process_time(text):
    """提取时间"""
    import re

    p = re.compile(r"\d{4}年\d{1,2}月\d{1,2}日\s\d{2}:\d{2}")
    p0 = re.compile(r"\d{4}-\d{1,2}-\d{1,2}\s\d{2}:\d{2}:\d{2}")
    p1 = re.compile(r"\w+\s\d{1,2},\s\d{4}")
    p2 = re.compile(r"\w+\s\d{4}")
    p3 = re.compile(r"\d{4}")
    if text.strip():
        res = p.findall(text)
        if res:
            return res[0]
        res = p0.findall(text)
        if res:
            return res[0]
        res = p1.findall(text)
        if res:
            return res[0]
        res = p2.findall(text)
        if res:
            return res[0]
        res = p3.findall(text)
        if res:
            return res[0]
    return ""


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


def process_author(text):
    """从有不同分隔符的作者字符串中提取人名：*请先去除非人名汉字*"""
    import re

    p = re.compile(r"([\u4e00-\u9fa5]+)")
    res = p.findall(text)
    return res


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


if __name__ == "__main__":
    # print(process_url("mailto:http://www.foeg.uzh.ch/analyse/politischekommunikation/news11/Sotomostudie.pdf"))
    # print(process_url_query("https://www.imemo.ru/en/index.php?page_id=502&id=484&p=60&ret=498"))
    # print(process("https://videos.aarp.org/detail/videos/all-videos/video/4117187433001/top-five-money-wasters?autoStart=true"))
    print(process_time_template("2019-5-19"))
    # print(process_text("27November2019"))
    # print(process_request("http://www.ebrd.com/cs/Satellite?c=Content&cid=1395242494713&pagename=EBRD%2FContent%2FDownloadDocument"))
    # text = """撰文：纪晓燕 龚丽欣 黄子慢"""
    # print(process_author(text))
    # print(process_time("May 16, 2002Economic and Social Research Institute"))
    # print(process_time_in_url("http://www.gjbmj.gov.cn/n1/2018/1217/c409082-30471818.html"))
