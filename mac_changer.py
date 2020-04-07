#!/usr/bin/#!/usr/bin/env python

import subprocess
import argparse

#Create Parser object to store Arguments in
parser = argparse.ArgumentParser("Change Mac Address")

# Parser Arguments values
parser.add_argument("-i", "--interface", metavar="", required=True, dest="interface",
                    help="Select Interface you wish to change MAC Address on.")
parser.add_argument("-m", "--mac", metavar="", required=True, dest="new_mac_address",
                    help="What you would like the MAC Address to be.")

args = parser.parse_args()

#Storing data given from CLI Arguments
interface = args.interface
new_mac_address = args.new_mac_address

print("[+] Changing MAC address for " + interface + " to " + new_mac_address)

# Executing IP Command to take down interface, change MAC Address and put it back up.
subprocess.call(["ip", "link", "set", "dev", interface, "down"])
subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac_address])
subprocess.call(["ip", "link", "set", "dev", interface, "up"])
