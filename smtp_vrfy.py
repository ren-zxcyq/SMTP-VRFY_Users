#!/usr/bin/python3

import socket
import sys


def connect(target_IP='127.0.0.1', target_Port=25):
    '''Connect to the SMTP server and return socket.
    '''
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((target_IP, target_Port))

    # Receive the banner
    banner = s.recv(1024)

    print(banner)
    return s

def vrfyUser(s: socket, user: str):
    '''Send 'VRFY <socket>' to socket s.
        Print the results.
    '''
    # VRFY user
    msg = 'VRFY ' + sys.argv[3] + '\r\n' 
    msg = bytes(msg,'utf-8')
    print(f'Sending: {msg}')
    s.send(msg)
    result = s.recv(1024)
    print(result)


def closeConnection():
    '''Close the connection socket
    '''
    # Close the socket
    s.close()


    
def main():
    '''Steps:
        1) Read argv
        2) Connect to SMTP server
        3) For user in file: vrfy()
        4) Close the connection
    '''
    # print(f'{sys.argv[0]} {sys.argv[1]} {sys.argv[2]} {sys.argv[3]}')
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <server IP> <server port> <usernames file>')
        sys.exit(0)
    target_IP = sys.argv[1]
    target_Port = sys.argv[2]
    filepath = sys.argv[3]
    s = connect(target_IP, int(target_Port))
    with open(sys.argv[3],'r') as f:
        for l in f:
            print(f'{l} --')
            vrfyUser(s,l)
    # sys.exit(0)



if __name__ == '__main__':
    main()
