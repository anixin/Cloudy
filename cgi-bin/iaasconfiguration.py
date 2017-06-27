#!/usr/bin/python2

import  cgi,cgitb,time
import  os,commands
from random import randint

cgitb.enable()

print  "content-type:text/html"
print  ""

y=cgi.FieldStorage()
os_name=y.getvalue('name')
ram_size=y.getvalue('ram_size')
cpu=y.getvalue('cpu_core')
hdd=y.getvalue('hdd_size')
port = y.getvalue('port')
os_path = "/root/Desktop/rhel7/rhel-server-7.2-x86_64-dvd.iso"

a=randint(7777,9999)


#This code below installs the os on the server's vm
print  commands.getoutput('sudo virt-install --name '+os_name+' --ram '+ram_size+' --vcpu '+cpu+' --nodisk --cdrom  '+os_path+'  --graphics vnc,listen=0.0.0.0,port='+port+'   --noautoconsole')

#it will launch the noVNC for client's acess through browser
print  commands.getoutput('sudo websockify -D '+ str(a)+' 192.168.122.1:'+port)

time.sleep(2)

print  "plz wait for os  "

#TODO change the link after test run
#This will provide the client with the link for redirection to server's vnc
print  "<a href='http://192.168.122.1/noVNC/vnc.html?host=192.168.122.1&port="+str(a)+"'target='_blank'> click here to access </a>"
