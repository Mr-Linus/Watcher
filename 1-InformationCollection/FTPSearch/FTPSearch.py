import ftplib
import optparse
import re


def SearchPage(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    reList = []
    for fileName in dirList:
        fn = fileName.lower()
        if ('.php' in fn) or ('.htm' in fn) or ('.asp' in fn):
            print("[+] Found page: "+fileName)
            reList.append(fileName)
        elif ('www' in fn) or ('ht' in fn) or ('doc' in fn) or ('page' in fn) or ('host' in fn):
            print("[+] Found directory : " + fileName)
            reList.append(fileName)
        elif ('.sql' in fn):
            print("[+] Found Database :" + fileName)
        elif ('.tar' in fn) or ('.zip' in fn) or ('.7z' in fn):
            print("[+] Found Compressed file: "+fileName)
    return reList

def ListPage(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return

def main():
    parser = optparse.OptionParser('usage: FTPSearchPage.py -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    if (options.tgtHost == None) and (options.tgtPort == None):
        print(parser.usage)
        exit(0)
    elif (options.tgtHost != None) and (options.tgtPort == None):
        port = 21
    else:
        port=options.tgtPort
    host = options.tgtHost
    ftp = ftplib.FTP(host)
    ftp.port=port
    f = open('accounts.txt')
    for item in f.readlines():
        item = item.strip()
        para = re.split(' ', item)
        if item and not item.startswith('#'):
            try:
                ftp.login(para[0],para[1])
            except:
                print("[-] FTP login Error!")
            SearchPage(ftp)
    f.close()



if __name__ == '__main__':
    main()
