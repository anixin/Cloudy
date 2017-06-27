#!/usr/bin/env python2

import commands ,cgi, time

print  "content-type:text/html"
print  ""


ss = cgi.FieldStorage()
software_name=ss.getvalue("softts")

commands.getoutput("sudo touch saasclient.py")
commands.getoutput("sudo chmod 777 saasclient.py")


f = open("saasclient.py",'w')
f.write("#!/usr/bin/python2\n")
f.write("import commands\n")
f.write(("commands.getstatusoutput('ssh -X root@192.168.2.19 " + software_name + " ') \n"))

f.close()

time.sleep(4)

commands.getoutput("sudo tar -cvf saasclient.tar saasclient.py")
commands.getoutput("sudo cp -rvf saasclient.tar /var/www/html/")

print "<META HTTP-EQUIV=refresh CONTENT='0 ; URL=http://192.168.122.1/saasclient.tar\n'>"