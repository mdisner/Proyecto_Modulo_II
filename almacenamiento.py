#!/usr/local/bin/python

import psutil
import os
from prettytable import PrettyTable
from psutil import virtual_memory

print("\n###########################\nMonitoreo de Almacenamiento\n###########################")
tabla = PrettyTable(['RAM Total (Bytes)','RAM  Libre (Bytes)','CPU Usado (%)','CPU Libre (%)'])

f = os.popen ("df -h")
for i in f.readlines():
    print i

mem = virtual_memory()

x = mem.total
w = mem.free
y = psutil.cpu_percent()
z = 100 - y

tabla.add_row([x,w,y,z])
print tabla









