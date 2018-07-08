import nmap
import optparse
from threading import Thread
## you must install nmap in your PC before you run the python program

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    results = nmScan.scan(tgtHost, tgtPort)
    if nmScan[list(results['scan'].keys())[0]]['tcp'][int(tgtPort)]['state'] == 'closed':
        return False
    else:
        print('[*] Port:' + str(tgtPort) + ' Open')
        return True


def main():
    parser = optparse.OptionParser('usage: PortScan-NMAP.py -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host,it must be a ip address.')
    parser.add_option('-p', dest='tgtPorts', type='string', help='specify target port[s], separated by \',\' or \'-\'')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    if ("," in options.tgtPorts) and ("-" not in options.tgtPorts):
        tgtPorts = str(options.tgtPorts).split(',')
    elif (", " not in options.tgtPorts) and ("-" in options.tgtPorts):
        (sPort, ePort) = options.tgtPorts.split('-')
        tgtPorts = list(range(int(sPort), int(ePort)+1))
    else:
        print("specify target port[s] Error!")
        exit(1)
    if tgtHost == None or tgtPorts == None:
        print(parser.usage)
        exit(0)
    for tgtPort in tgtPorts:
        Thread(target=nmapScan, args=(tgtHost, str(tgtPort))).start()


if __name__ == '__main__':
    main()

