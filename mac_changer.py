#!/usr/bin/#!/usr/bin/env python

import subprocess

interface = "enp0s3"
new_mac_address = "00:01:02:03:04:05"
print("[+] Changing MAC address for " + interface + " to " + new_mac_address)

# subprocess.call("ip link set interface down", shell=True)
# subprocess.call("ip link set interface address 00:01:02:03:04:05", shell=True)
# subprocess.call("ip link set interface up", shell=True)
