import socket
import sys
import time

import os
from struct import *


def checksum(msg):
    s = 0

    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = msg[i] + (msg[i + 1] << 8)
        s += + w

    s += (s >> 16)

    # complement and mask to 4 byte short
    return ~s & 0xffff


def get_ip_header(source_ip, dest_ip):
    # ip header fields
    ip_ihl = 5
    ip_ver = 4
    ip_tos = 0
    ip_tot_len = 0  # kernel will fill the correct total length
    ip_id = 54321  # Id of this packet
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = socket.IPPROTO_TCP
    ip_check = 0  # kernel will fill the correct checksum
    ip_saddr = socket.inet_aton(source_ip)  # spoof source ip
    ip_daddr = socket.inet_aton(dest_ip)

    ip_ihl_ver = (ip_ver << 4) + ip_ihl

    # the ! in the pack format string means network order
    return pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len, ip_id,
                ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr,
                ip_daddr)


def get_tcp_header(source_ip, tcp_source, dest_ip, tcp_dest, user_data):
    # tcp header fields
    tcp_seq = 1
    tcp_ack_seq = 1
    tcp_doff = 5  # 4 bit field, size of tcp header, 5 * 4 = 20 bytes

    # tcp flags
    tcp_fin = 0
    tcp_syn = 1
    tcp_rst = 0
    tcp_psh = 0
    tcp_ack = 1
    tcp_urg = 0
    tcp_window = socket.htons(5840)  # maximum allowed window size
    tcp_check = 0
    tcp_urg_ptr = 0

    tcp_offset_res = (tcp_doff << 4) + 0
    tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + \
                (tcp_psh << 3) + (tcp_ack << 4) + (tcp_urg << 5)

    # the ! in the pack format string means network order
    tcp_head = pack('!HHLLBBHHH', tcp_source, tcp_dest, tcp_seq,
                    tcp_ack_seq, tcp_offset_res, tcp_flags,
                    tcp_window, tcp_check, tcp_urg_ptr)

    # pseudo header fields
    source_address = socket.inet_aton(source_ip)
    dest_address = socket.inet_aton(dest_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_head) + len(user_data)

    psh = pack('!4s4sBBH', source_address, dest_address, placeholder,
               protocol, tcp_length)
    psh = psh + tcp_head + user_data

    tcp_check = checksum(psh)
    # print tcp_check

    # make the tcp header again and fill the correct checksum
    # remember checksum is NOT in network byte order
    return pack('!HHLLBBH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq,
                tcp_offset_res, tcp_flags, tcp_window) + \
           pack('H', tcp_check) + pack('!H', tcp_urg_ptr)


def tcp_ack(source_ip, tcp_source, dest_ip, tcp_dest):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except socket.error as msg:
        print('Socket could not be created. Error : %s' % msg)
        sys.exit()

    user_data = b''

    head_ip = get_ip_header(source_ip, dest_ip)
    head_tcp = get_tcp_header(source_ip, tcp_source, dest_ip,
                              tcp_dest, user_data)

    # final full packet - syn packets dont have any data
    packet = head_ip + head_tcp + user_data

    # Send the packet finally - the port specified has no effect
    s.sendto(packet, (dest_ip, 0))  # put in loop to flood the target
    s.close()
    time.sleep(0.1)


if __name__ == '__main__':
    data = os.popen("netstat -tulnap -4 | grep CLOSE_WAIT | "
                    "awk '{print $4,$5}' |  sed 's/:/ /g'", 'r').read()

    for line in data.split('\n'):
        values = line.split(" ")

        if len(values) > 1:
            print("src : " + values[0] + ":" + values[1] +
                  " dst : " + values[2] + ":" + values[3])

            tcp_ack(values[0], int(values[1]), values[2], int(values[3]))

    sys.exit()