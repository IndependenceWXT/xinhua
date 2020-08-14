import requests


def extract(context):
    """
    抽取函数
    :param context: 字典 {"url": url, "row": "当前行", "body": "当前页面"}
    :return: list 元素为字典
    """

    return []


def extract_from_script(context):
    import re

    p = re.compile(r"urls\[i\]='(.*?)'")
    body = context["body"]
    res = p.findall(body)
    if res:
        return res


if __name__ == "__main__":
    url = "http://www.fuzhou.gov.cn/was5/web/search?channelid=290792&templet=advsch.jsp&sortfield=-docorderpri%2C-docreltime&classsql=chnlid%3D5727&random=0.653659668892808&prepage=10&page=3"
    res = requests.get(url)
    print(res.text)
    context = {}
    context["body"] = res.text
    print(extract_from_script(context))
