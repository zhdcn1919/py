# -*- coding: utf-8 -*-

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    str1 = raw_input("请输入进入的吧：")
    tieba = requests.get("http://tieba.baidu.com/f?kw="+str1)
    #
    #print tieba.text
    #
    fr = open('src_tieba.txt','w')
    fr.write(tieba.text)
    fr.close()
    #
    author = re.findall(u'主题作者: (.*?)"',tieba.text,re.S)
    title = re.findall('class="j_th_tit ">(.*?)</a>',tieba.text,re.S)
    time = re.findall(u'"创建时间">(.*?)</span>',tieba.text,re.S)
    link = re.findall(r'<a href="/p/(.*?)" title="',tieba.text,re.S)

    # 把用户名中含有字符串的字符长度减半。
    def bgetlen(n):
        str_cut = re.findall('[0-9a-zA-Z_]',n,re.S)
        str2 = len(str_cut)/2
        alen = len(n)-len(str_cut)+str2
        return alen

    for (c,a,l,t) in zip(time,author,link,title):
        a = a.replace("℡","℡ ") # 把℡ 替换成℡  。
        a = a.replace("♂","♂ ")
        a = a.replace(".",". ")
        l = 'http://tieba.baidu.com/p/'+l
        if(bgetlen(a)==0):
            print c+'\t'+'         '+'\t'+l+'\t'+t
        elif(bgetlen(a)<=2):
            print c+'\t'+a+' '+' '+'    \t'+l+'\t'+t
        elif(bgetlen(a)<=4):
            print c+'\t'+a+'    \t'+l+'\t'+t
        else:
            print c+'\t'+a+'\t'+l+'\t'+t

if __name__=='__main__':
    main();
