def start_requests(**kwargs):
    from datetime import datetime
    source_type = 1
    copyright = 0
    web_site = "成都日报"
    today = datetime.now().date()

    web_site_url = "http://www.cdrb.com.cn/epaper/cdrbpc/202006/28/l01.html"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
        "publish_time": f"{today}"
    }
    
    month = today.strftime("%Y%m")
    day = today.strftime("%d")
    url = f"http://www.cdrb.com.cn/epaper/cdrbpc/{month}/{day}/l01.html"
    yield {"url": url, "page_rule_id": 15952, "hub_fields": hub_fields}
    

if __name__ == "__main__":
    for each in start_requests():
        print(each)
