#!/usr/bin/env python3
# coding: utf-8
import os
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import  WordCompleter
print("""\n\033[1;32m -----欢迎使用观察者----- \033[0m
\033[1;36m
██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗
██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
██║ █╗ ██║███████║   ██║   ██║     ███████║█████╗  ██████╔╝
██║███╗██║██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\033[0m
\033[32m
 使用exit命令退出系统!\033[0m""")
Completer = WordCompleter(['BotNet', 'CrackPHPMyAdmin', 'DataForgery', 'FTPCracking',
                            'FTPSearch', 'PortScan-Native', 'exit', 'PortScan-NMAP',
                            'SEO', 'SSHPasswordCracking', 'WebServiceAcquisition', 'WhoisQuery',
                            'ZipCracking', 'PdfScan'], ignore_case=True)
List = ['BotNet', 'CrackPHPMyAdmin', 'DataForgery', 'FTPCracking',
                            'FTPSearch', 'PortScan-Native',  'PortScan-NMAP',
                            'SEO', 'SSHPasswordCracking', 'WebServiceAcquisition', 'WhoisQuery',
                            'ZipCracking', 'PdfScan']
os.chdir("lib")
while True:
    try:
        GetInput = prompt('Watcher:>', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(),
                          completer=Completer)
        if str(GetInput) == "exit" or str(GetInput) == '^C':
            print("退出系统!")
            break
        if str(GetInput) == '':
            continue
        if str(GetInput) == 'list':
            print("Command List:")
            for cmd in List:
                print("  - "+str(cmd))
            continue
        os.system("python3 "+str(GetInput))
    except:
        print("退出系统!")
        break
