from scapy.all import *

dhcp_discover = Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandString(12,"0123456789abvdef"))/DHCP(options=[("message-type","discover"),"end"])
sendp(dhcp_discover, loop=1)