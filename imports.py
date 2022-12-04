from scapy.all import *

from scapy.layers.inet import IP, TCP

ip = get_if_addr(conf.iface)

delay = 5

def syn(filename:str, packet:Packet)->None:
    while True:
        try:
            fd = open(filename, 'a+')
            fd.write(packet[IP].src     + ' ')
            fd.write(packet[TCP].seq    + ' ')
            fd.write(packet[TCP].sport  + ' ')
            fd.write(packet[TCP].dport  + '\n')
            fd.close()
            break
        except:
            pass

syn_dir = 'syn'
syn_filter = 'dst host %s and tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-push) == tcp-syn'%ip

syn_drop_filter = 'src host %s and dst host %s and tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-push) == tcp-syn | tcp-ack'
