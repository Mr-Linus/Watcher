from pexpect import pxssh
import re
botNet = []


class Client:
    def __init__(self, host, port, user, password):
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(server=self.host, username=self.user, password=self.password, port=self.port)
            return s
        except Exception:
            print("[-]: BotServer:"+self.host+" Offline.")
            return 0

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(command):
    for client in botNet:
        if client.connect() != 0:
            print("[+]: BotServer: " + client.host + " Online.")
            output = client.send_command(command)
            print("[*] Output From:"+client.host+": ", end='')
            print("[+]:"+output.decode("utf-8"))

def addClient(host, port, user, password):
    client = Client(host, port, user, password)
    botNet.append(client)


def addBot():
    f = open('bot.txt')
    for item in f.readlines():
        item = item.strip()
        para = re.split(' ', item)
        if item and not item.startswith('#'):
            addClient(para[0], para[1], para[2], para[3])
    f.close()
    return 0


addBot()
botnetCommand('uname -a')
