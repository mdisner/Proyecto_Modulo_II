#!/usr/bin/python

import subprocess
from prettytable import PrettyTable
print "\n#####################\nMonitoreo de Procesos\n#####################"
tabla = PrettyTable(['USER','PID','%CPU','%MEM','COMMAND'])
ps = subprocess.Popen(('ps', 'aux'), stdout=subprocess.PIPE)
output = ps.communicate()[0]
for line in output.split('\n'):
        col = line.split( )
        try:
            tabla.add_row([col[0],col[1],col[2],col[3],col[10]])
        #    print col[0], col[1], col[2], col[3], col[10]
        #except Exception, err:
        #    print ""
        except Exception, err:
            print ""
print tabla















