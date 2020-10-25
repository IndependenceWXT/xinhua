"""
自动加载templates中的脚本文件里的处理器和验证器到base模版文件， 自动生成升级模版
    - 利用base模版，添加脚本处理器验证器制作自定义模版
    - 编码测试
    
    - 加载模版
    - 加载配置
    - 升级配置
    - 保存配置

"""

import inspect
import jinja2

import selenium
import yaml

from templates.process import *
from templates.validate import *


inspect.getsource(process_author_template)

