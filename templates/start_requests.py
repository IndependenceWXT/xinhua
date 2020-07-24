def start_requests(**kwargs):
    web_site = "日喀则市政府"

    web_site_url = "http://www.rkzszf.gov.cn/col/col93/index.html?number=42&uid=4275&pageNum=1"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for p in range(4):
        p = f"{p+1}" if p else "1"
        url = f"http://www.rkzszf.gov.cn/col/col93/index.html?number=42&uid=4275&pageNum={p}"
        yield {"url": url, "page_rule_id": 11510, "hub_fields": hub_fields}

    web_site = "日喀则发改委"

    web_site_url = "http://fgw.rkzszf.gov.cn/col/col901/index.html"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for p in range(3):
        p += 1
        url = f"http://fgw.rkzszf.gov.cn/col/col90{p}/index.html"
        yield {"url": url, "page_rule_id": 11512, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
