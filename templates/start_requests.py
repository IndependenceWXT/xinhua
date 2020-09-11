def start_requests(**kwargs):
    web_site = "交通运输部"

    web_site_url = "http://www.mot.gov.cn/zhengce/"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for p in range(67):
        p = f"_{p}" if p else ""
        url = f"http://xxgk.mot.gov.cn/2020/jigou/list{p}.html"
        yield {"url": url, "page_rule_id": 9888, "hub_fields": hub_fields}

    web_site_url = "http://www.mot.gov.cn/shuju/"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    yield {"url": web_site_url, "page_rule_id": 10052, "hub_fields": hub_fields}

    web_site_url = "http://www.mot.gov.cn/xinwen/"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}

    for page in range(30):
        page = f"_{page}" if page else ""
        url = f"http://www.mot.gov.cn/jiaotongyaowen/index{page}.html"
        yield {"url": url, "page_rule_id": 10058, "hub_fields": hub_fields}

    for page in range(2):
        page = f"_{page}" if page else ""
        url = f"http://www.mot.gov.cn/zhongyaohuiyi/index{page}.html"
        yield {"url": url, "page_rule_id": 10058, "hub_fields": hub_fields}

    for page in range(10):
        page = f"_{page}" if page else ""
        url = f"http://www.mot.gov.cn/difangxinwen/xxlb_fabu/index{page}.html"
        yield {"url": url, "page_rule_id": 10058, "hub_fields": hub_fields}

    for page in range(17):
        page = f"_{page}" if page else ""
        url = f"http://www.mot.gov.cn/guowuyuanxinxi/index{page}.html"
        yield {"url": url, "page_rule_id": 10058, "hub_fields": hub_fields}


def start_requests(**kwargs):
    source_type = 1
    copyright = 1
    web_site = "网站名"

    web_site_url = "栏目的链接"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for p in range(None):
        p = f"_{p}" if p else ""
        url = f"列表页链接然后修改为格式化字符串"
        yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}

    yield {"url": web_site_url, "page_rule_id": None, "hub_fields": hub_fields}

    url = ""
    for p in range(None):
        p = f"_{p}" if p else ""
        data = f""
        yield {
            "url": url,
            "page_rule_id": None,
            "data": data,
            "method": "POST",
            "hub_fields": hub_fields,
        }

    cates = [
        {"cate": "栏目链接的差异部分", "pages": None},
        {"cate": "栏目链接的差异部分", "pages": None},
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]
        web_site_url = f"栏目的链接格式化"
        hub_fields = {
            "web_site": web_site,
            "web_site_url": web_site_url,
            "source_type": source_type,
            "copyright": copyright,
        }
        for p in range(pages):
            p = f"_{p}" if p else ""
            url = f""
            yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
