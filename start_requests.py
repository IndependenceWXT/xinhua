def start_requests(**kwargs):
    web_site = "吕梁市政府"

    web_site_url = "http://www.lvliang.gov.cn/llxxgk/zfxxgk/xxgkml/zcwj_21555/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url
    }
    for page in range(3):
        page = f"_{page}" if page else ""
        url = f"http://www.lvliang.gov.cn/llxxgk/zfxxgk/xxgkml/zcwj_21555/index{page}.html"
        yield {"url": url, "page_rule_id": 10576, "hub_fields": hub_fields}
    
    web_site = "吕梁市发改委"
    web_site_url = "http://www.lvliang.gov.cn/zfjgzd/llsfgw/zcfb/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url
    }
    for page in range(4):
        page = f"_{page}" if page else ""
        url = f"http://www.lvliang.gov.cn/zfjgzd/llsfgw/zcfb/index{page}.html"
        yield {"url": url, "page_rule_id": 10578, "hub_fields": hub_fields}

if __name__ == '__main__':
    for each in start_requests():
        print(each)
