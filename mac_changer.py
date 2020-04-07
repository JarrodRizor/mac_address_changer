#!/usr/bin/#!/usr/bin/env python

import subprocess
import argparse


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


args = get_arguments()
change_mac(args.interface, args.new_mac_address)