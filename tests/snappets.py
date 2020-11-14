""" chrome snippets manage tool: export and import
"""

import json
from pathlib import Path
import fire

def version():
    versions = [
        "Chrome",
        "Chrome Dev",
        "Chrome Canary"
    ]
    print(json.dumps({i: v for i, v in enumerate(versions)}))
    choose = input('Your Chrome Version: \n')
    if int(choose) not in range(3):
        print("wrong operation.")
        return
    chrome = versions[int(choose)]
    return chrome


def home():
    return Path.home()


def conf(home, chrome):
    p = f"{home}/Library/Application Support/Google/{chrome}/Default/Preferences"
    return Path(p).read_text(encoding="utf-8")


def destination(h):
    dest = h / "Downloads" / "Snippets"
    dest.mkdir(exist_ok=True)
    return dest


def export():
    chrome = version()
    h = home()
    c = conf(h, chrome)
    dest = destination(h)

    data = json.loads(c)
    devtools = data["devtools"]
    preferences = devtools["preferences"]
    scriptSnippets = preferences["scriptSnippets"]
    scripts = json.loads(scriptSnippets)
    for each in scripts:
        name, content = each.values()
        p = dest / name
        p.write_text(content, encoding="utf-8")


def im(source):
    print("Close Chrome from Dock")
    chrome = version()
    h = home()
    conf_path = f"{h}/Library/Application Support/Google/{chrome}/Default/Preferences"
    c = conf(h, chrome)
    data = json.loads(c)
    devtools = data["devtools"]
    preferences = devtools["preferences"]
    scriptSnippets = preferences.get("scriptSnippets", '[]')
    p = Path(source)
    scripts = json.loads(scriptSnippets)
    for each in p.glob("*/*.js"):
        name = each.name
        content = each.read_text(encoding="utf-8")
        scripts.append(
            {
                "name": name,
                "content": content
            }
        )
    preferences["scriptSnippets"] = json.dumps(scripts)
    devtools["preferences"] = preferences
    data["devtools"] = devtools

    Path(conf_path).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


if __name__ == '__main__':
    # fire.Fire(export)
    im("/Users/fangtiansheng/Documents/GitHub/devtools-snippets/snippets")
