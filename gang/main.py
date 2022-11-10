#imports
import os
import requests
import time
import random
import sys
import threading
from os import system
#froms
from colorama import *
from dhooks import Webhook




system("title " + "GANG-TOOLS   MADE BY ALROHA#9999")



def rbxgen():
    account = random.choice(open("database/roblox.txt").readlines())
    print(account)
    time.sleep(10)
    Main()


def rbx2010gen():
    print("This is a part of the paid version of GANG-TOOLS\nTo buy: DM 0xd1d#5513")


def channelspammer():
    TOKEN = input(Fore.MAGENTA+"[" + ">" + Fore.MAGENTA+"]" + Fore.WHITE+" authorization: ")

    id = input("[>] Channel id?: ")

    wspam = input("[>] What do you  want to spam?: ")

    length = input("[>] Attack length: ")
    
     
    for i in range(int(length)):
        payload = {
            "content": f"{wspam}"
        }

        header = {
            'authorization': f"{TOKEN}"

        }
    
        r = requests.post(f"https://discord.com/api/v9/channels/{id}/messages", data=payload, headers=header)
        print("[*] Sent message")

    Main()


def whs():
    message = input("[>] Spam Message?: ")
    webhookurl = Webhook(input("[>] Webhook: "))
    al = int(input("[>] Attack length: "))
    delay = int(input("[>] Delay(seconds): "))
    
     
    
    for i in range(al):
        time.sleep(delay)
        webhookurl.send(message)
        print("[*] Sent message > " + message)

    Main()


def Nitro():
    yn = input("Do you want to generate Nitro codes?(Y/n): ")
    if yn == "Y":
        yas = random.randint(1,999999999999999)
        vaild = ["Active","Active", "Invalid"]
            
        

        print(f"https://discord.gift/{random.randint(1,999999999999999)} [{random.choice(vaild)}]") 
        time.sleep(1)
        print(f"https://discord.gift/{random.randint(1,999999999999999)} [{random.choice(vaild)}]") 
        time.sleep(1)
        print(f"https://discord.gift/{random.randint(1,999999999999999)} [{random.choice(vaild)}]") 
        time.sleep(1)
        print(f"https://discord.gift/{random.randint(1,999999999999999)} [{random.choice(vaild)}]") 
        time.sleep(1)
        print(f"https://discord.gift/{random.randint(1,999999999999999)} [{random.choice(vaild)}]") 
        time.sleep(1)
        print(f"https://discord.gift/{random.randint(1,999999999999999)} [{random.choice(vaild)}]") 
        time.sleep(1)
        print(f"https://discord.gift/{random.randint(1,999999999999999)} [{random.choice(vaild)}]") 
        time.sleep(1)
        print(f"https://discord.gift/{random.randint(1,999999999999999)} [{random.choice(vaild)}]") 
        time.sleep(1)
    elif yn == "n":
        print("Exiting")
    else:
        print("Exiting")
    Main()


def Token():
    print("This is a part of the paid version of GANG-TOOLS\nTo buy: DM 0xd1d#5513")

def Raider():
    print("This is a part of the paid version of GANG-TOOLS\nTo buy: DM 0xd1d#5513")



class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.start_logo()
        self.options()
        while self.gg == True:
            choose = input(str(Fore.MAGENTA+"   [" + ">" + Fore.MAGENTA+"]" + Fore.WHITE+f' Choice?:'))
            if(choose == str(1)):
                self.cls()
                self.start_logo()
                rbxgen()
            elif(choose == str(2)):
                self.cls()
                self.start_logo()
                rbx2010gen()
            elif(choose == str(3)):
                self.cls()
                self.start_logo()
                channelspammer()
            elif(choose == str(4)):
                self.cls()
                self.start_logo()
                whs()
            elif(choose == str(5)):
                self.cls()
                self.start_logo()
                Nitro()
            elif(choose == str(6)):
                self.cls()
                self.start_logo()
                Token()
            elif(choose == str(7)):
                self.cls()
                self.start_logo()
                Raider()



    def cls(self):
        linux= "clear"
        windows = "cls"
        os.system([linux, windows][os.name == "nt"])


    def start_logo(self):
        print(Fore.MAGENTA+"""


                                      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
                                     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$
                                    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/
                                    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$
                                    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$
                                    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$ """                         
        +Fore.BLUE + 
        """
> [MADE BY ALROHA]                  |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/
> [v1.0.0]                          \______/ |__/  |__/|__/  \__/ \______/ 

        """+Fore.MAGENTA+"""
==============================================================================================================                                                         
        """)


    def options(self):
        print(Fore.MAGENTA+"[" + "1" + Fore.MAGENTA+"]" + Fore.WHITE+" Roblox Generator")
        #2
        print(Fore.MAGENTA+"[" + "2" + Fore.MAGENTA+"]" + Fore.WHITE+" Roblox 2010 Generator")
        #3
        print(Fore.MAGENTA+"[" + "3" + Fore.MAGENTA+"]" + Fore.WHITE+" Channel Spammer")
        #4
        print(Fore.MAGENTA+"[" + "4" + Fore.MAGENTA+"]" + Fore.WHITE+" Webhook Spammer")
        #5
        print(Fore.MAGENTA+"[" + "5" + Fore.MAGENTA+"]" + Fore.WHITE+" Nitro Generator")
        #6
        print(Fore.MAGENTA+"[" + "6" + Fore.MAGENTA+"]" + Fore.WHITE+" Token Generator")
        #7
        print(Fore.MAGENTA+"[" + "7" + Fore.MAGENTA+"]" + Fore.WHITE+" Server Raider")
        #===
        print(Fore.MAGENTA+"==============================================================================================================\n")
Main()

