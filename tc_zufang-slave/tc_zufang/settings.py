# -*- coding: utf-8 -*-
BOT_NAME = 'tc_zufang'

SPIDER_MODULES = ['tc_zufang.spiders']
NEWSPIDER_MODULE = 'tc_zufang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tc_zufang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
DOWNLOAD_TIMEOUT=4
#避免爬虫被禁的策略1，禁用cookie
# Disable cookies (enabled by default)
CONCURRENT_REQUESTS=8
COOKIES_ENABLED = False
# CONCURRENT_REQUESTS_PER_IP=8
# CONCURRENT_REQUESTS_PER_DOMAIN=4
#设置下载延时，防止爬虫被禁
DOWNLOAD_DELAY = 5
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    "tc_zufang.Proxy_Middleware.ProxyMiddleware":100,
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'tc_zufang.timeout_middleware.Timeout_Middleware':610,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 300,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 400,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': None,
    'tc_zufang.rotate_useragent_dowmloadmiddleware.RotateUserAgentMiddleware':400,
    'tc_zufang.redirect_middleware.Redirect_Middleware':500,

}
#单机数据库配置
SingleMONGODB_SERVER = "101.200.46.191"
SingleMONGODB_PORT = 27017
SingleMONGODB_DB = "zufang_fs"
#设置数据入库pipline
ITEM_PIPELINES = {
    'tc_zufang.mongodb_pipeline.SingleMongodbPipeline':300,
}
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_URL = None
REDIS_HOST = '211.159.189.145' # 也可以根据情况改成 localhost
REDIS_PORT = '6379'
#配置日志存储目录
#LOG_FILE = "logs/scrapy.log"

