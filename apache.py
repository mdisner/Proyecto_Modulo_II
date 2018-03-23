#!/usr/bin/python

from subprocess import call

print "\n################\nMpnitoreo Apache\n################\n"
print "\n##################\nVHosts Habilitados\n##################\n"
call(['apachectl','-S'])
print "\n##################\nModulos Habilitados\n##################\n"
call(['apachectl','-M'])








