import os
import time
import random
import sys
from pystyle import Colors, Box, Write, Center, Colorate
import pystyle
import webbrowser

color_code = {
    "reset": "\033[0m",
    "underline": "\033[04m",
    "green": "\033[32m",
    "yellow": "\033[93m",
    "red": "\033[31m",
    "cyan": "\033[36m",
    "bold": "\033[01m",
    "url_l": "\033[36m",
    "li_g": "\033[92m",
    "f_cl": "\033[0m",
    "purple": "\033[95m",
    "blue": "\033[94m",
    "dark": "\033[38;5;240m",
    "light_gray": "\033[38;5;250m",
    "white": "\033[38;5;255m"
}
os.system("clear")
os.system("python3 src/serv.py")


Green = "\033[1;33m"
Blue = "\033[1;34m"
Grey = "\033[1;30m"
Reset = "\033[0m"
Red = "\033[1;31m"
Purple = "\033[0;35m"

g = "\033[1;32m"
r = "\033[1;31m"
w = "\033[0m"
b = "\033[1;34m"
o = "\033[1;33m"
bl = "\033[1;36;40m"

menu = """
┌───────────────────────────────────────────────┐
│            [1] DDoS по IP адресу              │
├───────────────────────────────────────────────┤
│            [2] Получить IP адрес по URL       │
├───────────────────────────────────────────────┤
│            [3] Логи DDoS атак                 │
└───────────────────────────────────────────────┘
"""

centered_menu = "\n".join([line.center(110) for line in menu.split("\n")])
colored_menu = Colorate.Vertical(Colors.white_to_black, centered_menu)
print(colored_menu)

op = int(input(f'{color_code["dark"]}[✿] Выберите действие => {color_code["reset"]}'))

if(op == 1):
    os.system("python3 src/ddos.py")
elif(op == 2):
    os.system("python3 src/Url.py")
elif(op == 3):
    os.system("python3 src/log-ddos.py")
else:
    print("\033[1;31;40mНеверный ввод. Перезагружаю инструменты!") 
    time.sleep(1.6)
    os.system("cd")
    os.system("cd Ultra-DDos")
    os.system("python3 main.py")
