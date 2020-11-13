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
            "cate": "dqs-u-currency/IblMthBltn?lang=cn&empty=-1&indexType=ittvo&yearMonth=",
            "web_site": "同业拆借月报",
        },
        {
            "cate": "dqs-u-currency/PrMthBltn?lang=cn&empty=-1&indexType=pitvo&searchDate=",
            "web_site": "质押式回购月报",
        },
        {
            "cate": "dqs-u-currency/OrMthBltn?lang=cn&empty=-1&indexType=ittvo&yearMonth=",
            "web_site": "买断式回购月报",
        },
        {"cate": "dqs-u-bond/BdcMthBltn?lang=cn&indexType=orgT&yearMonth=", "web_site": "债券借贷月报",},
        {"cate": "dqs-u-bond/BdcMthBltn?lang=cn&indexType=orgB&yearMonth=", "web_site": "现券买卖月报"},
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

    # 外汇交易中心统计月报-成交概览_按机构类别余额统计
    cates = [
        {
            "cate": "dqs-u-currency/IblMthBltn?lang=cn&empty=-1&indexType=itvo&yearMonth=",
            "web_site": "同业拆借月报",
        },
        {
            "cate": "dqs-u-currency/PrMthBltn?lang=cn&empty=-1&indexType=itVOList&searchDate=",
            "web_site": "质押式回购月报",
        },
        {
            "cate": "dqs-u-currency/OrMthBltn?lang=cn&empty=-1&indexType=btvo&yearMonth=",
            "web_site": "买断式回购月报",
        },
        {"cate": "dqs-u-bond/BdcMthBltn?lang=cn&indexType=orgB&yearMonth=", "web_site": "债券借贷月报",},
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
            yield {"url": url, "page_rule_id": 20309, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_按券种统计
    web_site = "买断式回购月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-currency/OrMthBltn?lang=cn&empty=-1&indexType=btvo&yearMonth={date}"
        yield {"url": url, "page_rule_id": 20310, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_按待偿期分类统计
    # 现券买卖月报
    web_site = "现券买卖月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-bond/CbtMthBltn?lang=cn&empty=-1&indexType=cpvo&yearMonth={date}"
        yield {"url": url, "page_rule_id": 20311, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_按债券类别分类统计
    web_site = "现券买卖月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-bond/CbtMthBltn?lang=cn&empty=-1&yearMonth=202009&indexType=btvo{date}"
        yield {"url": url, "page_rule_id": 20312, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_按计息方式分类
    # 现券买卖月报
    web_site = "现券买卖月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-bond/CbtMthBltn?lang=cn&empty=-1&indexType=imvo&yearMonth={date}"
        yield {"url": url, "page_rule_id": 20313, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_按机构类别分类
    # 现券买卖月报
    web_site = "现券买卖月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-bond/CbtMthBltn?lang=cn&empty=-1&indexType=itvo&yearMonth={date}"
        yield {"url": url, "page_rule_id": 20314, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_利率互换
    web_site = "利率互换月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-shibor/IrsMthBltn?lang=cn&empty=-1&indexType=irsmGroupVoList&searchDate={date}"
        yield {"url": url, "page_rule_id": 20315, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_标准债券远期成交情况
    web_site = "标准债券远期月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y-%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-bond/BondFwdBltn?lang=cn&rprtTp=6&searchDate={date}"
        yield {"url": url, "page_rule_id": 20316, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_标准债券远期分类成交情况(按交易品种分类)
    web_site = "标准债券远期月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y-%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-bond/BondFwdBltn?lang=cn&rprtTp=6&searchDate={date}"
        yield {"url": url, "page_rule_id": 20317, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_人民币外汇即期
    web_site = "人民币外汇即期月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-fx/RfxSpMthBltn?lang=cn&empty=-1&searchDate={date}"
        yield {"url": url, "page_rule_id": 20318, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_人民币外汇掉期\货币掉期
    cates = [
        {
            "cate": "dqs/rest/dqs-u-fx/RfxSwMthBltn?lang=cn&empty=-1&searchDate=",
            "web_site": "人民币外汇掉期月报",
        },
        {
            "cate": "ags/ms/cm-u-fx-mthrpt/searchCrsDealRptHis?lang=cn&month=",
            "web_site": "人民币外汇货币掉期月报",
        },
    ]
    for each in cates:
        cate = each["cate"]
        web_site = each["web_siet"]
        hub_fields = {
            "web_site": web_site,
            "web_site_url": web_site_url,
            "source_type": source_type,
            "copyright": copyright,
        }
        for i in range(31):
            day = now + timedelta(days=-1 * i)
            date = day.strftime("%Y%m")
            url = f"http://www.chinamoney.com.cn/{cate}{date}"
            yield {"url": url, "page_rule_id": 20319, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_人民币外汇远期
    web_site = "人民币外汇远期月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-fx/RfxFwMthBltn?lang=cn&empty=-1&searchDate={date}"
        yield {"url": url, "page_rule_id": 20320, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_人民币外汇期权
    web_site = "人民币外汇期权月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = (
            f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-fx/RfxSoMthBltn?lang=cn&yearMonth={date}"
        )
        yield {"url": url, "page_rule_id": 20321, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_外币拆借
    web_site = "外币拆借月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/ags/ms/cm-u-fx-mthrpt/searchFxclDealRptHis?lang=cn&month={date}"
        yield {"url": url, "page_rule_id": 20322, "hub_fields": hub_fields}

    # 外汇交易中心统计月报-成交概览_外币对即期
    web_site = "外币对即期月报"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "source_type": source_type,
        "copyright": copyright,
    }
    for i in range(31):
        day = now + timedelta(days=-1 * i)
        date = day.strftime("%Y%m")
        url = f"http://www.chinamoney.com.cn/dqs/rest/dqs-u-fx/CpairMthBltn?lang=cn&empty=-1&searchDate={date}"
        yield {"url": url, "page_rule_id": 20323, "hub_fields": hub_fields}


if __name__ == "__main__":
    import json

    for each in start_requests_1():
        print(json.dumps(each, indent=4, ensure_ascii=False))
