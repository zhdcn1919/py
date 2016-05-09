# -*- coding: utf-8 -*-

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

tieba = requests.get("http://tieba.baidu.com/f?kw=庆云")

print tieba.text

fr = open('src_tieba.txt','w')
fr.write(tieba.text)
fr.close()

author = re.findall(u'主题作者: (.*?)"',tieba.text,re.S)
title = re.findall('class="j_th_tit ">(.*?)</a>',tieba.text,re.S)
time= re.findall(u'"创建时间">(.*?)</span>',tieba.text,re.S)

def bgetlen(n):
    str_cut = re.findall('[0-9a-zA-Z]',n,re.S)
    str2 = len(str_cut)/2
    alen = len(n)-len(str_cut)+str2
    return alen

for (c,a,t) in zip(time,author,title):
    if(bgetlen(a)<4):
        print c+'\t'+a+'  \t'+t
    else:
        print c+'\t'+a+'\t'+t
