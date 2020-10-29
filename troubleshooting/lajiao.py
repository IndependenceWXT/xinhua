def get_date(selector):
    # 提取日期
    from datetime import datetime

    date = selector.xpath('.//*[@class="td-time"]/text()[contains(., "-")]')[0]
    date = date.split("来源")[0].strip().split()[0]
    date = datetime.strptime(date, "%Y-%m-%d")
    year = date.year
    month = date.month
    day = date.day
    date = f"{year}/{month}/{day}"
    return date


def get_content(selector):
    # 提取正文文本
    d = selector.xpath('.//*[@id="content"]')[0]
    content = d.xpath("string(.)")
    return content


def fill(array):
    # 用前面的非空值填充后面的空值
    tmp = ""
    for i, each in enumerate(array):
        if each:
            tmp = each
        # None值不动
        elif each == "":
            array[i] = tmp
    return array


def parse_price(detail):
    # 解析价格详情
    import re

    name = detail.split("：")[0]
    price = re.sub(r"[\(（].*?[\)）]", "", detail.split("：")[-1])
    p = re.compile(r"(\w{1}/\w{1})")
    if "/" in price:
        res = p.findall(price)
        if res:
            unit = res[0]
        else:
            return
    else:
        return
    p = re.compile(r"(\d+\.\d+|\d+)")
    res = p.findall(price)
    if res:
        low = res[0]
    else:
        return
    high = res[-1] if len(res) > 1 else low
    p = re.compile(r"[\(（](.*?)[\)）]")
    level = p.findall(detail)
    item = {
        "name": name,
        "unit": unit,
        "low": low,
        "high": high,
        "level": level[0] if level else "",
    }
    return item


def pre_extract(content):
    import re

    return re.sub(r"([\u4e00-\u9fa5])\s([\u4e00-\u9fa5])", r"\1\2", content)


def extract(content):
    # 提取结构
    import re

    data = []
    # 表格化
    table = [
        [each for i, each in enumerate(line.split("\u3000"))]
        for line in content.split("\r\n")
        if "：" in line and not re.findall('\d{11}', line)
    ]
    # 价格信息
    width = max(len(i) for i in table)
    colums = []
    for c in range(width):
        # width=3, c: 0, 1
        # 最后一列不需要填充空值
        if c < width - 1:
            colum = fill([i[c] if len(i) > c else None for i in table])
            colums.append(colum)
        else:
            colums.append([i[c] if len(i) > c else None for i in table])
    table = list(zip(*colums))
    data = [each for each in table if None not in each]
    items = []
    for each in data:
        place = each[0]
        detail = each[-1]
        source = each[-2] if width > 2 else ""
        item = parse_price(detail)
        if not item:
            continue
        item["place"] = place.replace("：", "")
        item["source"] = source.replace("：", "")
        items.append(item)
    return items


def normalize(date, items):
    # 数据结构化
    for item in items:
        item["date"] = date
    return items


def process(text):
    from lxml import etree
    from datetime import datetime
    import json

    result = []
    selector = etree.HTML(text)
    date = get_date(selector)
    content = get_content(selector)

    content = pre_extract(content)

    items = extract(content)

    result = normalize(date, items)

    return json.dumps(result)


def main(url):
    import requests
    import json

    res = requests.get(url)
    result = process(res.text)
    data = json.loads(result)
    from pprint import pprint

    pprint(data)
    print(len(data))


if __name__ == "__main__":
    import fire

    # fire.Fire(main)
    main("http://www.e658.cn/jg/show-htm-itemid-91719.html")

