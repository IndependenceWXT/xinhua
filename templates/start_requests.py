def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "新疆生产建设兵团-兵团胡杨网"

    web_site_url = "http://www.huyangnet.cn/node_50202.html"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for p in range(100):
        p = f"_{p+1}" if p else ""
        url = f"http://www.huyangnet.cn/node_50202{p}.html"
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
