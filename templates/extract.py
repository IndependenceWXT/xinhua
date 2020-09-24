import requests


def extract(context):
    """
    抽取函数
    :param context: 字典 {"url": url, "row": "当前行", "body": "当前页面"}
    :return: list 元素为字典
    """

    return []


def extract_from_script(context):
    """
    抽取函数
    :param context: 字典 {"url": url, "row": "当前行", "body": "当前页面"}
    :return: list 元素为字符串
    """
    import re
    text = context["body"]
    p = re.compile('<h1>.*?</h1>', re.DOTALL)
    res = p.findall(text)
    return res


if __name__ == "__main__":
    url = "https://www.chinanews.com/gn/2020/06-15/9212390.shtml"
    res = requests.get(url)
    print(res.text)
    context = {}
    context["body"] = res.text
    print(extract_from_script(context))
