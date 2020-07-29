def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "中国投融资担保股份有限公司"

    web_site_url = "http://www.guaranty.com.cn/gtztb/xwzx/mtbd/A050204index_1.htm?tab=3"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for p in range(4):
        p += 1
        url = f"http://www.guaranty.com.cn/gtztb/xwzx/mtbd/A050204index_{p}.htm?tab=3"
        yield {"url": url, "page_rule_id": 12914, "hub_fields": hub_fields}

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
