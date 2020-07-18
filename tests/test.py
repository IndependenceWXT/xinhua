from atlassian import Confluence
from pprint import pprint

confluence = Confluence(
    url='http://10.40.35.103:8090/',
    username='fangtiansheng',
    password='fangtiansheng123')

res = confluence.get_page_by_id(328080, expand=True)