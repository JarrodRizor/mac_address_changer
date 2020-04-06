#!/usr/bin/#!/usr/bin/env python

import subprocess
import optparse
import argparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interfact to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC Address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac_address = options.new_mac_address

print("[+] Changing MAC address for " + interface + " to " + new_mac_address)

subprocess.call(["ip", "link", "set", "dev", interface, "down"])
subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac_address])
subprocess.call(["ip", "link", "set", "dev", interface, "up"])
