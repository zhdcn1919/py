#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import requests

url = 'http://www.baidu.com'
html = requests.get(url)
html.encoding = 'utf-8'
