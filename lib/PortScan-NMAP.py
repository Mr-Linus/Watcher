import nmap
import optparse
from threading import Thread
import socket
## you must install nmap in your PC before you run the python program


def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    results = nmScan.scan(tgtHost, tgtPort)
    # ipaddr = list(results['scan'].keys())[0]
    # print(nmScan[socket.gethostbyname(tgtHost)]['tcp'][int(tgtPort)]['state'])
    if nmScan[socket.gethostbyname(tgtHost)]['tcp'][int(tgtPort)]['state'] == 'closed':
        return False
    else:
        print('[*] Port:' + str(tgtPort) + ' Open')
        return True


def main():
    parser = optparse.OptionParser('usage: PortScan-NMAP.py -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string', help='specify target port[s], separated by \',\' or \'-\'')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    if (tgtHost == None) or (options.tgtPorts == None):
        print(parser.usage)
        exit(0)
    if ("," in options.tgtPorts) and ("-" not in options.tgtPorts):
        tgtPorts = str(options.tgtPorts).split(',')
    elif (", " not in options.tgtPorts) and ("-" in options.tgtPorts):
        (sPort, ePort) = options.tgtPorts.split('-')
        tgtPorts = list(range(int(sPort), int(ePort)+1))
    elif options.tgtPorts.isdigit() and (int(options.tgtPorts) > 0) and (int(options.tgtPorts) <= 65535):
        nmapScan(tgtHost, options.tgtPorts)
        exit(0)
    else:
        print("specify target port[s] Error!")
        exit(1)
    for tgtPort in tgtPorts:
        Thread(target=nmapScan, args=(tgtHost, str(tgtPort))).start()


if __name__ == '__main__':
    main()

