def start_requests(**kwargs):
    web_site = "无锡市政府"

    web_site_url = "http://www.wuxi.gov.cn/zfxxgk/szfxxgkml/fgwjjjd/index.shtml"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url
    }
    for page in range(250):
        page = f"_{page+1}" if page else ""
        url = f"http://www.wuxi.gov.cn/zfxxgk/szfxxgkml/fgwjjjd/index{page}.shtml"
        yield {"url": url, "page_rule_id": 10713, "hub_fields": hub_fields}
    
    web_site = "无锡市发改委"
    web_site_url = "http://dpc.wuxi.gov.cn/zfxxgk/xxgkml/fgwjjjd/index.shtml"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url
    }
    for page in range(11):
        page = f"_{page+1}" if page else ""
        url = f"http://dpc.wuxi.gov.cn/zfxxgk/xxgkml/fgwjjjd/index{page}.shtml"
        yield {"url": url, "page_rule_id": 10715, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
