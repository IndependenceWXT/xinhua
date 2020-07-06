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


def validate(context):
    from datetime import datetime
    now = datetime.now()
    pt = datetime.strptime(context, "%Y-%m-%d %H:%M:%S")
    if pt > now:
        return False
    return True


if __name__ == '__main__':
    print(validate("2019-07-22 00:00:00"))
    