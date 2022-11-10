from colorama import *
import os
from os import system
import keyboard


system("title " + "PRESS ENTER")
os.system('cls')

print(Fore.MAGENTA+"""


                                      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
                                     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$
                                    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/
                                    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$
                                    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$
                                    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$ """                         
        +Fore.BLUE + 
        """
                                    |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/
                                    \______/ |__/  |__/|__/  \__/ \______/ 

        """+Fore.MAGENTA+"""                                            ALROHA
==============================================================================================================                                                         
        """)


while True:
    if keyboard.is_pressed("ENTER"):
        os.system('cls')
        os.system('python main.py')
        



