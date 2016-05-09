# -*- coding: utf-8 -*-

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

tieba = requests.get("http://tieba.baidu.com/f?kw=庆云")

print tieba.text

fr = open('tieba.txt','w')
fr.write(tieba.text)
fr.close()

author = re.findall(u'主题作者: (.*?)"',tieba.text,re.S)
title = re.findall('class="j_th_tit ">(.*?)</a>',tieba.text,re.S)
time= re.findall(u'"创建时间">(.*?)</span>',tieba.text,re.S)

for (c,a,t) in zip(time,author,title):
    if(len(a)<4):
        a = a+'       '
        print c+'\t'+a+"  \t"+t
    else:
        print c+"\t"+a+'\t'+t
