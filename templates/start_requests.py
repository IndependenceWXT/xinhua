def start_requests(**kwargs):
    web_site = "邯郸市政府"

    web_site_url = "http://hdzfxxgk.hd.gov.cn/zfwj/szfwj/"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for p in range(33):
        p = f"_{p}" if p else ""
        url = f"http://hdzfxxgk.hd.gov.cn/zfwj/szfwj/index{p}.html"
        yield {"url": url, "page_rule_id": 11574, "hub_fields": hub_fields}

    web_site = "邯郸市发改委"

    web_site_url = "http://www.hd.gov.cn/fgw/zwgk/yfxz/zcfg/"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for p in range(4):
        p = f"_{p}" if p else ""
        url = f"http://www.hd.gov.cn/fgw/zwgk/yfxz/zcfg/index{p}.html"
        yield {"url": url, "page_rule_id": 11576, "hub_fields": hub_fields}

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
        hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
        for p in range(pages):
            p = f"_{p}" if p else ""
            url = f""
            yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
