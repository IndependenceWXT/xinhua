import re
p = re.compile(r'/files/article/pics/(?P<year>\d{4})(?P<month>\d{2})/(?P<day>\d{2})/')

text = "/files/article/pics/201808/07/1533630466_101.jpg"
res = p.findall(text)
print(res[0])

