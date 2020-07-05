def start_requests(**kwargs):
    website = "医药网"

    cates = [
        {"channel": "医药财经", "cate": "yycj", "pages": 4},
        {"channel": "最新资讯", "cate": "hyyw/news", "pages": 6},
        {"channel": "医药营销", "cate": "hydt/yyyx", "pages": 14},
        {"channel": "医药进出口", "cate": "hydt/yyjck", "pages": 7},
        {"channel": "中医药资讯", "cate": "hydt/zyyzx", "pages": 11},
        {"channel": "企业新闻", "cate": "hydt/qyxw", "pages": 18},
        {"channel": "政策环境", "cate": "hydt/zchj/yjdt", "pages": 4},
        {"channel": "上市公司", "cate": "hydt/yyjck/ssgs", "pages": 3},
        {"channel": "国际动态", "cate": "gjdt", "pages": 3},
        {"channel": "人才资讯", "cate": "rczx", "pages": 2},
    ]
    for each in cates:
        channel = each["channel"]
        cate = each["cate"]
        pages = each["pages"]
        hub_fields = {
            "website": website,
            "channel": channel,
        }
        for page in range(pages):
            url = f"http://news.pharmnet.com.cn/news/{cate}/index{page}.html"
            yield {"url": url, "page_rule_id": 9481, "hub_fields": hub_fields}


if __name__ == '__main__':
    for each in start_requests():
        print(each)
