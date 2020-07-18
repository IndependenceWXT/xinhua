def process(text):
    text = text.split("-")
    text = "-".join(text[1:])
    return "http://121.18.64.252/zwgkcontent-" + text