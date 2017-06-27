#!/usr/bin/python2

import cgi
import commands

print  "content-type:text/html"
print  ""

print commands.getoutput("sudo hadoop fs -lsr /user/")

print "\n\n"
print "<pre>"
print "<a href='http://192.168.122.1//mapreducetask.html'>" 
print "Enter the form here"
print "</a>"
print "</pre>"
