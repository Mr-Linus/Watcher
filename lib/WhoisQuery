import optparse
import whois
def main():
    parser = optparse.OptionParser('usage:  WebServiceAcquisition.py -H <target domain> ')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target domain')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    if tgtHost == None:
        print(parser.usage)
        exit(0)
    if (not tgtHost.startswith('https://')) and (not tgtHost.startswith('http://')):
        domain = tgtHost
    elif tgtHost.startswith('https://'):
        domain = tgtHost.replace('https://', '')
    elif tgtHost.startswith('http://'):
        domain = tgtHost.replace('http://', '')
    print('Receive From Whois:')
    try:
        results = whois.whois(domain)
        for result in results:
            print(result+': '+str(results[result]))
    except Exception:
        pass


if __name__ == '__main__':
    main()