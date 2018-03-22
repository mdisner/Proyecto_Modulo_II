#!/usr/local/bin/python

import netifaces
from prettytable import PrettyTable
#import re
#import pwd, grp

print "\n##########################\nMonitoreo de Autenticacion\n##########################\n"

tabla = PrettyTable(['USUARIO','IP ORIGEN','IP DESTINO','PUERTO','FECHA','HORA'])
tabla2 = PrettyTable(['FECHA','HORA','USUARIO INICIAL','USUARIO FINAL'])

for x in netifaces.interfaces():
    try:
        myip = netifaces.ifaddresses(x)[netifaces.AF_INET][0]['addr']
        #print myip
    except Exception, err:
        myip = "127.0.0.1"
        #print myip


with open('/var/log/auth.log','r') as f:
    for line in f:
        if "ssh2" in line:
            campos = line.split()
            tabla.add_row([campos[8],campos[10],myip,campos[12],campos[0] + campos[1],campos[2]])

        if "Successful su" in line:
            campos2 = line.split()
            tabla2.add_row([campos2[0] + campos2[1],campos2[2],campos2[8],campos2[10]])
            

print "\n###############################\nAutenticacion por Protocolo SSH\n###############################\n"
print tabla
print "\n###################\nAutenticacion Local\n###################\n"
print tabla2
