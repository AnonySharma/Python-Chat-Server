import time
import socket
import sys

HEADER_LENGTH = 1024

print('\033[92m'+'\033[1m'+'CHAT SERVER '+'\033[0m'+'\033[92m'+'by ANKIT'+'\033[0m')
time.sleep(1)
print('Setting up server:')

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name = socket.gethostname()
IP = socket.gethostbyname(host_name)
PORT = 1803

server_socket.bind((host_name, PORT))

name = input('Enter name: ')
server_socket.listen(1)
print('Waiting for incoming connections...')

try:
    client_socket, client_address = server_socket.accept()
except:
    print('\033[92m'+'\033[1m'+"\nThanks for using ChatRoom!")
    exit()

print("Received connection request from ", client_address[0], '({})'.format(client_address[1]))
print('Connection Established!\n')

client_name = client_socket.recv(HEADER_LENGTH).decode()
print(client_name, 'has connected.')
print('Enter [bye] to leave!')

client_socket.send(name.encode())
while True:
    try:
        message = input('\033[1m'+'Me >> '+'\033[0m')
    except:
        print('\033[92m'+'\033[1m'+"\nThanks for using ChatRoom!")
        exit()    
    
    if message == '[bye]':
        client_socket.send('Bye! Have a nice day'.encode())
        print("\n")
        break

    try:
        client_socket.send(message.encode())
        message = client_socket.recv(HEADER_LENGTH).decode()
    except:
        print('\033[92m'+'\033[1m'+"\nThanks for using ChatRoom!")
        exit()

    print('\033[1m'+client_name+' >>'+'\033[0m', message)