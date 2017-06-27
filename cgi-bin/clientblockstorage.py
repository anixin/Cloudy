#!/usr/bin/python2
import commands,os
a = commands.getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.2.19 --discover')
b=commands.getstatusoutput('iscsiadm --mode node --targetname awk --portal 192.168.2.19:3260 --login') 
print a
print b