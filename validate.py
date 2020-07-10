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
    """验证发布时间是否大于当前时间"""
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
    """
    验证中文作者是否含有非法词
    """
    if context.startswith("error:"):
        return False
    elif len(context) > 4 or len(context) < 2:
        return False
    return True


def validate_publish_org(context):
    """
    验证来源中是否有error: 
        卡住未经正确处理的请求
    """
    if context.startswith("error:"):
        return False
    return True


def validate_url(context):
    """验证链接是否合法"""
    import re
    from urllib.parse import urlparse

    url = context.strip()
    rules = [
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


if __name__ == "__main__":
    print(validate_url("http:/10.40.35.103:8090/?a=1"))
