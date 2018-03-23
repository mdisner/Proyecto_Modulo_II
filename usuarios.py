#!/usr/bin/python

import subprocess
import pwd, grp
import re
from prettytable import PrettyTable

print("\n#####################\nMonitoreo de Usuarios\n#####################")

tabla = PrettyTable(['USUARIO','GRUPO'])
tabla_lock = PrettyTable(['USUARIOS BLOQUEADOS'])
tabla_activos = PrettyTable(['USUARIOS ACTIVOS (LOGGED)'])


for p in pwd.getpwall():
    tabla.add_row([p[0],grp.getgrgid(p[3])[0]])
print tabla

lock = re.compile(".*:!\$")

with open('/etc/shadow') as f:
    for line in f:
        if lock.match(line):
            campos = line.split(":")
            tabla_lock.add_row([campos[0]])
print tabla_lock            
tabla_activos.add_row([subprocess.check_output("who").split()[0]])
print tabla_activos











