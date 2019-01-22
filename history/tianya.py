#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import pandas as pd

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

a = []
url = 'http://focus.tianya.cn'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')

fr = open('stianya.txt','w')
fr.write(content)
fr.close()

items = re.findall(' title="(.*?)" target=_blank',content,re.S)

#for item in items:
#    a.append(item)
#    b = pd.DataFrame(a)
#    print b

for item in items:
    print items
