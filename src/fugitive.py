
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
        |    {Fore.CYAN}Website {Fore.YELLOW}: {Fore.WHITE}https://idicesecurity.com {Fore.RED}       |
        ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯         
    """)

menu_options = {
    f"{Fore.YELLOW}[{Fore.CYAN}1{Fore.YELLOW}]": f'{Fore.WHITE}ᴀᴅᴠᴀɴᴄᴇᴅ ꜱᴇᴀʀᴄʜ',
    f"{Fore.YELLOW}[{Fore.CYAN}2{Fore.YELLOW}]": f'{Fore.WHITE}ᴜꜱᴇʀɴᴀᴍᴇ ꜱᴇᴀʀᴄʜ',
    f"{Fore.YELLOW}[{Fore.CYAN}3{Fore.YELLOW}]": f'{Fore.WHITE}ᴇᴍᴀɪʟ ʀᴇɢɪꜱᴛʀʏ',
    f"{Fore.YELLOW}[{Fore.CYAN}4{Fore.YELLOW}]": f'{Fore.WHITE}ᴇᴍᴀɪʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ',
    f"{Fore.YELLOW}[{Fore.CYAN}5{Fore.YELLOW}]": f'{Fore.WHITE}ᴘᴀꜱᴛᴇʙɪɴ ꜱᴇᴀʀᴄʜ',
    f"{Fore.YELLOW}[{Fore.CYAN}6{Fore.YELLOW}]": f'{Fore.WHITE}ɢᴏᴏɢʟᴇ ᴅᴏʀᴋ ꜱᴇᴀʀᴄʜ',
    f"{Fore.YELLOW}[{Fore.CYAN}7{Fore.YELLOW}]": f'{Fore.WHITE}ᴘᴇᴏᴘʟᴇ ꜱᴇᴀʀᴄʜ',
    f"{Fore.YELLOW}[{Fore.CYAN}8{Fore.YELLOW}]": f'{Fore.WHITE}ɪᴘ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ',
    f"{Fore.YELLOW}[{Fore.CYAN}9{Fore.YELLOW}]": f'{Fore.WHITE}ᴅɪꜱᴄᴏʀᴅ ᴏꜱɪɴᴛ',
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

def option4():
     os.system("clear")
     print(f'{Fore.WHITE}Loading {Fore.YELLOW}[{Fore.CYAN}Holehe{Fore.YELLOW}]{Fore.WHITE}...')
     time.sleep(5)
     os.system("cd holehe && sudo python3 setup.py install && clear")
     entry = input(f"{Fore.WHITE}Enter Email{Fore.YELLOW}:{Fore.CYAN} ")
     os.system("""
     holehe """ + entry)

def option5():
     os.system("clear")
     print(f'{Fore.WHITE}Loading {Fore.YELLOW}[{Fore.CYAN}Infoga{Fore.YELLOW}]{Fore.WHITE}...')
     time.sleep(5)
     os.system("cd Infoga && sudo python3 setup.py install && clear")
     entry = input(f"{Fore.WHITE}Enter Email{Fore.YELLOW}:{Fore.CYAN} ")
     os.system("""
     python3 Infoga/infoga.py --info """ + entry + " --breach -v 3")

def option6():
     os.system("clear")
     print(f'{Fore.WHITE}Loading {Fore.YELLOW}[{Fore.CYAN}HarvestBin{Fore.YELLOW}]{Fore.WHITE}...')
     time.sleep(5)
     os.system("cd HarvestBin && python3 harvestbin.py")

def option7():
     os.system("clear")
     print(f'{Fore.WHITE}Loading {Fore.YELLOW}[{Fore.CYAN}Dork-Harvest{Fore.YELLOW}]{Fore.WHITE}...')
     time.sleep(5)
     os.system("cd Dork-Harvest && python3 dork-harvest.py")

def option8():
     os.system("clear")
     print(f'{Fore.WHITE}Loading {Fore.YELLOW}[{Fore.CYAN}Xurma-Dox{Fore.YELLOW}]{Fore.WHITE}...')
     time.sleep(5)
     os.system("cd Xurma-Dox && pip install -r requirements.txt && python3 xurma-dox.py")

def option9():
    os.system("clear")
    print(f'{Fore.WHITE}Loading {Fore.YELLOW}[{Fore.CYAN}GEO-Recon{Fore.YELLOW}]{Fore.WHITE}...')
    time.sleep(5)
    os.system("pip3 install colorama requests")
    os.system("clear")
    entry = input(f"{Fore.WHITE}Enter IP Address{Fore.YELLOW}:{Fore.CYAN} ")
    os.system(
        f"cd geo-recon && chmod +x geo-recon.py && pip install -r requirements.txt && python3 geo-recon.py {entry}"
    )


def option10():
     os.system("clear")
     print(f'{Fore.WHITE}Loading {Fore.YELLOW}[{Fore.CYAN}Discrow{Fore.YELLOW}]{Fore.WHITE}...')
     time.sleep(5)
     os.system("clear && python3 discrow.py")
  
  
  
  


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
        elif option == 3:
            option4()
        elif option == 4:
            option5()
        elif option == 5:
            option6()
        elif option == 6:
            option7()
        elif option == 7:
            option8()
        elif option == 8:
            option9()
        elif option == 9:
            option10()
        elif option == 99:
            option3()
        elif option == 00:
            print(f'{Fore.YELLOW}Thanks for using {Fore.WHITE}[{Fore.CYAN}Fugitive{Fore.WHITE}]{Fore.RED}!')
            exit()
        else:
            print(f'{Fore.RED}Invalid option. Please enter a number between {Fore.CYAN}1 {Fore.RED}and {Fore.CYAN}3{Fore.YELLOW}.')
