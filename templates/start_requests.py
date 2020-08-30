def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "遵义市政府"

    web_site_url = "http://www.zunyi.gov.cn/zwgk/jcxxgk/flfg/zfl_63284/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }

    cates = [
        {"cate": "http://www.zunyi.gov.cn/zwgk/jcxxgk/zcwj/zfl/index", "pages": 1},
        {"cate": "http://www.zunyi.gov.cn/zwgk/jcxxgk/zcwj/zff_5640672/index", "pages": 2},
        {"cate": "http://www.zunyi.gov.cn/zwgk/jcxxgk/zcwj/zfbf_5640673/index", "pages": 4},
        {"cate": "http://www.zunyi.gov.cn/zwgk/jcxxgk/zcwj/zfr_5640674/index", "pages": 6},
        {"cate": "http://www.zunyi.gov.cn/zwgk/jcxxgk/zcwj/szfqtwj/index", "pages": 2},
        {"cate": "http://www.zunyi.gov.cn/zwgk/jcxxgk/zcwj/wjbasc/index", "pages": 1},
        {"cate": "http://www.zunyi.gov.cn/zwgk/jcxxgk/zcwj/wjxgfz/index", "pages": 1},
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]

        for p in range(pages):
            p = f"_{p}" if p else ""
            url = cate + p + '.html'
            yield {"url": url, "page_rule_id": 10999, "hub_fields": hub_fields}


    web_site = "遵义市发改委"

    web_site_url = "http://fgw.zunyi.gov.cn/xxgk/zpfl/fgwj/dfxfg/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }

    for page in range(17):
        page = f"_{page}" if page else ""
        url = f"http://fgw.zunyi.gov.cn/xxgk/zpfl/fgwj/dfxfg/list{page}.html"
        yield {"url": url, "page_rule_id": 11001, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
