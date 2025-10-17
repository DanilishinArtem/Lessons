import socket
from datetime import datetime

server_address = ('localhost', 6789)
max_size = 4096

if __name__ == "__main__":
    print(f'[INFO] Starting the client at {datetime.now()}')
    # Make a connection 
    # [1] socket.socket create a socket
        # AF_NET - internet socket IP
        # SOCK_DGRAM - channel for sending and recieving datagrams
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # [2] Send a message to the server
    client.sendto(b'HEY!', server_address)
    data, server = client.recvfrom(max_size)
    print(f'[INFO] At {datetime.now()} {server} said {data}')
    client.close()