import requests
import json

def field(url):
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "DNT": "1",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4315.4 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://www.chinamoney.com.cn",
        "Referer": "http://www.chinamoney.com.cn/chinese/mtmoncjgl/",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    records = data["records"]
    fields = records[0].keys()
    return list(fields)


if __name__ == '__main__':
    url = "http://www.chinamoney.com.cn/dqs/rest/dqs-u-currency/OrMthBltn?lang=cn&empty=-1&indexType=btvo&yearMonth=202009"
    fields = field(url)
    fields = sorted(fields)
    print(json.dumps(fields))
    lines = []
    for each in fields:
        line = f"  `{each}` varchar(255) DEFAULT NULL COMMENT '{each}',"
        lines.append(line)
    res = "\n".join(lines)

    print(res)
