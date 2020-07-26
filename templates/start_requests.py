def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "乌鲁木齐市政府"

    web_site_url = "http://www.urumqi.gov.cn/info/nIndex.jsp?node_id=GKszf&cat_id=15282"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for p in range(4):
        p += 1
        url = f"http://www.wlmq.gov.cn/info/iList.jsp?isSd=false&node_id=GKszf&site_id=CMSurumqi&cat_id=15282&cur_page={p}"
        yield {"url": url, "page_rule_id": 10732, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
