#!/usr/bin/env python

#import necessary libraries
import subprocess as sp
import optparse as op

#create optparse instance
parser = op.OptionParser()

#create what user can enter
parser.add_option('-i', '--interface', dest='interface', help='This allows you to enter what interface to use, e.g. eth0')
parser.add_option('-m', '--mac', dest='mac_address', help='Enter new MAC address with correct format (e.g. 00:11:33:44:55:66)')

#collect user entries
(options, values) = parser.parse_args()

interface = options.interface
mac_address = options.mac_address

#execute subprocess module
sp.call(['ifconfig', interface, 'down'])
sp.call(['ifconfig', interface, 'hw', 'ether', mac_address])
sp.call(['ifconfig', interface, 'up'])
sp.call(['ifconfig', interface])
