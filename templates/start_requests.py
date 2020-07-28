def start_requests(**kwargs):
    from datetime import datetime, timedelta
    source_type = 1
    copyright = 0
    web_site = "西安日报"
    today = datetime.now().date()

    web_site_url = "http://epaper.xiancn.com/newxarb/html/2020-06/29/node_23.htm"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
        "publish_time": f"{today}"
    }
    
    month = today.strftime("%Y-%m")
    day = today.strftime("%d")
    url = f"http://epaper.xiancn.com/newxarb/html/{month}/{day}/node_23.htm"
    yield {"url": url, "page_rule_id": 12823, "hub_fields": hub_fields}



if __name__ == "__main__":
    for each in start_requests():
        print(each)
