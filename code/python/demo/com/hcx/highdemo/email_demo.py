#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'hancx@test.com'
receivers = ['118517757@qq.com']

message = MIMEText('Python test')
message['From'] = Header('test','utf-8')
message['To'] = Header('test', 'utf-8')

subject = 'python smtp test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('send success!')
except smtplib.SMTPException:
    print('Error:not send email message')
