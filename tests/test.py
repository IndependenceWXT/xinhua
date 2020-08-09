def extract(context):
    """
    抽取函数
    :param context: 字典 {"url": url, "row": "当前行", "body": "当前页面"}
    :return: list 元素为字典
    """
    import re
    import json

    url = context["url"]
    body = json.loads(context["body"])
    data = body[-1]
    last = data.get("id")

    url = re.sub(r"\d{7}", last, url)
    new_link = {"url": url}
    return [new_link]

    url = context["url"]
    row = context["row"]
    if url == "http://www.mrjjxw.com/":
        new_link = f"http://www.mrjjxw.com/mrjjxw/columns/importent/ui_column_articles_list.json?limit=20&article_id_before={row}"
    elif url == "http://www.mrjjxw.com/mrjjxw/ui_columns/digit":
        new_link = f"http://www.mrjjxw.com/mrjjxw/columns/digit/ui_column_articles_list.json?limit=20&article_id_before={row}"


if __name__ == "__main__":
    print(
        extract(
            {
                "url": "https://article-api.huxiu.com/web/channel/articleList?platform=www&last_time=1596795840&channel_id=115",
                "body": "",
            }
        )
    )

