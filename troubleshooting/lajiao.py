def remove_lines(text):
    # 预处理：去除非数据块
    text = "\r\n\r\n".join([i for i in text.split("\r\n\r\n") if "【" not in i and "中国辣椒网诚招全国各产区辣椒报价员" not in i])
    return text


def remove_empty_lines(text):
    # 预处理：去除空行
    while 1:
        if "\r\n\r\n\u3000" in text:
            text = text.replace("\r\n\r\n\u3000", "\r\n\u3000")
        else:
            return text


def split_places(text):
    # 分割数据块
    return text.split("\r\n\r\n")


def remove_contact(text):
    # 去除联系方式
    return "\r\n\r\n".join(["\r\n".join(i.split("\r\n")[:-2]) for i in text.split("\r\n\r\n")])


def extract_price(detail):
    # 解析价格详情
    import re
    name = detail.split("：")[0]
    price = re.sub(r"[\(（].*?[\)）]", "", detail.split("：")[-1])
    p = re.compile(r'(\w{1}/\w{1})')
    if "/" in price:
        res = p.findall(price)
        if res:
            unit = res[0]
    p = re.compile(r'(\d+\.\d+|\d+)')
    res = p.findall(price)
    low = res[0]
    high = res[-1] if len(res)>1 else low
    p = re.compile(r'[\(（](.*?)[\)）]')
    level = p.findall(detail)
    item = {
        "name": name,
        "unit": unit,
        "low": low,
        "high": high,
        "level": level[0] if level else ""
    }
    return item

def extract_2_level(place, tops, details):
    # 解析两层数据
    items = []
    top = None
    for line in place.split("\r\n"):
        if line.strip() in tops:
            top = line.strip()
        else:
            detail = line.strip()
            if "备注" in detail or "：" not in detail:
                continue
            item = extract_price(detail)
            item["place"] = top.replace("：", "")
            item["source"] = ""
            items.append(item)
    return items


def extract_3_level(place, tops, subs, details):
    # 解析三层数据
    items = []
    top = None
    sub = None
    for line in place.split("\r\n"):
        if line.strip() in tops:
            top = line.strip()
        elif line.strip() in subs:
            sub = line.strip()
        else:
            detail = line.strip()
            if "备注" in detail or "：" not in detail:
                continue
            item = extract_price(detail)
            item["place"] = top.replace("：", "")
            item["source"] = sub.replace("：", "")
            items.append(item)
    return items

def extract(place, tops, subs, details):
    if details:
        return extract_3_level(place, tops, subs, details)
    else:
        return extract_2_level(place, tops, subs)


def process(text):
    from lxml import etree
    from datetime import datetime
    import json

    s = etree.HTML(text)
    # 提取文字保留换行和空格
    res = []
    date = s.xpath('.//*[@class="td-time"]/text()[contains(., "-")]')[0]
    date = date.split("来源")[0].strip().split()[0]
    date = datetime.strptime(date, "%Y-%m-%d")
    year = date.year
    month = date.month
    day = date.day
    date = f"{year}/{month}/{day}"

    d = s.xpath('.//*[@id="content"]')
    text = d[0].xpath('string(.)').strip()
    normalizers = [remove_lines, remove_empty_lines]

    for each in normalizers:
        text = each(text)

    places = split_places(text)
    for place in places:
        place = remove_contact(place)
        tops = [i for i in place.strip().split("\r\n") if (not i.startswith("\u3000")) and i]
        subs = [i for i in place.strip().split("\r\n\u3000") if (not i.startswith("\u3000")) and i and (i not in tops) and "：" in i]
        details = [i for i in place.strip().split("\r\n\u3000\u3000") if (not i.startswith("\u3000")) and i and (i not in tops or i not in subs) and "\r\n" not in i]
        data = extract(place, tops, subs, details)
        res.extend(data)
    result = []
    for i in res:
        i["date"] = date
        result.append(i)
    return json.dumps(result, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    import requests
    url = "http://www.e658.cn/jg/show-htm-itemid-91658.html"
    res = requests.get(url)
    print(process(res.text))
    
