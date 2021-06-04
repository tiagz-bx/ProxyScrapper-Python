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
Title = "Proxy scrapper by tiagz join --> Private - Rewards discord.gg/wcJEZnW7aJ"
ctypes.windll.kernel32.SetConsoleTitleW(Title)
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.BLUE + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.RED + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.YELLOW + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.LIGHTMAGENTA_EX + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.BLUE + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ')
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.BLUE + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.RED + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.YELLOW + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.LIGHTMAGENTA_EX + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.BLUE + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ')
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.BLUE + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.RED + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.YELLOW + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.LIGHTMAGENTA_EX + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.BLUE + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ')
print(Fore.CYAN + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.BLUE + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.RED + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
time.sleep(1)
os.system('cls')
print(Fore.LIGHTBLACK_EX + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.LIGHTMAGENTA_EX + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.BLUE + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.LIGHTMAGENTA_EX + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ') 
print(Fore.LIGHTBLACK_EX + 'For other tools join --> Private - Rewards discord.gg/wcJEZnW7aJ')    

def get_proxies(type_proxy):
    r = requests.get(url + type_proxy)

    text = r.text
    text = text.replace("\n","")

    with open (f"./output/{type_proxy}.txt","w") as f:
        f.write(text)


    lines = 0
    with open(f'./output/{type_proxy}.txt', 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()
            print('Scraped {} '.format(lines) + 'proxies.')
url = "https://api.proxyscrape.com/?request=getproxies&timeout=3000&country=all&ssl=all&anonymity=all&proxytype="  

print("")
print("")
print(Fore.WHITE + """
                                                                                  
		 █████╗ ██████╗ ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗    
		██╔══██╗██╔══██╗██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗   
		███████║██████╔╝██║    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝   
		██╔══██║██╔═══╝ ██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗   
		██║  ██║██║     ██║    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║   
		╚═╝  ╚═╝╚═╝     ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   
                                                                                  
""")
print("")
type_proxy = input('                                    ' + Fore.LIGHTRED_EX + '[http]' + Fore.LIGHTYELLOW_EX + '-' + Fore.LIGHTBLACK_EX + '[https]' + Fore.LIGHTYELLOW_EX + '-' + Fore.LIGHTRED_EX + '[socks4]' + Fore.LIGHTYELLOW_EX + '-' + Fore.LIGHTBLACK_EX + '[socks5]' + Fore.LIGHTYELLOW_EX + ':'   + Fore.LIGHTBLACK_EX + '\n\n  </> ')


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