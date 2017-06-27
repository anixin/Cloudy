#!/usr/bin/python2

import commands,os
from random import randint
import cgi

print  "content-type:text/html"
print  ""
a=randint(7777,9999)
page=cgi.FieldStorage()

lang = page.getvalue('n')
print lang
if lang=='py' :
    test = commands.getstatusoutput("sudo docker run -itd -p "+str(a) +":4200  new/shell ")
    print " your interpreter is loading "
    print "<a href = 'https://192.168.122.1:"+str(a)+"'>"
    print " click here for python"
    print "</a>"


