#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://news.163.com/rank'

<<<<<<< HEAD
def Spider(url):
    i = 0
    print "downloading ", url
    myPage = requests.get(url).content.decode("gbk")
    # myPage = urllib2.urlopen(url).read().decode("gbk")
    myPageResults = Page_Info(myPage)
    save_path = u"/home/hades/163"
    filename = str(i)+"_"+u"新闻排行榜"
    StringListSave(save_path, filename, myPageResults)
    i += 1
    for item, url in myPageResults:
        print "downloading ", url
        new_page = requests.get(url).content.decode("gbk")
        # new_page = urllib2.urlopen(url).read().decode("gbk")
        newPageResults = New_Page_Info(new_page)
        filename = str(i)+"_"+item
        StringListSave(save_path, filename, newPageResults)
        i += 1
=======
html = requests.get(url)
>>>>>>> 6212727a4274f12026a066ff9ae17dc34123ed62

print html.text

fr = open('wangyi.txt','w')
fr.write(html.text)
fr.close()
