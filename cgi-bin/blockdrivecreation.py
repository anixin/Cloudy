#!/usr/bin/python2

import  cgi
import  commands,time

print  "content-type:text/html"
print  ""

b=cgi.FieldStorage()
blockdrivename=b.getvalue('blockdrivename')
blockdrivesize=b.getvalue('blockdrivesize')
print blockdrivesize

#LV creating for the available storage
a = commands.getstatusoutput("sudo lvcreate --size " + blockdrivesize+"M --name " + blockdrivename + " myvg" )
print a
if a[0]==0:
    # conf file changes with ign 
    blockcreatingfile = open('/etc/tgt/targets.conf','a')
    blockcreatingfile.write('<target ' +  blockdrivename+'>\n     backing-store /dev/myvg/'+blockdrivename+'\n</target>\n')
    blockcreatingfile.close()
else:
    print "Error in lv creation"

commands.getoutput("sudo systemctl restart tgtd")
commands.getoutput("sudo iptables -F")
commands.getoutput("sudo setenforce 0")


#client side

commands.getoutput("sudo touch clientblockstorage.py")
commands.getoutput("sudo chmod 777 clientblockstorage.py")

## Writing in the client side copy 

f = open("clientblockstorage.py",'w')
f.write("#!/usr/bin/python2\n")
f.write("import commands,os\n")
f.write("a = commands.getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.2.19 --discover')\n")
f.write("b=commands.getstatusoutput('iscsiadm --mode node --targetname " + blockdrivename + " --portal 192.168.2.19:3260 --login') \n")
f.write("print a\n")
f.write("print b")
f.close()
time.sleep(4)

commands.getstatusoutput("sudo tar -cvf clientblockstorage.tar clientblockstorage.py")
commands.getstatusoutput("sudo cp -rvf clientblockstorage.tar /var/www/html/")

print   "<META HTTP-EQUIV=refresh CONTENT='0 ; URL=http://192.168.2.19/clientblockstorage.tar\n'>"


