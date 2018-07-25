import threadpool
import time
from socket import *

balance = 0


def portScanner(port):
    global ip
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((ip, port))
        print('[+] %d Open' % port)
        s.close()
    except:
        pass


ip = input("IP:")
sPort = int(input('Start:'))
ePort = int(input('End:'))
ePort += 1
print("Start Scanning:")
start_time = time.time()
pool = threadpool.ThreadPool(10)
reqs = threadpool.makeRequests(portScanner, [x for x in range(sPort, ePort)])
[pool.putRequest(x) for x in reqs]
pool.wait()
print('Scanning Complete!')
print("Used：{} sec.".format(time.time()-start_time))
