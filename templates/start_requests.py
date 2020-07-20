def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "新疆"

    cates = [
        {"cate": "xw/btdt", "catalog": "15206", "pages": 144},
        {"cate": "xw/btdt", "catalog": "15205", "pages": 294},
        {"cate": "xw/btdt", "catalog": "15207", "pages": 30},
        {"cate": "gk/zdgk/zcjd", "catalog": "15274", "pages": 15},
        {"cate": "gk/wjzc", "catalog": "36226", "pages": 35},
        {"cate": "gk/tjxx", "catalog": "15221", "pages": 3},
        {"cate": "gk/ghjh", "catalog": "15220", "pages": 3},
        {"cate": "gk/zdxm", "catalog": "15223", "pages": 3},
    ]
    for each in cates:
        cate = each["cate"]
        catalog = each["catalog"]
        pages = each["pages"]
        web_site_url = f"http://www.xjbt.gov.cn/{cate}/"
        hub_fields = {
            "web_site": web_site,
            "web_site_url": web_site_url,
            "source_type": source_type,
            "copyright": copyright,
        }
        for p in range(pages):
            p += 1
            url = f"http://www.xjbt.gov.cn/zcms/catalog/{catalog}/pc/index_{p}.shtml"
            yield {"url": url, "page_rule_id": 10516, "hub_fields": hub_fields}



if __name__ == "__main__":
    for each in start_requests():
        print(each)
