#!/usr/bin/env python

import sys

device = "eth0"
prefix = "44";
source_file = "/sys/class/net/" + device + "/address"

def convertToInteger(hexa):
    return str(int("0x" + hexa, 16))

try:
    f = open(source_file, "r")
except:
    sys.exit(1)

mac = f.readline().strip()

tokens = mac.split(':')

ip = prefix + "." + convertToInteger(tokens[3]) + "." + convertToInteger(tokens[4]) + "." + convertToInteger(tokens[5])

print ip
