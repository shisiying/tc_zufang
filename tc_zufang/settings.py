# -*- coding: utf-8 -*-

# Scrapy settings for tc_zufang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tc_zufang'

SPIDER_MODULES = ['tc_zufang.spiders']
NEWSPIDER_MODULE = 'tc_zufang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tc_zufang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#避免爬虫被禁的策略1，禁用cookie
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
#设置下载延时，防止爬虫被禁
DOWNLOAD_DELAY = 2
DOWNLOADER_MIDDLEWARES = {
#         #避免爬虫被禁的策略3，实现了一个可以访问google cache中的数据的download middleware(默认禁用)
#         # 'woaidu_crawler.contrib.downloadmiddleware.google_cache.GoogleCacheMiddleware':50,
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        #避免爬虫被禁的策略2,实现了一个download middleware，不停的变user-aget
    'tc_zufang.rotate_useragent_dowmloadmiddleware.RotateUserAgentMiddleware':400,
    # 'scrapy_crawlera.CrawleraMiddleware': 600
}
#crawlera代理设置
# #禁用Autothrottle扩展和增加并发请求的最大数量，以及设置下载超时
# CRAWLERA_ENABLED = True
# CONCURRENT_REQUESTS = 32
# CONCURRENT_REQUESTS_PER_DOMAIN = 32
# AUTOTHROTTLE_ENABLED = False
# DOWNLOAD_TIMEOUT = 600
# CRAWLERA_PRESERVE_DELAY = True
# CRAWLERA_USER = '726cf7a7812845dda9facc355fdb544f'
# CRAWLERA_PASS='hello2016'
#单机数据库配置
SingleMONGODB_SERVER = "localhost"
SingleMONGODB_PORT = 27017
SingleMONGODB_DB = "zufang_fs"
#设置数据入库pipline
ITEM_PIPELINES = {
    'tc_zufang.mongodb_pipeline.SingleMongodbPipeline':300,
}
#使用scrapy-redis组件，分布式运行多个爬虫
SCHEDULER = "tc_zufang.scrapy_redis.scheduler.Scheduler"
# Don't cleanup redis queues, allows to pause/resume crawls.
#实现断点续爬。
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'tc_zufang.scrapy_redis.queue.SpiderPriorityQueue'

#配置日志存储目录
# LOG_FILE = "logs/scrapy.log"
#爬虫监控使用graphite
# STATS_CLASS = 'tc_zufang.graphite.RedisGraphiteStatsCollector'
# GRAPHITE_HOST = '127.0.0.1'
# GRAPHITE_PORT = 2003
# GRAPHITE_IGNOREKEYS = []

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tc_zufang.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tc_zufang.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tc_zufang.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
