#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://news.163.com/rank'

html = requests.get(url)

print html.text

fr = open('wangyi.txt','w')
fr.write(html.text)
fr.close()
