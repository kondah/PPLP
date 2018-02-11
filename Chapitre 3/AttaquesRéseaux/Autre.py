from scapy.all import *


send(IP(dst="198.221.192.158", ihl=2, version=5)/ICMP())
