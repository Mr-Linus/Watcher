import re
import requests
import optparse
from colorama import Fore,Back,Style

def req(url,username,password):
    headers =  {
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    payload = {
        'pma_username':'{}'.format(username),
        'pma_password':'{}'.format(password),
        'server':'1',
    }
    res = requests.post(url,data=payload,headers=headers)
    return res

def option():
    usage = '%prog -h | --help'
    parser = optparse.OptionParser(usage = usage)
    parser.add_option("--url",dest="url",help="target url  usage: -url http://www.xxx.com/phpmyadmin")
    parser.add_option("--user",dest="username",help="username   usage: --user root")
    parser.add_option("--pass",dest="password",help="password path   usage: --pass /sqlsec/password.txt")
    (options, args) = parser.parse_args()
    return parser,options

def main():
    parser,args = option()
    try:
        res = req(args.url,args.username,'root')
        login_success = re.compile(r'opendb_url')
        success = login_success.search(res.text)

        if success:
            print(Fore.GREEN + "[+] PHPMyAdmin is vulerable")
        else:
            print(Fore.RED + "[*] PHPMyAdmin is not vulerable")
    except Exception as e:
        print(Fore.YELLOW + '执行异常{}'.format(e))
        parser.print_help()

if __name__ == '__main__':
    main()