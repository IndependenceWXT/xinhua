def start_requests(**kwargs):
    web_site = "河北"

    web_site_url = "http://www.hebei.gov.cn/hebei/14462058/14471802/14471805/index.html"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    yield {"url": web_site_url, "page_rule_id": 10520, "hub_fields": hub_fields}

    web_site_url = "http://info.hebei.gov.cn/hbszfxxgk/6806024/6810698/index.html"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    yield {"url": web_site_url, "page_rule_id": 10869, "hub_fields": hub_fields}

    web_site_url = "http://info.hebei.gov.cn/eportal/ui?pageId=6817552"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for page in range(87):
        page += 1
        url = f"http://info.hebei.gov.cn/eportal/ui?currentPage={page}&pageId=6817552"
        yield {"url": url, "page_rule_id": 10890, "hub_fields": hub_fields}

    web_site_url = "http://www.hebei.gov.cn/hebei/14462058/14471802/14471750/index.html"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for page in range(2082):
        page += 1
        url = f"http://www.hebei.gov.cn/hebei/14462058/14471802/14471750/df829939/index{page}.html"
        yield {"url": url, "page_rule_id": 10890, "hub_fields": hub_fields}

    web_site_url = "http://www.hebei.gov.cn/hebei/14462058/14471802/14471756/index.html"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for page in range(3614):
        page += 1
        url = f"http://info.hebei.gov.cn/eportal/ui?currentPage={page}&pageId=6911774"
        yield {"url": url, "page_rule_id": 10890, "hub_fields": hub_fields}

    # 只有一条列表页
    yield {"url": web_site_url, "page_rule_id": None, "hub_fields": hub_fields}

    # 列表页分页为GET请求
    for page in range(None):
        page = f"_{page}" if page else ""
        url = f"请替换此处为列表页链接然后修改为格式化字符串"
        yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}

    # 列表页分页为POST请求: 请先尝试转换为GET方式是否可行
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

    # 栏目链接相似度较高的列表页
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
