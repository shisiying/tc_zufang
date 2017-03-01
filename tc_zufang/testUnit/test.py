# -*- coding: utf-8 -*-
import re
# re='gz_2_39755299868183_28191154595392_sortid:1486483205000 @ ses:busitime ^ desc @ pubid:5453707'
# res=re.split('_')
# print 'http://dg.58.com/zufang/'+res[3]+'x.shtml'
# tre=u'\r\n                        2017-02-06 10:55:02\u66f4\u65b0\xa0\xa0\xa0\xa0'
# res=re.split(r'\W',tre.strip())
# print res[0]+'-'+res[1]+'-'+res[2]+' '+res[3]+':'+res[4]+':'+res[5]
# te=u'\u9ec4\u6c5f'
# print te.encode('utf8')
# res=u'http://sw.58.com/chuzu/'
# ress=re.findall('^http\:\/\/\w+\.58\.com',res)
# print ress
# '''[u'\r\n                            \u623f\u6e90\u7f16\u53f7\uff1a6947\xa0\xa0\xa
# 0\xa0\r\n                        2017-01-22 00:02:01\u66f4\u65b0\xa0\xa0\xa0\xa0
# ', u' \u6b21\u6d4f\u89c8\r\n        ']
# # [u'\r\n                        2017-02-06 13:12:02\u66f4\u65b0\xa0\xa0\xa0\xa0',
# #  u' \u6b21\u6d4f\u89c8\r\n        ']
# #  '''
# raw_time=u'\r\n                            \u623f\u6e90\u7f16\u53f7\uff1a6947\xa0\xa0\xa0\xa0\r\n                        2017-01-22 00:02:01\u66f4\u65b0\xa0\xa0\xa0\xa0'
# raw_time1=u'\r\n                        2017-02-06 10:55:02\u66f4\u65b0\xa0\xa0\xa0\xa0'
# res=re.findall(r'\d+\-\d+\-\d+\s+\d+\:\d+\:\d+',raw_time)
# res1=re.findall(r'\d+\-\d+\-\d+\s+\d+\:\d+\:\d+',raw_time1)
# print res
# print res1
# print res1
# # res = re.split(r'\W', raw_time.strip())
# print re.split(r'\s',res)
# print re.split(r'\s',res1)
# res='http://sw.58.com/zufang/28973792599111x.shtml'
# print res.split("//")[1].split('.')[0]
'''
第一国际百安居
南城
第一国际
'''
[u'\u7b2c\u4e00\u56fd\u9645\u767e\u5b89\u5c45', u'\u5357\u57ce', u'\u7b2c\u4e00\
u56fd\u9645']
[u'\u5357\u57ce', u'\u7b2c\u4e00\u56fd\u9645']
res=u'\u7b2c\u4e00\u56fd\u9645'
res1=res.encode("utf8")
print res1