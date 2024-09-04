#!/usr/bin/env python

import subprocess as sp
import optparse as op

#define function
def change_mac(interface, mac_address):
	sp.call(['ifconfig', interface, 'down'])
	sp.call(['ifconfig', interface, 'hw', 'ether', mac_address])
	sp.call(['ifconfig', interface, 'up'])
	sp.call(['ifconfig', interface])

parser = op.OptionParser()

parser.add_option('-i', '--interface', dest='interface', help='This is to add the interface type, such as eth0')
parser.add_option('-m', '--mac', dest='mac_address', help='This is to enter in the MAC information. Use proper sytax, e.g. 00:11:22:33:44:55. Example: -i eth0 -m 00:11:22:33:44:55')

(options, values) = parser.parse_args()

#call function
change_mac(options.interface, options.mac_address)
