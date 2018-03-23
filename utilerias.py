#!/usr/bin/python

import subprocess
import pip

print "Instalacion de las utilerias necesarias\n"
print "Este script funciona para sistemas operativos compatibles con Debian 8-9\n"

print "Es necesario tener instalado Python en version 2.7\n"
print "Los modulos requiere tener instalado pip\n"

print "Por favor ejecute los siguientes comandos: \n"
print "sudo apt-get install build-essential \n"
print "sudo apt-get install python-pip \n"

try:

    subprocess.call(['pip', 'install', 'psutil'])
    subprocess.call(['pip', 'install', 'prettytable'])
    subprocess.call(['pip', 'install', 'netifaces'])

except Exception, err:
    print "Por favor ejecute los comandos mencionados"
















