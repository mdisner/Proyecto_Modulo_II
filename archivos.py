#!/usr/local/bin/python

import psutil
import os
from subprocess import call
from prettytable import PrettyTable
print "\n#####################\nMonitoreo de Archivos\n#####################"

tabla = PrettyTable(['ARCHIVO'])

for line in call(["lsof"]):
    tabla.add_row([line[0]])
print tabla    
    












