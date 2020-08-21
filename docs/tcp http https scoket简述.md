## **![img](http://confluence.shangjian.tech:8090/plugins/servlet/confluence/placeholder/macro?definition=e3RvY30&locale=zh_CN&version=2)**

## **tcp**

**https://tools.ietf.org/html/rfc793**



### OSI体系结构

OSI体系结构，意为[开放式系统互联](https://baike.baidu.com/item/开放式系统互联/562749)。国际标准组织（国际标准化组织）制定了OSI模型。这个模型把[网络通信](https://baike.baidu.com/item/网络通信/9636548)的工作分为7层，分别是[物理层](https://baike.baidu.com/item/物理层/4329158),[数据链路层](https://baike.baidu.com/item/数据链路层/4329290),[网络层](https://baike.baidu.com/item/网络层/4329439),[传输层](https://baike.baidu.com/item/传输层/4329536),会话层，[表示层](https://baike.baidu.com/item/表示层/4329716)和[应用层](https://baike.baidu.com/item/应用层/4329788)

这个模型把[网络通信](https://baike.baidu.com/item/网络通信/9636548)的工作分为7层，分别是[物理层](https://baike.baidu.com/item/物理层/4329158),[数据链路层](https://baike.baidu.com/item/数据链路层/4329290),[网络层](https://baike.baidu.com/item/网络层/4329439),[传输层](https://baike.baidu.com/item/传输层/4329536),会话层，[表示层](https://baike.baidu.com/item/表示层/4329716)和[应用层](https://baike.baidu.com/item/应用层/4329788)

### TCP

传输控制协议（TCP，Transmission Control Protocol）是为了在不可靠的互联网络上提供可靠的端到端字节流而专门设计的一个传输协议



![img](https://img-blog.csdnimg.cn/20190414223004578.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xlaG82NjY=,size_16,color_FFFFFF,t_70)



### 三次握手

SYN表示建立连接，

ACK表示响应，

FIN表示关闭连接，

PSH表示有 DATA数据传输，

RST表示连接重置。

\1. 客户端发送SYN（SEQ=x）报文给服务器端，进入SYN_SEND状态。

2.服务器端收到SYN报文，回应一个SYN （SEQ=y）ACK（ACK=x+1）报文，进入SYN_RECV状态。

3.客户端收到服务器端的SYN报文，回应一个ACK（ACK=y+1）报文，进入Established状态。

![数据部文档 > tcp http https scoket简述 > image2020-8-21_11-20-38.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_11-20-38.png?version=1&modificationDate=1597980038988&api=v2)

![数据部文档 > tcp http https scoket简述 > image2020-8-21_11-56-34.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_11-56-34.png?version=1&modificationDate=1597982194886&api=v2)

### 四次挥手

\1. 某个应用进程首先调用close，称该端执行“主动关闭”（active close）。该端的TCP于是发送一个FIN分节，表示数据发送完毕。
\2. 接收到这个FIN的对端执行 “被动关闭”（passive close），这个FIN由TCP确认。
注意：FIN的接收也作为一个文件结束符（end-of-file）传递给接收端应用进程，放在已排队等候该应用进程接收的任何其他数据之后，因为，FIN的接收意味着接收端应用进程在相应连接上再无额外数据可接收。
\3. 一段时间后，接收到这个文件结束符的应用进程将调用close关闭它的套接字。这导致它的TCP也发送一个FIN。
\4. 接收这个最终FIN的原发送端TCP（即执行主动关闭的那一端）确认这个FIN。 [3] 

![数据部文档 > tcp http https scoket简述 > image2020-8-21_11-36-19.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_11-36-19.png?version=1&modificationDate=1597980979434&api=v2)

![数据部文档 > tcp http https scoket简述 > image2020-8-21_11-57-6.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_11-57-6.png?version=1&modificationDate=1597982226697&api=v2)



## HTTP

https://www.w3.org/Protocols/rfc2616/rfc2616.html

超文本传输协议，是一个基于请求与响应，无状态的，应用层的协议，常基于TCP/IP协议传输数据，互联网上应用最为广泛的一种网络协议,所有的WWW文件都必须遵守这个标准。设计HTTP的初衷是为了提供一种发布和接收HTML页面的方法。

### 请求

![数据部文档 > tcp http https scoket简述 > image2020-8-20_22-45-6.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-20_22-45-6.png?version=1&modificationDate=1597934709017&api=v2)

![数据部文档 > tcp http https scoket简述 > image2020-8-21_10-54-8.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_10-54-8.png?version=1&modificationDate=1597978448149&api=v2)

### 响应

![数据部文档 > tcp http https scoket简述 > image2020-8-20_22-45-44.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-20_22-45-44.png?version=1&modificationDate=1597934746359&api=v2)



![数据部文档 > tcp http https scoket简述 > image2020-8-21_10-55-31.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_10-55-31.png?version=1&modificationDate=1597978531209&api=v2)







## HTTPS

HTTPS是身披SSL（Secure Sockets Layer [安全套接字协议](https://baike.baidu.com/item/安全套接字协议)）外壳的HTTP。HTTPS是一种通过计算机网络进行安全通信的传输协议，经由HTTP进行通信，利用SSL/TLS建立全信道，加密数据包。HTTPS使用的主要目的是提供对网站服务器的身份认证，同时保护交换数据的隐私与完整性。

![数据部文档 > tcp http https scoket简述 > image2020-8-21_11-51-51.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_11-51-51.png?version=1&modificationDate=1597981911154&api=v2)



![数据部文档 > tcp http https scoket简述 > image2020-8-21_11-55-30.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_11-55-30.png?version=1&modificationDate=1597982130498&api=v2)







### 基础知识

对称加密，非对称加密

公钥 私钥

### 传输过程

-   ① Client发送https请求；
-   ② Client和Server通过tcp的三次握手建立连接，且协商完ssl的版本、加密书算法；
-   ③ Server发送crt证书给Client；
-   ④ Client通过信任机构CA的证书，验证Server证书的有效性，若证书无效，则显示告警；若证书有效，Client随机生成一个字符串，并使用Server证书中的公钥对随机字符串进行加密；
-   ⑤ Client发送加密后的随机字符串给Server；
-   ⑥ Server使用自己的私钥解密，获取Client产生的随机字符串，此后，Client和Server之间的通信数据都使用该随机字符串进行对称加密；
-   ⑦ Server使用随机字符串加密数据，并发送给Client；
-   ⑧ Client使用随机字符串解密数据；



## 总结



![数据部文档 > tcp http https scoket简述 > image2020-8-21_11-59-20.png](http://confluence.shangjian.tech:8090/download/attachments/55826696/image2020-8-21_11-59-20.png?version=1&modificationDate=1597982360554&api=v2)



http连接=以http协议为通信协议的tcp连接

http短连接=以http协议为通信协议的，请求一次就断开的tcp连接

http长连接=以http协议为通信协议的，请求多次才断开的tcp连接

socket tcp的实现

websocket 也是一种协议