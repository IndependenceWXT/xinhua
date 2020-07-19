from atlassian import Confluence
from pprint import pprint

confluence = Confluence(
    url='http://10.40.35.103:8090/',
    username='fangtiansheng',
    password='fangtiansheng123')

res = confluence.get_page_by_id(328080, expand="body.storage")
print(type(res))
# pprint(res)
res = confluence.get_page_properties(328080)
# pprint(res)

res = confluence.get_user_details_by_userkey("2c918083730fcf020173135f0972000d")
print(res)
def start_requests(**kwargs):
    source_type = 1
    copyright = 0
    web_site = "呼和浩特市政府"

    web_site_url = "http://www.huhhot.gov.cn/zwgk/zfxxgkzl/zfxxgkmlx/"
    news_type = "政策文件"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "news_type": news_type,
        "source_type": source_type,
        "copyright": copyright,
    }
    for p in range(250):
        p = f"_{p}" if p else ""
        url = f"http://www.huhhot.gov.cn/zwgk/zfxxgkzl/zfxxgkmlx/index_3340{p}.html"
        yield {"url": url, "page_rule_id": 11580, "hub_fields": hub_fields}

    web_site = "呼和浩特市发改委"

    web_site_url = "http://fgw.huhhot.gov.cn/swgk/zwgk/zcfg/"
    hub_fields = {
        "web_site": web_site,
        "web_site_url": web_site_url,
        "news_type": news_type,
        "source_type": source_type,
        "copyright": copyright,
    }
    for p in range(10):
        p = f"_{p}" if p else ""
        url = f"http://fgw.huhhot.gov.cn/swgk/zwgk/zcfg/index{p}.html"
        yield {"url": url, "page_rule_id": 11582, "hub_fields": hub_fields}
