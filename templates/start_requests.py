def start_requests(**kwargs):
    from datetime import datetime, timedelta

    now = datetime.now()
    web_site = "外汇交易中心统计月报-成交概览"
    source_type = 1
    copyright = 0

    web_site_url = "http://www.chinamoney.com.cn/chinese/mtmoncjgl/"

    # 外汇交易中心统计月报-成交概览_按交易品种
    cates = [
        {
            "cate": "dqs-u-currency/IblMthBltn?lang=cn&empty=-1&indexType=tvvo&yearMonth=",
            "web_site": "同业拆借月报",
        },
        {
            "cate": "dqs-u-currency/PrMthBltn?lang=cn&empty=-1&indexType=tvvo&searchDate=",
            "web_site": "质押式回购月报",
        },
        {
            "cate": "dqs-u-currency/OrMthBltn?lang=cn&empty=-1&indexType=tvvo&yearMonth=",
            "web_site": "买断式回购月报",
        },
        {"cate": "dqs-u-bond/BdcMthBltn?lang=cn&indexType=pro&yearMonth=", "web_site": "债券借贷月报"},
    ]
    for each in cates:
        cate = each["cate"]
        web_site = each["web_site"]
        for i in range(31):
            hub_fields = {
                "web_site": web_site,
                "web_site_url": web_site_url,
                "source_type": source_type,
                "copyright": copyright,
            }
            day = now + timedelta(days=-1 * i)
            date = day.strftime("%Y-%m-%d")
            url = f"http://www.chinamoney.com.cn/dqs/rest/{cate}{date}"
            yield {"url": url, "page_rule_id": 18433, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_按机构类别交易统计
    cates = [
        {
            "cate": "http://www.chinamoney.com.cn/dqs/rest/dqs-u-currency/IblMthBltn?lang=cn&empty=-1&yearMonth=202008&indexType=ittvo",
            "web_site": "同业拆借月报",
        },
        {
            "cate": "http://www.chinamoney.com.cn/dqs/rest/dqs-u-currency/PrMthBltn?lang=cn&empty=-1&searchDate=202009&indexType=pitvo",
            "web_site": "质押式回购月报",
        },
        {
            "cate": "http://www.chinamoney.com.cn/dqs/rest/dqs-u-currency/OrMthBltn?lang=cn&empty=-1&yearMonth=202009&indexType=ittvo",
            "web_site": "买断式回购月报",
        },
        {
            "cate": "http://www.chinamoney.com.cn/dqs/rest/dqs-u-bond/BdcMthBltn?lang=cn&yearMonth=202009&indexType=orgT",
            "web_site": "债券借贷月报",
        },
        {"cate": "", "web_site": ""},
        {"cate": "", "web_site": ""},
        {"cate": "", "web_site": ""},
    ]
    for each in cates:
        cate = each["cate"]
        web_site = each["web_site"]
        for i in range(31):
            hub_fields = {
                "web_site": web_site,
                "web_site_url": web_site_url,
                "source_type": source_type,
                "copyright": copyright,
            }
            day = now + timedelta(days=-1 * i)
            date = day.strftime("%Y-%m-%d")
            url = f"http://www.chinamoney.com.cn/dqs/rest/{cate}{date}"
            yield {"url": url, "page_rule_id": 18434, "hub_fields": hub_fields}


if __name__ == "__main__":
    import json

    for each in start_requests_1():
        print(json.dumps(each, indent=4, ensure_ascii=False))
