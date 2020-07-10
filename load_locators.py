import yaml
from pprint import pprint

with open("新闻详情页配置模板.yml", mode='r', encoding='utf-8') as stream:
    try:
        data = yaml.safe_load(stream)
        pprint(data)
    except yaml.YAMLError as exc:
        pprint(exc)

with open('tmp.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

with open("tmp.yaml", mode='r', encoding='utf-8') as stream:
    data_loaded = yaml.safe_load(stream)

print(data == data_loaded)