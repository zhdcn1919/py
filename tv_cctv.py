#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

html = requests.get("http://tv.cctv.com/live/cctv13")
html.encoding="utf-8"

print html.text

fr = open("cctv_page.txt","w")
fr.write(html.text)
fr.close()
