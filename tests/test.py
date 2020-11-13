def process(text):
    import json
    data = json.loads(text)
    for record in data["records"]:
        for rate in record["list"]:
            rate["rate"] = record["rate"]
            rate["updateDate"] = data["data"]["showYearMonth"]
    return json.dumps(data)


def process(text):
    import json
    data = json.loads(text)
    for each in data["records"]:
        each["lastDate"] = data["data"]["lastDate"]
    return json.dumps(data)