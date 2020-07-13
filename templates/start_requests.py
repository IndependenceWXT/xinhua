def start_requests(**kwargs):
    web_site = "克拉玛依市人民政府"

    web_site_url = "https://www.klmy.gov.cn/010/010005/secondpage.html"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
    for page in range(2):
        page = f"{page+1}" if page else "secondpage"
        url = f"https://www.klmy.gov.cn/010/010005/{page}.html"
        yield {"url": url, "page_rule_id": 10702, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
