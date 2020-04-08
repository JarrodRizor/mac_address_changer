#!/usr/bin/#!/usr/bin/env python

import subprocess
import argparse
import re


def get_arguments():
    parser = argparse.ArgumentParser("Change Mac Address")
    parser.add_argument("-i", "--interface", metavar="", required=True, dest="interface",
                        help="Select Interface you wish to change MAC Address on.")
    parser.add_argument("-m", "--mac", metavar="", required=True, dest="new_mac_address",
                        help="What you would like the MAC Address to be.")
    return parser.parse_args()


def change_mac(interface, new_mac_address):
    print("[+] Changing MAC address for " + interface + " to " + new_mac_address)
    subprocess.call(["ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac_address])
    subprocess.call(["ip", "link", "set", "dev", interface, "up"])


def get_current_mac(interface):
    iplink = subprocess.check_output(["ip", "link", "show", interface]).decode("utf-8")
    mac_address_search_result = re.search(r"([0-9a-fA-F]:?){12}", iplink)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


print("Current MAC = " + str(get_current_mac(get_arguments().interface)))

change_mac(get_arguments().interface, get_arguments().new_mac_address)

current_mac = get_current_mac(get_arguments().interface)

if current_mac == get_arguments().new_mac_address:
    print("[+} MAC Address was successfully changed to " + get_arguments().new_mac_address)
else:
    print("[-] MAC address did not change.")
