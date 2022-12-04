import logger as lg
import protect.core
import imports
import os

def init():
    os.system('iptables -N defence_syn_flood')
    os.system('iptables -A defence_syn_flood -s ' + imports.ip + ' --protocol tcp --tcp-flags SYN,ACK,FIN,RST SYN -j DROP')
    #iptables -I defence_syn_flood 1 -s <myip> --dport <forward> --protocol tcp --tcp-flags SYN,ACK,FIN,RST SYN -j DROP

def end():
    os.system('iptables -F defence_syn_flood')
    os.system('iptables -X defence_syn_flood')

if __name__ == '__main__':  
    init()

    loggers = []
    loggers.append(lg.logger(imports.syn_filter, imports.syn, imports.syn_dir))
    for logger in loggers:
        logger.run()

    protect.core.init()

    try:
        while True:
            protect.core.start()
    except:
        for logger in loggers:
            logger.stop()
        
        protect.core.stop()
    
    end()

