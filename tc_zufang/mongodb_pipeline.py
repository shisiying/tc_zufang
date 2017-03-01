# -*- coding: utf-8 -*-
from pymongo import MongoClient
from scrapy import log

class SingleMongodbPipeline(object):
    MONGODB_SERVER = "localhost"
    MONGODB_PORT = 27017
    MONGODB_DB = "zufang_fs"

    def __init__(self):
        #初始化mongodb连接
        try:
            client = MongoClient(self.MONGODB_SERVER, self.MONGODB_PORT)
            self.db = client[self.MONGODB_DB]
        except Exception as e:
            print str(e)

    @classmethod
    def from_crawler(cls, crawler):
        cls.MONGODB_SERVER = crawler.settings.get('SingleMONGODB_SERVER', 'localhost')
        cls.MONGODB_PORT = crawler.settings.getint('SingleMONGODB_PORT', 27017)
        cls.MONGODB_DB = crawler.settings.get('SingleMONGODB_DB', 'zufang_fs')
        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def process_item(self, item, spider):
        zufang_detail = {
            'title': item.get('title'),
            'money': item.get('money'),
            'method': item.get('method'),
            'area': item.get('area', ''),
            'community': item.get('community', ''),
            'targeturl': item.get('targeturl'),
            'pub_time': item.get('pub_time', ''),
            'city':item.get('city','')
        }
        result = self.db['zufang_detail'].insert(zufang_detail)
        log.msg("Item %s wrote to MongoDB database %s/book_detail" %
                (result, self.MONGODB_DB),
                level=log.DEBUG, spider=spider)
        return item