def start_requests(**kwargs):
    web_site = "遵义市政府"

    web_site_url = "http://www.zunyi.gov.cn/zwgk/jcxxgk/flfg/zfl_63284/"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for page in range(3):
        page = f"_{page}.html" if page else ""
        url = f"http://www.zunyi.gov.cn/zwgk/jcxxgk/flfg/zfl_63284/index{page}.html"
        yield {"url": url, "page_rule_id": 10999, "hub_fields": hub_fields}


    web_site = "遵义市发改委"

    web_site_url = "http://fgw.zunyi.gov.cn/xxgk/zpfl/fgwj/dfxfg/"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for page in range(17):
        page = f"_{page}" if page else ""
        url = f"http://fgw.zunyi.gov.cn/xxgk/zpfl/fgwj/dfxfg/list{page}.html"
        yield {"url": url, "page_rule_id": 11001, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
