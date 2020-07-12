import hashlib


def md5(text):
    return hashlib.md5(str(text).encode()).hexdigest()


def process(data):
    """计算网站名发布时间标题内容详情的MD5"""
    print(data)
    data["content_md5"] = md5(
        data.get("web_site", "") + 
        data.get("publish_time", "") + 
        data.get("title", "") + 
        data.get("content", "") # 空字符串到这里会变成None
    )
    return data
