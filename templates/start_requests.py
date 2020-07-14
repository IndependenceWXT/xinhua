def start_requests(**kwargs):
    web_site = "克拉玛依市人民政府"

    web_site_url = "https://www.klmy.gov.cn/010/010005/secondpage.html"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    cates = [
        {
            "cate": f"http://www.wuhai.gov.cn/wuhai/xxgk4/jbxxgk46/813704/4c76f15a-{page}.html",
            "pages": 2,
            "web_site": "乌海市政府",
            "web_site_url": "http://www.wuhai.gov.cn/wuhai/xxgk4/jbxxgk46/813704/index.html",
            "page_rule_id": 10927,
        },
        {
            "cate": f"http://fgw.wuhai.gov.cn/eportal/ui?currentPage={page}&pageId=507579&moduleId=6ac003d7d6614ea796cb07915cb3687e",
            "pages": 2,
            "web_site": "乌海市发改委",
            "web_site_url": "http://fgw.wuhai.gov.cn/eportal/ui?pageId=507579&currentPage=1&moduleId=6ac003d7d6614ea796cb07915cb3687e",
            "page_rule_id": 10929,
        },
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]
        hub_fields = {"web_site": each["web_site"], "web_site_url": each["web_site_url"]}
        for page in range(pages):
            page = page + 1
            url = cate
            yield {"url": url, "page_rule_id": each["page_rule_id"], "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
