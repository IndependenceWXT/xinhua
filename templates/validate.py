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
    """Version: 2020_07_17
    验证中文作者是否含有非法词
    """
    if context.startswith("error:"):
        return False
    elif len(context) > 4:
        return False
    return True


def validate_publish_org(context):
    """Version: 2020_07_11
    验证来源中是否有error: 
        卡住未经正确处理的请求
    """
    if context.startswith("error:"):
        return False
    return True


def validate_url(context):
    """Version: 2020_07_14
    验证链接是否合法
    """
    import re
    from urllib.parse import urlparse

    url = context.strip()
    # 调度中可能复制带了空格
    if len(url) != len(context):
        return False

    rules = [
        r"(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",
        r"@^(https?|ftp)://[^\s/$.?#].[^\s]*$@iS",
        r"#\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))#iS",
    ]
    for each in rules:
        p = re.compile(each)
        res = p.findall(url)
        if res:
            return True
    else:
        try:
            q = urlparse(url)
        except:
            return False
        else:
            if all([q.scheme, q.netloc, q.path]):
                return True
            else:
                return False


def validate_tag(context):
    """Version: 2020_07_12
    TODO: 验证标签, 不同网站调整长度, 测试一段时间
    """
    import re

    text = context.strip()
    if text.startswith("error:"):
        return False
    # 验证长度
    if len(text) > 5 or len(text) < 2:
        return False
    # 验证是否是含有非中文字符
    rules = [r"[\u4e00-\u9fa5]+"]
    for each in rules:
        p = re.compile(each)
        res = p.match(text)
        if res:
            if res[0] == text:
                return True
            else:
                return False
    else:
        return False


def validate_title(context):
    """Version: 2020_07_16
    验证标题是否是省略过的, 并且文本长度是否在区间内
    """
    import re
    
    text = context.strip()
    length = len(re.sub(r"\s+", "", text))
    if 100 > length > 2 and not text.endswith("..."):
        return True
    return False


def validate_news_type(context):
    """Version: 2020_07_11
    验证新闻类型
    """
    import re

    text = context.strip()
    # 验证长度
    if len(text) > 5 or len(text) < 2:
        return False

    rules = [r"[\u4e00-\u9fa5]+"]
    for each in rules:
        p = re.compile(each)
        res = p.match(text)
        if res:
            if res[0] == text:
                return True
            else:
                return False
    else:
        return False


def validate_web_site(context):
    """2020_07_13
    验证网站名是否复制带了空格
    """
    import re

    if len(context) == len(context.strip()):
        return True
    return False


def test_validators():
    # TODO: 测试验证器
    pass


if __name__ == "__main__":
    # print(validate_url("http:/10.40.35.103:8090/?a=1"))
    print(validate_tag(""))
