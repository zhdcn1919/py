#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.tvmao.com/program/duration/satellite/w5-h16.html"
headers = {
	"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0"
}
html = requests.get(url,headers=headers)

fr = open("mao.txt","w")
fr.write(html.text)
fr.close()

link = re.findall('class="tdchn"><a href="(.*?)"',html.text,re.S)
title = re.findall('ctr="H?K?">(.*?)</a>',html.text,re.S)  # 又学习了一个正则。(H?K?)

for link,title in zip(link,title):
    link = "http://www.tvmao.com"+link
    title = title.replace('频道','')
    print title+'\t'+link
