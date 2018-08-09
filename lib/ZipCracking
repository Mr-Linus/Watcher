import zipfile
import optparse
from threading import Thread


def ExtractFile(zFile, password):
    try:
        zFile.extractall(pwd=bytes(password.encode('utf-8')))
        print("[+] Found password "+password + '\n')

    except:
        pass


def main():
    parser = optparse.OptionParser("usage: ZipCracking.py "+"-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if options.zname == None or options.dname == None :
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        if line and not line.startswith('#'):
            password = line.strip()
            Thread(target=ExtractFile, args=(zFile, password)).start()


if __name__ == '__main__':
    main()