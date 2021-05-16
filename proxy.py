# Author : NAOY-TIAGZ
# Discord : NAOY#0001 </> TIAGZ#0001
# Github : https://github.com/NAOYY ... https://github.com/tn-nt
#module
from urllib.request import Request, urlopen
from base64 import b64decode
import requests
import urllib
import ctypes
import webbrowser
import os 
import shlex
import time
import json
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()
#module début du script

print(Fore.CYAN + 'WELCOME TO THE NSI SCRAPER ITS A PROXY SCRAPER USED API KEY MADE BY NAOY#0001 AND </> TIAGZ-UHQ#0001') 
time.sleep(1) # Sleep for 3 seconds
os.system('cls')

def get_proxies(type_proxy):
    r = requests.get(url + type_proxy)

    text = r.text
    text = text.replace("\n","")

    # EXPORT PROXYS
    with open (f"./output/{type_proxy}.txt","w") as f:
        f.write(text)


    lines = 0
    with open(f'./output/{type_proxy}.txt', 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()
            print('Scraped {} '.format(lines) + 'proxies.')
    

# Proxysscrape
url = "https://api.proxyscrape.com/?request=getproxies&timeout=100&country=all&ssl=all&anonymity=all&proxytype="
# Proxyslist
# ProxyScrape2


print("                                                                                      ╔═══════════════╗ ")
print("                                                                                         Version 1.0    ")
print("                                                                                      ╚═══════════════╝ ")                                                                                                                                                                                
                                                                                        

print("""
		██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗███████╗ ██████╗██████╗  █████╗ ██████╗ 
		██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗
		██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████╗██║     ██████╔╝███████║██████╔╝
		██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ 
		██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ███████║╚██████╗██║  ██║██║  ██║██║     
		╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     
		                                                                                  
		 █████╗ ██████╗ ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗    
		██╔══██╗██╔══██╗██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗   
		███████║██████╔╝██║    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝   
		██╔══██║██╔═══╝ ██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗   
		██║  ██║██║     ██║    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║   
		╚═╝  ╚═╝╚═╝     ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   
                                                                                  
""")
type_proxy = input("                [http] - [https] - [socks4] - [socks5]:   \n\n >> ")


#HTTP
if type_proxy == "http" or type_proxy.lower() == "http":
    get_proxies("http")


#HTTPS
elif type_proxy == "https" or type_proxy.lower() == "https":
    get_proxies("https")


#SOCKS4
elif type_proxy == "socks4" or type_proxy.lower() == "socks4":
    get_proxies("socks4")


#SOCKS5
elif type_proxy == "SOCKS5" or type_proxy.lower() == "socks5":
    get_proxies("socks5")
