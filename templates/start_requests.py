def start_requests(**kwargs):
    web_site = "营口市政府"
    web_site_url = "http://www.yingkou.gov.cn/dynamic/zw/openlist.html?categorynum=001001003"
    cates = [
        {"cate": "001001003001", "pages": 2},
        {"cate": "001001003002", "pages": 19},
        {"cate": "001001003003", "pages": 32},
        {"cate": "001001003004", "pages": 0},
        {"cate": "001001003005", "pages": 0},
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]
        hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
        url = "http://www.yingkou.gov.cn/EWB_YK_Mid/rest/lightfrontaction/getgovinfolist"
        for p in range(pages):
            data = '{"params":{"deptcode":"","categorynum":"'+cate+'","pageIndex":"'+str(p)+'","pageSize":15,"siteGuid":"7eb5f7f1-9041-43ad-8e13-8fcb82ea831a"}}'
            yield {
                "url": url,
                "page_rule_id": 11542,
                "data": data,
                "method": "POST",
                "hub_fields": hub_fields,
            }



if __name__ == "__main__":
    for each in start_requests():
        print(each)
