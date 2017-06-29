项目目录介绍
===============
所有项目默认的地址默认是本地，可根据需要配置远程服务器
1）django_web是数据的可视化端，执行的方法是，在这个目录下，执行python manage.py runserver启动服务器，然后访问，http://ip:port/document，配置mongodb服务器的话，需要修改views下的地址
2）ipprocy是爬虫代理ip模块，执行的方法是cd进入目录中，然后执行python IPProxy.py
3）tc_zufang是Master端的爬虫，执行方法是，cd进入目录中，然后执行scrapy crawl tczufang,
配置获取代理ip服务器地址，需修改utils下的GetProxyIp.py文件，此地址也是ipprocy运行的服务器地址
配置redis服务器，需修改utils下的InsertRedis.py文件的redis服务器地址，以及修改目录下的settings文件的redis服务器地址
4）tc_zufang-slave是Slave端的爬虫，执行方法是，cd进入目录中，然后执行scrapy crawl tczufang
配置redis服务器：修改settings的redis地址，此处redis地址应该与utils下的InsertRedis.py文件的redis服务器地址2类型的一样
配置mongodb服务器，修改settings的mongodb的地址，此处的地址应该与django_web的mongodb服务器地址一样。
