#!/usr/bin/python
#coding:utf-8
import sys
import urllib
import re

reload(sys)
sys.setdefaultencoding( "utf-8" )
domain = 'www.baidu.com'
r = urllib.urlopen('http://wap.ip138.com/ip.asp?ip=%s'%domain)
fip=r.read()
rip=re.compile(r"<br/><b>查询结果：(.*)</b><br/>")
result=rip.findall(fip)
print "%s\t %s" %(domain,result[0])
print "---------------------------"
