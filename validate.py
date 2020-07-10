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

    now = datetime.now()
    pt = datetime.strptime(context, "%Y-%m-%d %H:%M:%S")
    if pt > now:
        return False
    return True


def validate_author(context):
    """
    验证中文作者是否含有非法词
    """
    flags = ["记者", "撰文", "通讯员", "责任编辑", "编辑"]
    for each in flags:
        if each in context:
            return False
    else:
        if len(context) > 10 or len(context) < 2:
            return False
        return True


def validate_url(context):
    """验证链接是否合法"""
    # TODO: 用urllib.parse处理
    pass


def validate_publish_org(text):
    # TODO: 发布来源验证
    pass


if __name__ == "__main__":
    print(validate("2019-07-22 00:00:00"))
