from datetime import datetime
import socket

server_address = ('localhost', 6789)
max_size = 4096

if __name__ == "__main__":
    print(f'[INFO] Starting the server at {datetime.now()}')
    print(f'[INFO] Waiting for a client to call.')
    # Make a connection 
    # [1] socket.socket create a socket
        # AF_NET - internet socket IP
        # SOCK_DGRAM - channel for sending and recieving datagrams
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # [2] bind socket and server_address
    server.bind(server_address)
    # Start of waiting for datagrams
    data, client = server.recvfrom(max_size)

    print(f'[INFO] At {datetime.now()} {client} said {data}')
    server.sendto(b'Are you talking to me?',client)
    server.close()