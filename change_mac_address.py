#!/usr/bin/env python

import subprocess as sp
import optparse as op
import re

#define functions

def get_args():
	#instantiate object
	parser = op.OptionParser()
	#call method
	parser.add_option("-i", "--interface", dest="interface", help="This is to add the interface type, such as eth0")
	parser.add_option("-m", "--mac", dest="mac_address", help="This is to enter in the MAC information. Use proper sytax, e.g. 00:11:22:33:44:55. Example: -i eth0 -m 00:11:22:33:44:55")

	(options, values) = parser.parse_args()
	if not options.interface:
		#handle error
		parser.error("[-] An interface (e.g. eth0) must be specified.") 
	elif not options.mac_address:
		#handle error
		parser.error("[-] A MAC address must be specified (e.g. 22:11:1a:3b:44:55")
	else:
		return options

def change_mac(interface, mac_address):
	sp.call(["sudo", "ifconfig", interface, "down"])
	sp.call(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
	sp.call(["sudo", "ifconfig", interface, "up"])

def display_mac(interface):
	output_result = sp.check_output(["ifconfig", interface])

	reg_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output_result)
	if reg_search_result:
		return reg_search_result.group(0)
	else:
		print("[-] No MAC address to display, i.e. no MAC address found")

#call functions
options = get_args()
updated_mac = display_mac(options.interface)
print("Change MAC to: " + str(updated_mac))
change_mac(options.interface, options.mac_address)
updated_mac = display_mac(options.interface)

if updated_mac == options.mac_address:
	print("[+] The MAC address was successfully changed to: " + updated_mac)
else:
	print("[-] The MAC address was not changed. Please try again.")
