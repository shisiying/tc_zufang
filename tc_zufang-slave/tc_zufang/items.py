# -*- coding: utf-8 -*-
#定义需要抓取存进数据库的字段
from scrapy.item import Item,Field
class TcZufangItem(Item):
    #帖子名称
    title=Field()
    #租金
    money=Field()
    #租赁方式
    method=Field()
    #所在区域
    area=Field()
    #所在小区
    community=Field()
    #帖子详情url
    targeturl=Field()
    #帖子发布时间
    pub_time=Field()
    #所在城市
    city=Field()
    # 联系电话
    phone= Field()
    # 图片1
    img1 = Field()
    # 图片2
    img2 = Field()



