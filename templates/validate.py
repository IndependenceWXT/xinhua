def validate_default(context):
    """
    校验器 返回Ture or False
    :param context:
        若为页面与校验器
            字典 {"url": url, "text": text, "status_code": 200, "original_url": "跳转前url", "headers": "响应headers"}
        若为字段校验器
            context为字段值（字符串）
    :return: bool
    """
    headers = context.get("headers")
    location = headers["Location"]
    if len(location.split("/")) > 6:
        return False
    return True


def validate_publish_time(context):
    """Version: 2020_07_11
    验证发布时间是否大于当前时间
    """
    from datetime import datetime

    if context.startswith("error:"):
        return False
    else:
        now = datetime.now()
        pt = datetime.strptime(context, "%Y-%m-%d %H:%M:%S")
        if pt > now:
            return False
        return True


def validate_author(context):
    """Version: 2020_07_18
    验证中文作者是否含有非法词
    """
    if context.startswith("error:"):
        raise ValueError(f"{context!r} author process failed")
        return False
    elif len(context) > 4:
        raise ValueError(f"{context!r} author length:{len(context)} overflow")
        return False
    return True


def validate_publish_org(context):
    """Version: 2020_07_18
    验证来源中是否有error: 
        卡住未经正确处理的请求
    """
    if context.startswith("error:"):
        return False
    elif len(context) > 15:
        return False
    return True


def validate_url(context):
    """Version: 2020_07_18
    验证链接是否合法
    """
    import re
    from urllib.parse import urlparse

    text = context.strip()
    # 调度中可能复制带了空格
    if len(text) != len(context):
        return False

    rules = [
        r"(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",
        r"@^(https?|ftp)://[^\s/$.?#].[^\s]*$@iS",
        r"#\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))#iS",
    ]
    for each in rules:
        p = re.compile(each)
        res = p.findall(text)
        if res:
            return True
    else:
        try:
            q = urlparse(text)
        except:
            return False
        else:
            if all([q.scheme, q.netloc, q.path]):
                return True
            else:
                return False


def validate_tag(context):
    """Version: 2020_08_11
    验证标签, 不同网站调整长度
    """
    import re
    import logging

    text = context.strip()
    if text.startswith("error:"):
        raise ValueError(f"tag extract failed: {text!r}")
        return False
    # 验证长度
    if len(text) > 10:
        raise ValueError(f"tag length {len(context)!r} overflow: {context!r}")
        return False
    return True


def validate_title(context):
    """Version: 2020_08_16
    验证标题是否是省略过的, 并且文本长度是否在100内
    """
    import re

    text = context.strip()
    length = len(re.sub(r"\s+", "", text))
    if text.endswith("...") or text.startswith("error:") or "&" in text:
        return False
    elif length > 150:
        return False
    return True


def validate_news_type(context):
    """Version: 2020_07_18
    验证新闻类型
    """
    if context.startswith("error:"):
        return False
    elif len(context) > 8:
        return False
    return True


def validate_web_site(context):
    """2020_07_13
    验证网站名是否复制带了空格
    """
    import re

    if len(context) == len(context.strip()):
        return True
    return False


def validate_source_type(context):
    """Version: 2020_07_18
    验证资源类型字段是否设置
    """
    if context in ["1", "2", "3", "4"]:
        return True
    else:
        return False


def validate_copyright(context):
    """Version: 2020_07_18
    验证版权字段是否设置
    """
    if context in ["0", "1"]:
        return True
    else:
        return False


def validate_hits(context):
    """Version: 2020_07_25
    验证点击量是否是整数
    """
    if context.isdigit():
        return True
    elif not context.startswith("error:"):
        return True
    return False


def validate_abstract(context):
    """Version: 2020_08_04
    验证摘要是否是完整的内容
    """
    import re

    text = context.strip()
    if text.endswith("..."):
        return False
    return True


def test_validators():
    # TODO: 测试验证器
    pass


if __name__ == "__main__":
    # print(validate_url("http:/10.40.35.103:8090/?a=1"))
    print(validate_url("http://www.wuhai.gov.cn/wuhai/xxgk4/jbxxgk46/813704/index.html"))
