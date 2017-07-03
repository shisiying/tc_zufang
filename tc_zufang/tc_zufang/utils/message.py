# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def sendMessage_warning():
    server = smtplib.SMTP('smtp.163.com', 25)
    server.login('seven_2016@163.com', '*******')
    msg = MIMEText('爬虫Master被封警告！请求解封！', 'plain', 'utf-8')
    msg['From'] = 'seven_2016@163.com <seven_2016@163.com>'
    msg['Subject'] = Header(u'爬虫被封禁警告！', 'utf8').encode()
    msg['To'] = u'seven <751401459@qq.com>'
    server.sendmail('seven_2016@163.com', ['751401459@qq.com'], msg.as_string())
