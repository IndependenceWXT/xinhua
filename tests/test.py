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