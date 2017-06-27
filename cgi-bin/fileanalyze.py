#!/usr/bin/python2

import cgi
import commands

print  "content-type:text/html"
print  ""

an = cgi.FieldStorage()
location=an.getvalue('flocation')

stat=commands.getstatusoutput("sudo hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount "+location+"   /res")
if stat[0]==0:
    print "Error in counting"
else:
    print " successfully counted"

#print commands.getoutput("sudo cat /result/")