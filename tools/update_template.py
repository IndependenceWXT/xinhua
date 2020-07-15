"""
TODO: 自动加载templates中的脚本文件里的处理器和验证器到base模版文件， 自动升级模版
    - 制作base模版
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

