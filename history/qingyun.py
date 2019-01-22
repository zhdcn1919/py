#!/urs/bin/env python
#-*-coding:utf8-*-

import requests
import re

#下面三行是编码转换的功能，大家现在不用关心。
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

html = requests.get('http://tieba.baidu.com/f?kw=庆云&ie=utf-8&pn=0')
#html = requests.get('http://tieba.baidu.com/f?kw=%C7%EC%D4%C6&fr=ala0&tpl=5')

html.encoding = 'utf-8' #将编码转为utf-8FA防止中文乱码。

f = open('w.txt','w')
f.write(html.text)

title = re.findall('class="j_th_tit">(.*?)</a>',html.text,re.S)
# title = re.findall('class="j_th_tit ">(.*?)</a>',html.text,re.S)
#title = re.findall('target="_blank">(.*?)</a>',html.text,re.S)


for TITLE in title:
    print TITLE
#    f.write(TITLE)
 #   f.write('\n')
