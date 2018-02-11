from scapy.all import *

ans, unans = sr(IP(dst="192.168.18.161")/TCP(dport=[80,21],flags="A"))

for s, r in ans:
    if s[TCP].dport == r[TCP].sport:
        print "port non filtre : ", s[TCP].dport