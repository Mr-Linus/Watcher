import optparse
import pygeoip

gi = pygeoip.GeoIP('../etc/GeoLiteCity.dat')


def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    print("Target: "+tgt+" Geo-Located.")
    print("City: "+str(rec['city']))
    print("Country: "+str(rec['country_name']))
    print("Longitude: "+str(rec['longitude'])+" Latitude: "+str(rec['latitude']))
    print("Region code: "+str(rec['region_code']))
    print("Time zone: "+str(rec['time_zone']))


def main():
    parser = optparse.OptionParser('usage:  GeoIP.py -H <target host> ')
    parser.add_option('-H', dest='host', type='string', help='specify target Host')
    (options, args) = parser.parse_args()
    Host = options.host
    if Host == None:
        print(parser.usage)
        exit(0)
    else:
        printRecord(Host)
        exit(1)


if __name__ == '__main__':
    main()
