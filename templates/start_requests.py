def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "中融信托"

    web_site_url = "http://zritc.com.cn/aboutzr/gsxw/"
    cates = [
        {"cate": "qcbxzs", "pages": 2495},
        {"cate": "rsbxzs", "pages": 2036},
        {"cate": "jtbxzs", "pages": 723},
        {"cate": "lxbxzs", "pages": 660},
        {"cate": "ylbxzs", "pages": 2223},
        {"cate": "lcbxzs", "pages": 2064},
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]
        hub_fields = {
            "web_site": web_site,
            "web_site_url": web_site_url,
            "source_type": source_type,
            "copyright": copyright,
        }
        for p in range(1):
            p = f"_{p}" if p else ""
            url = f"http://www.cpic.com.cn/zixun2/{cate}/index{p}.shtml"
            yield {"url": url, "page_rule_id": 13100, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
