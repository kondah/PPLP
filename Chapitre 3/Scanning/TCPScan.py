
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

SYN = IP(dst="192.168.18.161")/TCP(dport=80,flags='S')
print "Envoye"
SYN.display()

print "Reponse"
reponse = sr1(SYN, timeout=1,verbose=0)
reponse.display()

if int(reponse[TCP].flags) == 18:
    print "envoye"
    ACK = IP(dst="192.168.18.161")/TCP(dport=80, flags='A', ack=(reponse[TCP].seq + 1))
    reponse2 = sr1(ACK, timeout=1, verbose=0)
    ACK.display()
    print "Reponse"
    reponse2.display()
else :
    print "Pas de SYN-ACK"


