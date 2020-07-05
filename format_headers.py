import sys
import json


def jsonfy(s):
    headers = {}
    lines = s.strip().split("\n")
    for line in lines:
        k, v = line.split(": ")
        headers[k.strip()] = v.strip()
    print(json.dumps(headers, indent=4))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        jsonfy(sys.argv[1])
    else:
        print("请输入正确的Headers")