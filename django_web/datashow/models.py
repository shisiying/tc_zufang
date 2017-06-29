# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import *
from django.db import models

# Create your models here.
class ItemInfo(Document):
    # 帖子名称
    title = StringField()
    # 租金
    money = StringField()
    # 租赁方式
    method = StringField()
    # 所在区域
    area = StringField()
    # 所在小区
    community = StringField()
    # 帖子详情url
    targeturl = StringField()
    # 帖子发布时间
    pub_time = StringField()
    # 所在城市
    city = StringField()
    phone = StringField()
    img1= StringField()
    img2 = StringField()
    #指定是数据表格
    meta={'collection':'zufang_detail'}
