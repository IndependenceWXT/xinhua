def start_requests(**kwargs):
    source_type = 1
    copyright = 1
    web_site = "长江网"

    web_site_url = "http://news.cjn.cn/ttdd/?spm=zm1066-001.0.0.1.oQ34W5"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for p in range(14):
        p = f"_{p}" if p else ""
        url = f"http://news.cjn.cn/ttdd/index{p}.htm"
        yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}

    web_site_url = "http://finance.cjn.cn/whjjzx/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for p in range(9):
        p = f"_{p}" if p else ""
        url = f"http://finance.cjn.cn/whjjzx/index{p}.htm"
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
