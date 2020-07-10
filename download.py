# coding:utf8
"""
下载脚本示例
   必须定义download函数
"""
def download(req) -> dict:
    """
 
    Args:
        req:  即为 DownloadRequest 对象 具体属性参见 http://confluence.shangjian.tech:8090/pages/viewpage.action?pageId=44155217
 
    Returns:
        {
            "redirect_url": "跳转后url str",
            "content": "页面源码 bytes",
            "text": "页面源码 str"",
            "status_code": "响应码 int",
            "headers": "响应headers  dict",
            "cookies": "响应cookies  dict",
            "status": "待定",
        }
        不需要全部返回：
            一般情况下 仅需要 redirect_url、content、status_code 字段
 
    """
    import requests

    r = requests.get(req.url)
    return dict(redirect_url=r.url, content=r.content)

class DownloadRequest:
    def __init__(self):
        self.url: str = ""
        self.url_id: str = ""
        self.method: str = ""
        self.data: str = ""
        self.post_type: str = "form"
        self.headers: dict = {}
        self.cookies: dict = {}
        self.download_url: str = ""
        self.timeout: int = 0
        self.proxy: str = "" # ip:port
        self.allow_redirects = True
 
        self.js_expr: str = ""
        self.load_wait: int = 0
        self.host: str = ""
        self.host_id: int = 0
        self.js_wait: int = 0

class DownloadResponse:
    def __init__(self):
        self.status_code = 200
        self.redirect_url = ""
        self.headers = {}
        self.cookies = {}
        self.content = b""
        self.text = ""
        self.js_val = None
        self.delay = 0
        self.charset = "utf-8"
        self.fail_reason = ""
        self.status: str = DownloadStatus.ok
 
    def from_dict(self, d: dict):
        """
        从字典加载
        Args:
            d:
 
        Returns:
 
        """
        self.status_code = d.get("status_code", self.status_code)
        self.redirect_url = d.get("redirect_url", self.status_code)
 
        self.headers.update(format_headers(d.get("headers", self.headers)))
        self.cookies.update(d.get("cookies", {}))
 
        self.content = d.get("content", self.content)
        self.text = d.get("text", self.text)
        self.status = d.get("status", self.status)


