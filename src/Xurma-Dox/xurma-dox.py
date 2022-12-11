
import requests, os, colorama
from sys import argv
import urllib3
from os import system as terminal
import requests
from colorama import Fore,Style




os.system('clear')
print(f''' {Fore.WHITE}

      .o oOOOOOOOo                                            OOOo
      Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
      OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
      OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
      `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
      .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
      OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
     oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
    oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
   OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
   "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
      Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
      :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
      .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                   '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                        `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                    .     OP"          : o     .
                                :

        {Fore.CYAN}█▄─▀─▄█▄─██─▄█▄─▄▄▀█▄─▀█▀─▄██▀▄─████▄─▄▄▀█─▄▄─█▄─▀─▄█
        {Fore.WHITE}██▀─▀███─██─███─▄─▄██─█▄█─███─▀─█████─██─█─██─██▀─▀██
        {Fore.CYAN}▀▄▄█▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▄▄█▄▄▀
---------------------------------------------------------------------
| CODED BY : RetroPackets | GITHUB : https://github.com/RetroPackets|
---------------------------------------------------------------------
                  {Fore.RED}Type [close] To Close Program !{Fore.CYAN}
''')

menu_options = {
    1: 'Scrape Email Address',
    2: 'Scrape Phone Number',
    3: 'Scrape IP Address',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
        

def option3():
     os.system("clear")
     print("Loading...")
     os.system("cd src && python3 xurma-dox-ip.py")
     

def option1():
     os.system("clear")
     print("Loading...")
     os.system("cd src && python3 xurma-dox-email.py")
     

def option2():
     os.system("clear")
     print("Loading...")
     os.system("cd src && python3 xurma-dox-phone.py")

def close():
    print(f"{Fore.CYAN} [Xurma Dox] {Fore.WHITE}Program Is Shutting Down...")
    exit()
    

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input(f'''{Fore.GREEN}
Enter Your Choice{Fore.CYAN}:{Fore.WHITE} '''))
        except:
            print("")
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif close == close:
            close()


        
