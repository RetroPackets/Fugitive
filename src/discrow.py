# Author: 
#   github.com/a3r0id 

# File:   
#   discord_user.py

# Usage:  
#   python3 discord_user.py

# Description:
#   This script takes a Discord user ID and returns all public information associated with it. (Requires a valid Discord token to authenticate with the API.)

# Requirements:
#   pip3 install requests

from requests import get

my_token = input("Enter your token: ").strip()
user_id  = input("Enter the user ID: ").strip()

r = get("https://discord.com/api/v8/users/" + user_id, headers={"authorization": my_token})

if r.status_code != 200:
    print("[-] *Invalid user ID or token*")
    exit()

j = r.json()
j["username_full"] = "%s#%s" % (j['username'], j['discriminator'],)
if (j['avatar'] is not None):
    j["avatar_full"] = "https://cdn.discordapp.com/avatars/%s/%s.png" % (j['id'], j['avatar'],)
else:
    j['avatar_full'] = "<Default Avatar>"
    
for key, value in j.items():
    print(f"[+] {key}: {value}")
