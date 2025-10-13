import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 4096

if __name__ == "__main__":
    print(f'[INFO] Starting the server at {datetime.now()}')
    print(f'[INFO] Waiting for a client to call.')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen()

    client, addr = server.accept()
    data = client.recv(max_size)

    print(f'[INFO] At {datetime.now()} {client} said {data}')
    client.sendall(b'Are you talking to me?')
    client.close()
    server.close()