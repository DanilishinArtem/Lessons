import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 4096

if __name__ == "__main__":
    print(f'[INFO] Starting the client at {datetime.now()}')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)
    client.sendall(b'Hey!')
    data = client.recv(max_size)
    print(f'[INFO] At {datetime.now()} someone replied {data}')
    client.close()