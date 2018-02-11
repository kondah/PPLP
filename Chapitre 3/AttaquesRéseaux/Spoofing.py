import socket
from scapy.all import *


macsrc = "aa:aa:aa:aa:aa:aa"
macdst = "00:50:56:f2:f4:6d"
packet = Ether(src=macsrc, dst=macdst)/IP(dst='192.168.18.2', src='192.168.18.11')/TCP(dport=80, flags='S')
sendp(packet)

