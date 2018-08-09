#!/usr/bin/env python3
# coding: utf-8
import os
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import  WordCompleter
print("""\n\033[1;32m -----欢迎使用极云监控系统----- \033[0m
\033[1;36m
██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗
██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
██║ █╗ ██║███████║   ██║   ██║     ███████║█████╗  ██████╔╝
██║███╗██║██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\033[0m
\033[32m
 常用命令:
 cpu disk memory ip net times shell run update install scan
 使用exit命令退出系统!\033[0m""")
Completer = WordCompleter(['BotNet', 'CrackPHPMyAdmin', 'DataForgery', 'FTPCracking',
                            'FTPSearch', 'PortScan-Native', 'exit', 'PortScan-Native',
                            'seo', 'SSHPasswordCracking', 'WebServiceAcquisition', 'WhoisQuery',
                            'ZipCracking'], ignore_case=True)

os.chdir("lib")
while True:
   # try:
        GetInput = prompt('Watcher:>')
        if str(GetInput) == "exit" or str(GetInput) == '^C':
            print("退出系统!")
            break
        if str(GetInput) == '':
            continue
        os.system(str(GetInput))
    #except:
    #    print("退出系统!")
    #    break
