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
    """Version: 2020_07_13
    时间提取脚本模版
    """
    import re
    from datetime import datetime

    data = text.strip()

    rules = [
        r"(\d{2}\d{2}([\.\-/|年月\s]{1,3}\d{1,2}){2}日?(\s?\d{2}:\d{2}(:\d{2})?)?)|(\d{1,2}\s?(分钟|小时|天)前)",  # 常见中文日期格式, 网上找的
        # r"\d{10}",  # TODO: 处理时间戳, 遇到再加: 15开头的10或13位数字, 其实匹配前10个就够了
        r"",  # 如有不是常见的日期时间格式，此处替换成案例
    ]
    # 无内容时间返回空
    if not data:
        return "error:空字符串"
    # 预处理，替换掉会影响正则提取的固定字符串, 如点击量的数字
    flags = [""]
    for each in flags:
        data = data.replace(each, "")
    # 提取日期时间
    for each in rules:
        p = re.compile(each)
        res = p.findall(data)
        res = res and res[0] and res[0][0]
        if res:
            return res
        else:
            continue
    else:
        return f"error:{text}"


def process_time_test(text):
    """提取时间"""
    import re
    import dateparser

    post_time = "1999年06月30日 17:35:00"
    time_re = re.compile("[年月日\s]")
    ctime = dateparser.parse(time_re.sub(" ", text))
    print(ctime)


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
    """Version: 2020_07_12
    作者提取脚本模版
    returns:
        []: 正则匹配失败
    """
    import re

    # 按需排序
    rules = [
        r"\b([\u4e00-\u9fa5]\s?[\u4e00-\u9fa5]+)\b",  # 常见中文作者格式
        r"([a-zA-Z0-9]+)",  # 作者为字母和数字组合
        # r"",  # 如有不是常见的作者格式，此处替换成案例
    ]
    # 预处理，替换掉会影响正则提取的固定字符串, 从验证器中更新
    flags = ["作者", "记者", "撰文", "通讯员", "责任编辑", "编辑", "通讯中"]
    punctuations = ["【", "】", "（", "）"]
    flags.extend(punctuations)
    for each in flags:
        text = text.replace(each, "")

    # 判断是否是空作者
    author = text.strip()
    if len(author) < 2:
        return []

    # 提取作者
    for each in rules:
        p = re.compile(each)
        res = p.findall(author)
        if res:
            return [i.replace(" ", "") for i in res]
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
    """Version: 2020_07_12_16:23:00
    来源提取
    """
    import re

    # 预处理，替换掉会影响正则提取的固定字符串, 从验证器中更新
    flags = ["信息来源", "来源", "转自", "发文机关"]
    for each in flags:
        text = text.replace(each, "")

    # 来源为空
    if len(text.strip()) < 2:
        return ""

    # 按需排序
    rules = [
        r"([\u4e00-\u9fa5]+)",  # 默认提取中文, 其它格式卡住后处理
        # r"", # 自定义
        # r"([^\s/$.?].[^\s]*)", # www.railwaygazette.com
    ]

    # 提取来源
    for each in rules:
        p = re.compile(each)
        res = p.findall(text)
        if res:
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
        return res[0]
    else:
        return ""


def process_tag_template(text):
    """Version: 2020_07_12_19:10:00
    标签提取脚本模版
    returns:
        []: 正则匹配失败
    """
    import re

    tag = text.strip()

    # 按需排序
    rules = [
        r"\b([\u4e00-\u9fa5]+)\b",  # 连续中文字符
        # r"",  # 如有不是常见的作者格式，此处替换成案例
    ]
    # 无内容返回空列表
    if not tag:
        return []
    # 预处理，替换掉会影响正则提取的固定字符串, 从验证器中更新
    flags = ["标签", "关键字", "主题分类"]
    for each in flags:
        tag = tag.replace(each, "")
    # 提取作者
    for each in rules:
        p = re.compile(each)
        res = p.findall(tag)
        if res:
            return res
        else:
            continue
    else:
        return [f"error:{text}"]


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


# 计算content_md5, 数组字段去重, 不处理附件
import hashlib


def md5(text):
    return hashlib.md5(str(text).encode()).hexdigest()


def process(data):
    """Version: 2020_07_12
    计算 网站名 发布时间 标题 内容详情 的MD5
    """
    keys = ["web_site", "publish_time", "title", "content"]
    values = [data.get(k) or "" for k in keys]

    data["content_md5"] = md5("".join(values))
    # 数组字段去重, 去空
    if data.get("tag"):
        data["tag"] = list(set([tag for tag in data["tag"] if tag]))
    if data.get("author"):
        data["author"] = list(set([tag for tag in data["author"] if tag]))

    return data


def process_short_content(text):
    """Version: 2020_07_11_release
    处理短正文, 用了挺久了, 应该稳定可用了
    """
    import re

    if len(re.sub(r"\s+", "", text)) < 80:
        return ""
    return text


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
    print(process_author_template("（编辑：）"))
    # print(process_tag_template("主题分类：其他"))
