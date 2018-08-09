import optparse
import builtwith

def main():
    parser = optparse.OptionParser('usage:  WebServiceAcquisition.py -H <target host> ')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    if tgtHost == None:
        print(parser.usage)
        exit(0)
    if (not tgtHost.startswith('https://')) and (not tgtHost.startswith('http://')):
        tgtHost1 = 'http://'+tgtHost
        tgtHost2 = 'https://'+tgtHost
    elif tgtHost.startswith('https://'):
        tgtHost2 = tgtHost
        tgtHost1 = 'http://'+tgtHost.replace('https://', '')
    elif tgtHost.startswith('http://'):
        tgtHost1 = tgtHost
        tgtHost2 = 'https://'+tgtHost.replace('http://', '')
    print('Receive From HTTP Protocol:')
    try:
        resultsHTTP = builtwith.parse(tgtHost1)
        for resultHTTP in resultsHTTP:
            print(resultHTTP+': '+str(resultsHTTP[resultHTTP]))
    except Exception:
        print("The Target does not support HTTP.")

    print('Receive From HTTPS Protocol:')
    try:
        resultsHTTPS = builtwith.parse(tgtHost2)
        for resultHTTPS in resultsHTTPS:
            print(resultHTTPS + ': ' + str(resultsHTTPS[resultHTTPS]))
    except Exception:
        print('The Target does not support HTTPS')


if __name__ == '__main__':
    main()