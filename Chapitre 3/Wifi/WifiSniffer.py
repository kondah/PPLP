from scapy.all import *

ap_list = []
iface = "wlan0mon"

def parsePacker(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                #print pkt.show()
                ap_list.append(pkt.addr2)
                print "BSSID : %s  --- SSID : %s "%(pkt.addr2, pkt.info)
                

while 1:
    sniff(iface=iface, prn=parsePacker, count=50, timeout=10)
