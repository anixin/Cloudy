#!/usr/bin/python2

import commands as cmd

iplist =cmd.getstatusoutput("sudo nmap -sS -n 192.168.0/24 | grep -i report | cut -d' ' -f5")

cmd.getstatusoutput("sudo touch iplist.txt")

fileiplist = open('iplist.txt','w')
fileiplist.write(iplist)
fileiplist.close()

cmd.getstatusoutput="sudo touch hdfs-site.xml"
filehdfssite = open('hdfs-site.xml','w')

## TODO hdfs-site.xml entry
# filehdfssite.write('')

cmd.getstatusoutput="sudo touch core-site.xml"
filecoresite = open('core-site.xml','w')

## TODO core-site.xml entry
#filecoresite.write('')

#Transferring the two files to datanode's system
for ips in fileiplist :
    cmd.getstatusoutput("sudo scp hdfs-site.xml root@"+ips+":/etc/hadoop/") 
    cmd.getstatusoutput("sudo scp core-site.xml root@"+ips+":/etc/hadoop/")