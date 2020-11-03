"""
用百度词法分析过滤测试库的author的所有值, 输出不是作者, 来源的元素
"""

from aip import AipNlp
from pprint import pprint

APP_ID = '21245238'
API_KEY = 'OMCn5VRMP0xt15wGdZhnxtev'
SECRET_KEY = 'wPQa0OC7bb14tSR9oGnIDIDlSzFL9ODa'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def check_author():
    with open("author.txt", mode="r", encoding="utf=8") as f:
        for line in f:
            text = line.strip()
            res = client.lexer(text)
            # pprint(res)
            if not res.get("items"):
                print(text)
                continue
            for each in res["items"]:
                if each["ne"] == "PER":
                    continue
            else:
                print(text)


def check_organization():
    with open("publish_org.txt", mode="r", encoding="utf=8") as f:
        for line in f:
            text = line.strip()
            res = client.lexer(text)
            # pprint(res)
            if not res.get("items"):
                print(text)
                continue
            for each in res["items"]:
                if each["ne"] == "ORG":
                    continue
            else:
                print(text)

if __name__ == '__main__':
    check_organization()


# text = "中国人民银行网站"
# res = client.lexer(text)
# pprint(res)