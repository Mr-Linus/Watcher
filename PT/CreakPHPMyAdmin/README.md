# install requirements
```shell
pip3 install -r requirements.txt
```

or

```shell
pipenv install
pipenv shell
```

# usage

```r
Usage: creakmysql.py -h | --help

Options:
  -h, --help       show this help message and exit
  --url=URL        target url  usage: -url http://www.xxx.com/phpmyadmin
  --user=USERNAME  username   usage: --user root
  --pass=PASSWORD  password path   usage: --pass /sqlsec/password.txt
```

# 使用效果
本次测试的环境是phpstudy下的phpmyadmin，目前就爆破的速度来看有点慢，希望自己后期学了多线程后可以提高爆破的速度。
![](http://image.3001.net/images/20180709/15311358833281.png)  