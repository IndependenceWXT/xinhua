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
    web_site = "民政部"

    web_site_url = "http://xxgk.mca.gov.cn:8011/gdnps/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for page in range(139):
        page += 1
        url = f"http://xxgk.mca.gov.cn:8011/gdnps/searchIndex.jsp?params=%257B%2522goPage%2522%253A{page}%252C%2522doRepeated%2522%253A1%252C%2522orderBy%2522%253A%255B%257B%2522orderBy%2522%253A%2522scrq%2522%252C%2522reverse%2522%253Atrue%257D%252C%257B%2522orderBy%2522%253A%2522orderTime%2522%252C%2522reverse%2522%253Atrue%257D%255D%252C%2522pageSize%2522%253A15%252C%2522queryParam%2522%253A%255B%257B%2522shortName%2522%253A%2522ownSubjectDn%2522%252C%2522value%2522%253A%2522%252F1%252F3%252F102%2522%257D%252C%257B%2522shortName%2522%253A%2522fbjg%2522%252C%2522value%2522%253A%2522%252F1%252F3%252F102%2522%257D%252C%257B%257D%252C%257B%257D%252C%257B%257D%255D%257D&callback=jQuery&_="
        yield {"url": url, "page_rule_id": 9864, "hub_fields": hub_fields}

    web_site_url = "http://www.mca.gov.cn/article/xw/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    cates = [
        {"cate": "tt", "pages": 32},
        {"cate": "mzyw", "pages": 57},
        {"cate": "tzgg", "pages": 31},
        {"cate": "ywdt", "pages": 37},
        {"cate": "dfdt", "pages": 100},
        {"cate": "mtbd", "pages": 100},
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]
        for page in range(pages):
            page += 1
            page = page if page != 1 else ""
            url = f"http://www.mca.gov.cn/article/xw/mtbd/?{page}"
            yield {"url": url, "page_rule_id": 9865, "hub_fields": hub_fields}

    web_site_url = "http://www.mca.gov.cn/article/gk/jd/shzzgl/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for page in range(2):
        page += 1
        page = page if page != 1 else ""
        url = f"http://www.mca.gov.cn/article/gk/jd/shzzgl/?{page}"
        yield {"url": url, "page_rule_id": 10001, "hub_fields": hub_fields}




if __name__ == "__main__":
    for each in start_requests():
        print(each)
