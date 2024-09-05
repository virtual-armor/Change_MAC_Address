#!/usr/bin/env python

import subprocess as sp
import optparse as op

#define functions

def get_args():
	#instantiate object
	parser = op.OptionParser()
	#call method
	parser.add_option('-i', '--interface', dest='interface', help='This is to add the interface type, such as eth0')
	parser.add_option('-m', '--mac', dest='mac_address', help='This is to enter in the MAC information. Use proper sytax, e.g. 00:11:22:33:44:55. Example: -i eth0 -m 00:11:22:33:44:55')

	(options, values) = parser.parse_args()
	if not options.interface:
		#handle error
		parser.error('[-] An interface (e.g. eth0) must be specified.') 
	elif not options.mac_address:
		#handle error
		parser.error('[-] A MAC address must be specified (e.g. 22:11:1a:3b:44:55')
	else:
		return options

def change_mac(interface, mac_address):
	sp.call(['sudo', 'ifconfig', interface, 'down'])
	sp.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac_address])
	sp.call(['sudo', 'ifconfig', interface, 'up'])
	print('\n')
	sp.call(['ifconfig', interface])

#call function
options = get_args()
change_mac(options.interface, options.mac_address)
