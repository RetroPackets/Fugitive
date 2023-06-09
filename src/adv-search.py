import argparse
import sys
from helium import *
import time
from colorama import Fore, Back, Style
import os 

prev_url = -1
final = []
driver = -1

os.system("clear")
print(f"""

  {Fore.WHITE}░█▀▀▀ █──█ █▀▀▀ ─▀─ ▀▀█▀▀ ─▀─ ▀█─█▀ █▀▀ 
  {Fore.RED}░█▀▀▀ █──█ █─▀█ ▀█▀ ──█── ▀█▀ ─█▄█─ █▀▀ 
  {Fore.WHITE}░█─── ─▀▀▀ ▀▀▀▀ ▀▀▀ ──▀── ▀▀▀ ──▀── ▀▀▀             
        {Fore.RED}⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
        | {Fore.CYAN}Created By {Fore.YELLOW}: {Fore.WHITE}RetroPackets {Fore.RED}|
        ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
""")
test = input(f"{Fore.WHITE}𝗦𝗘𝗔𝗥𝗖𝗛 {Fore.YELLOW}⑆ {Fore.GREEN}")
def banner():
    os.system("clear")
    print(f"""

  {Fore.WHITE}░█▀▀▀ █──█ █▀▀▀ ─▀─ ▀▀█▀▀ ─▀─ ▀█─█▀ █▀▀ 
  {Fore.RED}░█▀▀▀ █──█ █─▀█ ▀█▀ ──█── ▀█▀ ─█▄█─ █▀▀ 
  {Fore.WHITE}░█─── ─▀▀▀ ▀▀▀▀ ▀▀▀ ──▀── ▀▀▀ ──▀── ▀▀▀             
        {Fore.RED}⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
        | {Fore.CYAN}Created By {Fore.YELLOW}: {Fore.WHITE}RetroPackets {Fore.RED}|
        ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯           
    """)

def parser_error(self):
    banner()
    print(f"Usage: python {sys.argv[0]} [Options] use -h for help")
    sys.exit()


def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d 'THE-DORK-YOU-WANT'")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-f', '--dorkfile', required=False)
    parser.add_argument('-d', '--dork', required=False)
    parser.add_argument('-o', '--output', required=False)
    return parser.parse_args()


def input_(dork):
    helium.write(dork)
    helium.press(ENTER)
    time.sleep(2)

def re_enter():
    global prev_url
    global driver
    driver = helium.start_firefox(headless=False)
    time.sleep(5)
    go_to(prev_url)
    flow()


def urlExtract():
    global final
    urls = helium.find_all(S('.yuRUbf'))
    url = [i.web_element.find_element_by_tag_name('a').get_attribute('href') for i in urls]
    if not url:
        kill_browser()
        re_enter()
    url = clean(url)
    final.extend(url)

def pages():
    global driver
    global prev_url
    while True:
        try:
            prev_url = driver.current_url
            helium.scroll_down(num_pixels=100000)
            helium.click('Next')
            time.sleep(2)
            urlExtract()
        except:
            break


def clean(li):
    li = set(li)
    return list(li)

def flow():
    urlExtract()
    time.sleep(2)
    pages()
    try:
        kill_browser()
    except:
        pass

def exechaha(args,dorks):
    global driver
    if args.dorkfile:
        with open(dorks) as f:
            while True:
                if not (line := f.readline()):
                    break
                driver = helium.start_firefox(headless=False)
                go_to('https://www.google.com/search?q=site:doxbin.com | site:instagram.com | site:facebook.com | site:youtube.com | site:zerobin.net | site:pastebin.com | site:skidbin.net | site:hastebin.com | site:twitter.com | site:linkedin.com | site:pinterest.com | site:tumblr.com | site:snapchat.com | site:reddit.com | site:github.com | site:gitlab.com | site:pornhub.com | site:whatsapp.com  \ site:tiktok.com "' + test +'"')
                input_(line)
                time.sleep(5)
                flow()

    else:
        line = args.dork
        driver = helium.start_firefox(headless=False)
        time.sleep(5)
        go_to(f'https://www.google.com/search?q="{test}"')
        input_(line)
        time.sleep(5)
        flow()
        
def main():
    banner()
    global final
    args = parse_args()
    dorks = args.dorkfile
    exechaha(args,dorks)
    if args.output:
        with open(f'{args.output}.txt', 'w') as file1:
            for i in clean(final):
                file1.write(i.strip()+'\n')
    else:
        for i in clean(final):
            print(f"{Fore.YELLOW}[{Fore.GREEN}ϟ{Fore.YELLOW}] {Fore.BLUE}{i}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[ERR]: Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
