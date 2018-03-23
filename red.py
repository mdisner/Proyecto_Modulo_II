#!/usr/bin/python

import netifaces
from prettytable import PrettyTable
import socket
from subprocess import call

tabla = PrettyTable(['Interfaz','IP','Subnent Mask','Gateway'])
print "\n################\nMonitoreo de Red\n################"

for x in netifaces.interfaces():
    #print x
    info = netifaces.ifaddresses(x)
    try:
        ip = netifaces.ifaddresses(x)[netifaces.AF_INET][0]['addr']
     #   print ip
    except Exception, err:
        ip = "No tiene IP asociada"
    try:    
        sub = netifaces.ifaddresses(x)[netifaces.AF_INET][0]['netmask']
      #  print sub
    except Exception, err:
        sub = "No tiene Subnet mask asociada"
    try:
        gw = netifaces.gateways()['default'][netifaces.AF_INET][0]
    except Exception, err:
        gw = "No tiene Gateway asociado"

    tabla.add_row([x,ip,sub,gw])

print tabla
print "\n##########################\nPuertos TCP/UDP en Escucha\n##########################"
call(["netstat","-lntu"])
print "\n###############################\nConexiones TCP/UDP Establecidas\n###############################"
call(["netstat","-ntu","|","grep","ESTABLISHED"])
print "\n##########################\nEstadisticas por Protocolo\n##########################"
call(["netstat","-st"])
print "\n##########################\nReglas de IPTABLES\n##########################"
call(["iptables","-L"])














