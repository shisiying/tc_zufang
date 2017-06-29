1.项目目录介绍
===============

    所有项目默认的地址默认是本地，可根据需要配置远程服务器
    1）django_web是数据的可视化端，执行的方法是，在这个目录下，执行python manage.py runserver启动服务器，然后访问，http://ip:port/document
    配置mongodb服务器的话，需要修改views下的地址
    
    2）ipprocy是爬虫代理ip模块，执行的方法是cd进入目录中，然后执行python IPProxy.py
    
    3）tc_zufang是Master端的爬虫，执行方法是，cd进入目录中，然后执行scrapy crawl tczufang,
    配置获取代理ip服务器地址，需修改utils下的GetProxyIp.py文件，此地址也是ipprocy运行的服务器地址
    配置redis服务器，需修改utils下的InsertRedis.py文件的redis服务器地址，以及修改目录下的settings文件的redis服务器地址
    
    4）tc_zufang-slave是Slave端的爬虫，执行方法是，cd进入目录中，然后执行scrapy crawl tczufang
    配置redis服务器：修改settings的redis地址，此处redis地址应该与utils下的InsertRedis.py文件的redis服务器地址2类型的一样
    配置mongodb服务器，修改settings的mongodb的地址，此处的地址应该与django_web的mongodb服务器地址一样。

2.配置环境（非docker环境下部署）docker下部署不做说明
=========================

    服务器需配置的环境：
    mongodb redis python2.7 
    python要安装的库
    scrapy==1.0  requests chardet web.py sqlalchemy gevent psutil django==1.5 redis python-redis pymongo twisted==11.0 scrapy-redis
    执行步骤:
    #第一步：打开代理
    python IPProxy.py
    #第二步：部署Master端
    scrapy crawl tczufang
    #第三步:redis插入起始url
    连接上redis之后，执行下列指令，如下所示:
    lpush start_urls http://dg.58.com/chuzu/
    下列是可抓取列表：
    'http://dg.58.com/chuzu/',
    'http://sw.58.com/chuzu/',
    'http://sz.58.com/chuzu/',
    'http://gz.58.com/chuzu/',
    'http://fs.58.com/chuzu/',
    'http://zs.58.com/chuzu/',
    'http://zh.58.com/chuzu/',
    'http://huizhou.58.com/chuzu/',
    'http://jm.58.com/chuzu/',
    'http://st.58.com/chuzu/',
    'http://zhanjiang.58.com/chuzu/',
    'http://zq.58.com/chuzu/',
    'http://mm.58.com/chuzu/',
    'http://jy.58.com/chuzu/',
    'http://mz.58.com/chuzu/',
    'http://qingyuan.58.com/chuzu/',
    'http://yj.58.com/chuzu/',
    'http://sg.58.com/chuzu/',
    'http://heyuan.58.com/chuzu/',
    'http://yf.58.com/chuzu/',
    'http://chaozhou.58.com/chuzu/',
    'http://taishan.58.com/chuzu/',
    'http://yangchun.58.com/chuzu/',
    'http://sd.58.com/chuzu/',
    'http://huidong.58.com/chuzu/',
     http:// boluo.58.com/chuzu/',
    Slave:101.200.46.191
    #第三步：部署Slave端
    scrapy crawl tczufang
    #第四步：部署可视化端
    python manage.py runserver
    访问http://ip:port/document
