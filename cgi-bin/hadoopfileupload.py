#!/usr/bin/python2

import cgi
import commands

print  "content-type:text/html"
print  ""

page=cgi.FieldStorage()
filelocation=page.getvalue('fileaddress')
commands.getoutput("sudo hadoop fs -mkdir /user")
commands.getoutput("sudo hadoop dfsadmin -setSpaceQuota 600M /user")

commands.getoutput("sudo hadoop fs -put "+filelocation+"  hdfs://172.17.0.2:10005/user/")

print "File Uploaded Successfully" 

print "<pre>"
print "<a href='http://192.168.122.1/cgi-bin/mapreducetask.py'>" 
print "Click here to see your files"
print "</a>"
print "</pre>"