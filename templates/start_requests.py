def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "国家核安全局"
    cates = [
        {"cate": "zhxx_8953/yjzx", "pages": 46},
        {"cate": "zhxx_8953/gzdt", "pages": 100},
        {"cate": "zcfg_8964", "pages": 2},
        {"cate": "zcfg_8964/bz", "pages": 9},
        {"cate": "zhxx_8953/haqnb", "pages": 2},
        {"cate": "zcfg_8964/fg", "pages": 5},
        {"cate": "zcfg_8964/gh", "pages": 1},
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]
        web_site_url = f"http://nnsa.mee.gov.cn/{cate}/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
        for page in range(pages):
            page = f"_{page}" if page else ""
            url = f"http://nnsa.mee.gov.cn/{cate}/index{page}.html"
            yield {"url": url, "page_rule_id": 9944, "hub_fields": hub_fields}
def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "吐鲁番市人民政府"

    web_site_url = "http://www.tlf.gov.cn/zwgk/mlxxlb.jsp?a51t=7&a51p=1&a51c=2000&urltype=tree.TreeTempUrl&wbtreeid=6093"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    yield {"url": web_site_url, "page_rule_id": 10685, "hub_fields": hub_fields}

      

if __name__ == "__main__":
    for each in start_requests():
        print(each)
