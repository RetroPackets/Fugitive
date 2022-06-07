
import requests, os, colorama
from sys import argv
import urllib3
from os import system as terminal
import requests
from colorama import Fore,Style
import time

os.system("clear")
print(f"""

             {Fore.WHITE}░█▀▀▀ █──█ █▀▀▀ ─▀─ ▀▀█▀▀ ─▀─ ▀█─█▀ █▀▀ 
             {Fore.RED}░█▀▀▀ █──█ █─▀█ ▀█▀ ──█── ▀█▀ ─█▄█─ █▀▀ 
             {Fore.WHITE}░█─── ─▀▀▀ ▀▀▀▀ ▀▀▀ ──▀── ▀▀▀ ──▀── ▀▀▀             
        {Fore.RED}⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
        |     {Fore.CYAN}Github {Fore.YELLOW}: {Fore.WHITE}https://github.com/RetroPackets  {Fore.RED}|
        |    {Fore.CYAN}Discord {Fore.YELLOW}: {Fore.WHITE}https://discord.gg/YkwJWJTGqs    {Fore.RED}|
        | {Fore.CYAN}Created By {Fore.YELLOW}: {Fore.WHITE}RetroPackets {Fore.RED}                    |
        |    {Fore.CYAN}YouTube {Fore.YELLOW}: {Fore.WHITE}RetroPackets                     {Fore.RED}|
        ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯         
    """)

menu_options = {
    f"{Fore.YELLOW}[{Fore.CYAN}1{Fore.YELLOW}]": f'{Fore.WHITE}ᴀᴅᴠᴀɴᴄᴇᴅ ꜱᴇᴀʀᴄʜ',
    f"{Fore.YELLOW}[{Fore.CYAN}2{Fore.YELLOW}]": f'{Fore.WHITE}ᴜꜱᴇʀɴᴀᴍᴇ ꜱᴇᴀʀᴄʜ',
    f"""{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~
{Fore.YELLOW}[{Fore.CYAN}00{Fore.YELLOW}]""": f'{Fore.WHITE}ᴄʟᴏꜱᴇ ꜰᴜɢɪᴛɪᴠᴇ',
    f"{Fore.YELLOW}[{Fore.CYAN}99{Fore.YELLOW}]": f'{Fore.WHITE}ᴄʟᴇᴀʀ ꜱᴄʀᴇᴇɴ',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     os.system("clear")
     print('Loading...')
     time.sleep(5)
     os.system("python3 adv-search.py -d search")
     print(f"""

  {Fore.WHITE}░█▀▀▀ █──█ █▀▀▀ ─▀─ ▀▀█▀▀ ─▀─ ▀█─█▀ █▀▀ 
  {Fore.RED}░█▀▀▀ █──█ █─▀█ ▀█▀ ──█── ▀█▀ ─█▄█─ █▀▀ 
  {Fore.WHITE}░█─── ─▀▀▀ ▀▀▀▀ ▀▀▀ ──▀── ▀▀▀ ──▀── ▀▀▀             
        {Fore.RED}⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
        | {Fore.CYAN}Created By {Fore.YELLOW}: {Fore.WHITE}RetroPackets {Fore.RED}|
        ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯           
    """)


def option2():
     os.system("clear")
     print(f'{Fore.WHITE}Loading {Fore.YELLOW}[{Fore.CYAN}Maigret{Fore.YELLOW}]{Fore.WHITE}...')
     time.sleep(5)
     os.system("cd maigret && python3 launcher.py")
     
def option3():
     os.system("clear")
     time.sleep(4)
     print(f'{Fore.WHITE}Loading{Fore.YELLOW}...')
     os.system("clear")
     print(f"""

  {Fore.WHITE}░█▀▀▀ █──█ █▀▀▀ ─▀─ ▀▀█▀▀ ─▀─ ▀█─█▀ █▀▀ 
  {Fore.RED}░█▀▀▀ █──█ █─▀█ ▀█▀ ──█── ▀█▀ ─█▄█─ █▀▀ 
  {Fore.WHITE}░█─── ─▀▀▀ ▀▀▀▀ ▀▀▀ ──▀── ▀▀▀ ──▀── ▀▀▀             
        {Fore.RED}⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
        | {Fore.CYAN}Created By {Fore.YELLOW}: {Fore.WHITE}RetroPackets {Fore.RED}|
        ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯           
    """)


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input(f"""
   {Fore.WHITE}🅴🅽🆃🅴🆁{Fore.YELLOW} ⑆ {Fore.BLUE}"""))
        except:
            print(f'{Fore.RED}Wrong input. Please enter a number {Fore.YELLOW}...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 99:
            option3()
        elif option() == 00:
            print(f'{Fore.YELLOW}Thanks message before exiting')
            exit()
        else:
            print(f'{Fore.RED}Invalid option. Please enter a number between {Fore.CYAN}1 {Fore.RED}and {Fore.CYAN}3{Fore.YELLOW}.')
