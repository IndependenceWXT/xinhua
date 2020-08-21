
前言
记录一下很常见，但也很容易忽略的一些问题。主要是跟Web服务器相关的。

本文涉及到的名词有：

cgi、fastcgi、wsgi、uwsgi、gunicore、nginx、httpd

web服务器

WSGI服务

web框架



1、Web服务演进
基本框架：

Client（用户） -> Web服务器 -> 网页源码



1:支持最基本的文件访问

Client（用户） -> Web服务器(apache) -> 静态文件

2:实现动态生成文件功能

Client（用户） -> Web服务器(apache) -> 静态文件

                                                               |

                                                               |-> cgi -> 动态生成文件

3:提升cgi效率

Client（用户） -> Web服务器(apache) -> 静态文件

                                                                |

                                                                |-> fastcgi -> 动态生成文件

4:提升静态文件效率效率

Client（用户） -> Web服务器(nginx、apache) -> 静态文件

                                                                            |

                                                                            | -> fastcgi -> 动态生成文件


5:某些语言的特定实现方式

Client（用户） -> Web服务器(nginx、apache) -> 静态文件

                                                                           |

                                                                           | -> uwsgi -> flask、django -> 动态生成文件

Client（用户） -> Web服务器(nginx、apache) -> 静态文件

                                                                           |

                                                                           | -> php-fpm(fastcgi) -> php文件 -> 动态生成文件



2、通用规范
CGI
即Common Gateway Interface（通用网关接口） 见 https://zh.wikipedia.org/wiki/%E9%80%9A%E7%94%A8%E7%BD%91%E5%85%B3%E6%8E%A5%E5%8F%A3

为什么要有CGI？
早期的web服务器仅能访问静态网页。即你所访问的所有网页内容都是提前生成好放到服务器的上的，所谓的网页访问就是读取服务器上的某个文件然后返回内容。

cgi使动态网页成为可能。

CGI如何实现的？
通过定义一系列的通信规范来实现。

简而言之就是将url、header、params放入环境变量里，当你访问一个CGI文件时，web服务器会执行此CGI文件（脚本）获取输出然后返回给浏览器。你可以在CGI脚本中返回任意内容。

CGI程序可以用任何脚本语言或者编程语言实现，只要该语言可以在系统上运行。

例如：http://www.example.com/wiki.cgi

以前比较常用的是perl来实现cgi脚本。

CGI环境变量示例：
https://www.runoob.com/python/python-cgi.html

CONTENT_TYPE：这个环境变量的值指示所传递来的信息的MIME类型。目前，环境变量CONTENT_TYPE一般都是：application/x-www-form-urlencoded,他表示数据来自于HTML表单。

CONTENT_LENGTH：如果服务器与CGI程序信息的传递方式是POST，这个环境变量即使从标准输入STDIN中可以读到的有效数据的字节数。这个环境变量在读取所输入的数据时必须使用。

HTTP_COOKIE：客户机内的 COOKIE 内容。

HTTP_USER_AGENT：提供包含了版本数或其他专有数据的客户浏览器信息。

PATH_INFO：这个环境变量的值表示紧接在CGI程序名之后的其他路径信息。它常常作为CGI程序的参数出现。

QUERY_STRING：如果服务器与CGI程序信息的传递方式是GET，这个环境变量的值即使所传递的信息。这个信息经跟在CGI程序名的后面，两者中间用一个问号'?'分隔。

REMOTE_ADDR：这个环境变量的值是发送请求的客户机的IP地址，例如上面的192.168.1.67。这个值总是存在的。而且它是Web客户机需要提供给Web服务器的唯一标识，可以在CGI程序中用它来区分不同的Web客户机。

REMOTE_HOST：这个环境变量的值包含发送CGI请求的客户机的主机名。如果不支持你想查询，则无需定义此环境变量。

REQUEST_METHOD：提供脚本被调用的方法。对于使用 HTTP/1.0 协议的脚本，仅 GET 和 POST 有意义。

SCRIPT_FILENAME：CGI脚本的完整路径

SCRIPT_NAME：CGI脚本的的名称

SERVER_NAME：这是你的 WEB 服务器的主机名、别名或IP地址。

SERVER_SOFTWARE：这个环境变量的值包含了调用CGI程序的HTTP服务器的名称和版本号。例如，上面的值为Apache/2.2.14(Unix)

CGI的缺点？
一般每次的CGI请求都需要新生成一个程序的副本来运行，这样大的工作量会很快将服务器压垮。

因此一些更有效的技术像mod_perl，可以让脚本解释器直接作为模块集成在Web服务器（例如：Apache）中，这样就能避免重复加载和初始化解释器。

不过这只是就那些需要解释器的高级语言（即解释语言，例如python）而言的，使用诸如C一类的编译语言则可以避免这种额外负荷。

由于C及其他编译语言的程序与解释语言程序相比，前者的运行速度更快、对操作系统的负荷更小，使用编译语言程序是可能达到更高执行效率的.

然而因为开发效率等原因，在目前解释型语言还是最合适的。



FastCGI
即FastCommon Gateway Interface（快速通用网关接口）见：https://zh.wikipedia.org/wiki/FastCGI

为了解决CGI效率低下的问题而进行的改进。

CGI会对每个请求创建一个进程，在请求结束时销毁。开销太大。

而FastCGI会使用进程池来处理请求，避免频繁开启进程的开销。




3、特定语言实现
WSGI
即 Python Web Server Gateway Interface（Python Web服务器网关接口）

参见：

https://www.python.org/dev/peps/pep-3333/

https://zh.wikipedia.org/wiki/Web%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BD%91%E5%85%B3%E6%8E%A5%E5%8F%A3

https://www.liaoxuefeng.com/wiki/1016959663602400/1017805733037760

起初是为Python定义的Web服务器与Web应用程序之间的接口。后来一些其他语言也参考实现了自己的wsgi

为什么要有WSGI？
抄自PEP-3333：

Python当前拥有各种各样的Web应用程序框架，例如Zope，Quixote，Webware，SkunkWeb，PSO和Twisted Web-仅举几例[1]。对于Python的新用户来说，各种各样的选择可能是个问题，因为通常来说，他们对Web框架的选择将限制他

们对可用Web服务器的选择，反之亦然。

相比之下，尽管Java具有许多可用的Web应用程序框架，但是Java的“ Servlet” API使得使用任何Java Web应用程序框架编写的应用程序都可以在支持Servlet API的任何Web服务器中运行。

WSGI规范？
定义了两类对象：

Web服务器：例如uWSGI、gunicorn。[Werkzeug]

Web应用程序：Flask、Django的application



Web应用程序只需要实现一个函数即可:

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


Web服务器收到请求后会调用application函数

wsgi的environment示例：
{

'HTTP_ACCEPT': '*/*',

'HTTP_ACCEPT_ENCODING': 'gzip, deflate',

'HTTP_CONNECTION': 'keep-alive',

'HTTP_HOST': 'localhost:6666',

'HTTP_USER_AGENT': 'python-requests/2.18.4',

'PATH_INFO': '/hello',

'QUERY_STRING': '',

'REMOTE_ADDR': '127.0.0.1',

'REMOTE_PORT': 61415,

'REQUEST_METHOD': 'GET',

'SCRIPT_NAME': '',

'SERVER_NAME': '0.0.0.0',

'SERVER_PORT': '6666',

'SERVER_PROTOCOL': 'HTTP/1.1',

'SERVER_SOFTWARE': 'Werkzeug/0.14.1',

'werkzeug.server.shutdown': '<function WSGIRequestHandler.make_environ.<locals>.shutdown_server at 0x108a02378>',

'wsgi.errors': "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>",

'wsgi.input': '<_io.BufferedReader name=7>',

'wsgi.multiprocess': False,

'wsgi.multithread': False,

'wsgi.run_once': False,

'wsgi.url_scheme': 'http',

'wsgi.version': (1, 0)

}



WSGI的好处？
如果没有的话，Web框架就只能通过Socket接收原始数据，自己实现HTTP协议的解析。但这些事情其实是不必要的，交给专业的人来做更好。

一般WSGI服务器都是C写的，效率更高。

对web框架的使用者来说，他们并不关心如何接收 HTTP 请求，也不关心如何将请求路由到具体方法处理并将响应结果返回给用户。Web框架的使用者在大部分情况下，只需要关心如何实现业务的逻辑即可。



Flask干了啥？
flask.Flask的

def __call__(self, environ, start_response):
    """Shortcut for :attr:`wsgi_app`."""
    return self.wsgi_app(environ, start_response)


Django干了啥？
django.core.handlers.wsgi.py

class WSGIHandler(base.BaseHandler):
    request_class = WSGIRequest

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_middleware()


    def __call__(self, environ, start_response):
        ...
        status = '%d %s' % (response.status_code, response.reason_phrase)
        response_headers = [
        *response.items(),
        *(('Set-Cookie', c.output(header='')) for c in response.cookies.values()),
        ]
        start_response(status, response_headers)
        if getattr(response, 'file_to_stream', None) is not None and environ.get('wsgi.file_wrapper'):
        response = environ['wsgi.file_wrapper'](response.file_to_stream)
        return response




uwsgi、uWSGI
https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/

uwsgi是一个uWSGI服务器的专有协议

https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/Protocol.html

uWSGI服务器实现了wsgi、uwsgi两种协议

uWSGI配置示例：
[uwsgi]

http = :8000

socket = 127.0.0.1:3031

wsgi-file = backend/wsgi.py

callable = app

chdir = /opt/baelish/src

processes = 4

threads = 16

plugins = python3

max-requests = 100000

master = true

harakiri=30

uWSGI很复杂 有兴趣的可以研究一下

混淆点
WSGI: Python Web Server Gateway Interface

uWSGI: 实现了WSGI、uwsgi两种协议的一个Web服务器

uwsgi: uWSGI服务器自定义的一种协议

为啥我不用uWSGI也可以启动Web服务？
如果你看源码的话，会发现其实是启动了个Python内置的WSGI服务器。



gunicore
跟uWSGI同属实现了WSGI协议的Web服务器。前身是ruby的unicore。

但底层实现不一样，各有优缺点吧。

http://xiaorui.cc/archives/4264



PHP
php本质上是一个CGI脚本。所以PHP写的网站都是.php结尾的文件。

php-fpm是一个实现了fastcgi规范的进程管理服务


4、Web服务器
Nginx
作用很多，不一一说明了。

1、静态文件访问功能（很优秀）

2、服务转发

3、负载均衡

4、虚拟主机：不同域名访问同一个IP、同一个主机上的不同服务



一般生产服务会使用nginx+uwsgi+flask部署

静态使用nginx处理，动态直接转发到uWSGI

为啥nginx不能直接接flask?
因为nginx不会python

如果在nginx中直接用WSGI， 那么 nginx线程中就要启动python解释器，



Apache
感觉已经过时了，不过曾经很火，因为出现的比较早，所以还有很多老系统在用。



IIS

微软开发windows服务器上运行的


5、其他语言：
Java 现在流行内置 tomcat 了

php 最近也有一些内置 http server 的框架，性能远超跑 fpm 里的框架

ruby 版的 wsgi 叫 rack

go 语言则是标准库内置 http 服务

nodejs 也是内置 http



参考：

https://www.python.org/dev/peps/pep-3333/

https://juejin.im/post/6844904202825646093

http://www.nowamagic.net/academy/detail/1330211



