import imports
import os

drop_all_syn = '-d %s --protocol tcp --tcp-flags SYN,RST,ACK,FIN SYN -j DROP'%imports.ip
os.system('iptables -I INPUT 1 %s'%drop_all_syn)