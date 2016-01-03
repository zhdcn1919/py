#!/system/sbin/env python
# coding=utf-8


import string
import time
import datetime
import urllib2



try:
    verify = raw_input('请输入QQ号码')
except KeyboardInterrupt:
    pass
def check_qq(verify):
    if verify.isdigit():
       checkurl = 'http://wpa.qq.com/pa?p=1:"+verify+":1'
       c = urllib2.urlopen(checkurl)
       length=c.headers.get("content-length")
       c.close()
    print datetime.datetime.now()
    if length=='2329':
        return 'Online'
    elif length=='2262':
        return 'Offline'
    else:
        return 'Unknown Status!'
if __name__ == '__main__':
    check_qq(verify)
    print 'qq ' + 'is '+ check_qq(verify)
