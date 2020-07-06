def start_requests(**kwargs):
    web_site = ""

    web_site_url = ""
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url
    }
    yield {"url": web_site_url, "page_rule_id": 10389, "hub_fields": hub_fields}

    web_site_url = ""
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url
    }
    for page in range(10):
        page = f"_{page+1}" if page else ""
        url = f"xxx{page}.index"
        yield {"url": url, "page_rule_id": 1089, "hub_fields": hub_fields}

if __name__ == '__main__':
    for each in start_requests():
        print(each)
