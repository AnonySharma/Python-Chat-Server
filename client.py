import time
import socket
import sys

HEADER_LENGTH = 1024

print('\033[92m'+'\033[1m'+'CHAT CLIENT '+'\033[0m'+'\033[92m'+'by ANKIT'+'\033[0m')
time.sleep(1)

room_socket = socket.socket()
host_name = socket.gethostname()
IP = socket.gethostbyname(host_name)
PORT = 1803

name = input("Enter Client's name: ")

print('Trying to connect to the server: {}, ({})'.format(IP, PORT))
time.sleep(1)

try:
    room_socket.connect((IP, PORT))
    print("Successfully Connected!\n")
except:
    print('\033[91m'+'\033[1m'+"Server is not active!")
    exit()

room_socket.send(name.encode())
server_name = room_socket.recv(HEADER_LENGTH).decode()

print('{} has joined...'.format(server_name))
print('Enter [bye] to leave!')
while True:
    try:
        message = room_socket.recv(HEADER_LENGTH).decode()
    except:
        print('\033[92m'+'\033[1m'+"\nThanks for using ChatRoom!")
        exit()
    
    print('\033[1m'+server_name+" >>"+'\033[0m', message)
    
    try:
        message = input('\033[1m'+'Me >> '+'\033[0m')
    except:
        print('\033[92m'+'\033[1m'+"\nThanks for using ChatRoom!")
        exit()    

    if message == "[bye]":
        room_socket.send('Bye! Have a nice day'.encode())
        print("\n")
        exit()

    try:
        room_socket.send(message.encode())
    except:
        print('\033[91m'+'\033[1m'+"\nServer is not active!")
        print('\033[92m'+'\033[1m'+"Exiting..Thanks for using ChatRoom!")
        exit() 