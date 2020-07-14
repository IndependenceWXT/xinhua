def start_requests(**kwargs):
    web_site = "请替换此处为网站名"

    web_site_url = "请替换此处为栏目的链接"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for page in range(None):
        page = f"_{page}" if page else ""
        url = f"请替换此处为列表页链接然后修改为格式化字符串"
        yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}

    web_site = "请替换此处为网站名"

    web_site_url = "请替换此处为栏目的链接"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for page in range(None):
        page = f"_{page}" if page else ""
        url = f"请替换此处为列表页链接然后修改为格式化字符串"
        yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}

    yield {"url": web_site_url, "page_rule_id": None, "hub_fields": hub_fields}

    url = ""
    for page in range(None):
        page = f"_{page}" if page else ""
        data = f""
        yield {
            "url": url,
            "page_rule_id": None,
            "data": data,
            "method": "POST",
            "hub_fields": hub_fields,
        }

    cates = [
        {"cate": "请替换此处为栏目链接的差异部分", "pages": None},
        {"cate": "请替换此处为栏目链接的差异部分", "pages": None},
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]
        web_site_url = f"请替换此处为栏目的链接格式化"
        hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
        for page in range(pages):
            page = f"_{page}" if page else ""
            url = f""
            yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
