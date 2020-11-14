def start_requests(**kwargs):
    from datetime import datetime, timedelta

    web_site = "外汇交易中心机构交易情况"
    source_type = 1
    copyright = 0
    web_site_url = "http://www.chinamoney.com.cn/chinese/mtdexorgtrade/"
    now = datetime.now()

    cates = [
        {"cate": "bondsSale", "web_site": "现券买卖分机构交易情况"},
        {"cate": "creditLend", "web_site": "同业拆借分机构交易情况"},
        {"cate": "pledgeRepurchase", "web_site": "质押式回购分机构交易情况"},
    ]
    for each in cates:
        cate = each["cate"]
        web_site = each["web_site"]
        hub_fields = {
            "web_site": web_site,
            "web_site_url": web_site_url,
            "source_type": source_type,
            "copyright": copyright,
        }
        date = now.strftime("%Y-%m-%d")
        url = f"http://www.chinamoney.com.cn/fe-c/{cate}SubsectorTranAction.do?method=showTable&searchDate={date}"
        yield {"url": url, "page_rule_id": 18430, "hub_fields": hub_fields}


if __name__ == "__main__":
    import json

    for each in start_requests():
        print(json.dumps(each, indent=4, ensure_ascii=False))
