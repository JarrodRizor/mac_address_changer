#!/usr/bin/#!/usr/bin/env python

import subprocess

interface = input("interface > ")
new_mac_address = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac_address)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
subprocess.call(["ifconfig", interface, "up"])
