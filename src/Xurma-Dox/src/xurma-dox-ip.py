import requests, json, os, cloudscraper, re
from bs4 import BeautifulSoup
from colorama import Fore

def logo():
    os.system('clear')
    return f''' {Fore.WHITE}

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
'''
with open('config.json') as f:
    config = json.load(f)

stripe_mid = config.get('ict(__stripe_mid')
tripe_sid = config.get('__stripe_sid')
PHPSESSID = config.get('PHPSESSID')
remember = config.get('remember')


def tt(cmd):
    scraper = cloudscraper.create_scraper()
    url=f'https://thatsthem.com/ip/{cmd}'
    coookies = dict(__stripe_mid=f'{stripe_mid}',
        __stripe_sid=f'{tripe_sid}',
        PHPSESSID=f'{PHPSESSID}',
        remember=f'{remember}')
    path=scraper.get(url, cookies=coookies).text
    soup = BeautifulSoup(path, 'lxml')
    print (f'''
{Fore.WHITE}𝗧𝗔𝗥𝗚𝗘𝗧        : {Fore.CYAN}{cmd}\n
-------------------------------''')
        
    for phone in soup.findAll('a', {'href': lambda x: x and '/phone/' in x}):
        print(f'''{Fore.WHITE}𝗣𝗛𝗢𝗡𝗘 𝗡𝗨𝗠𝗕𝗘𝗥    : {Fore.YELLOW} '''+ phone.text.strip().replace('\n', ' ')+ '\n')
        
    for ipele in soup.findAll('a', {'href': lambda x: x and '/email/' in x}):
        print(f'''{Fore.WHITE}𝗘𝗠𝗔𝗜𝗟 𝗔𝗗𝗗𝗥𝗘𝗦𝗦    : {Fore.YELLOW} '''+ ipele.text.strip().replace('\n ',' ')+ '\n ')
        
    for ipele in soup.findAll('a', {'href': lambda x: x and '/VIN/' in x}):
        print(f'''{Fore.WHITE}𝗩𝗜𝗡 𝗡𝗨𝗠𝗕𝗘𝗥    : {Fore.YELLOW} '''+ ipele.text.strip().replace('\n ',' ')+ '\n ')

    for namle in soup.findAll('a', {'href': lambda x: x and '/name/' in x}):
        print(f'{Fore.WHITE}𝗙𝗨𝗟𝗟 𝗡𝗔𝗠𝗘        : {Fore.YELLOW}'+ namle.text.strip().replace('\n',' ')+ '\n')
        
    for house in soup.findAll('a', {'href': lambda x: x and '/address/' in x}):
        print(f'''{Fore.WHITE}𝗔𝗗𝗗𝗥𝗘𝗦𝗦          :
{Fore.YELLOW}''' + house.text.strip().replace('\n ',' ')+ '\n')

def main():
    print(logo())
    cmd = input(f'{Fore.GREEN}𝗧𝗮𝗿𝗴𝗲𝘁 𝗜𝗣 𝗔𝗱𝗱𝗿𝗲𝘀𝘀  ~>{Fore.WHITE} ')
    tt(cmd)
main()

os.system("python3 qu.py")
