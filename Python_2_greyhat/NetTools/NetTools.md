# NetTools
### TCP Client
```python
import socket

target_host = 'www.google.com'
target_port = 80

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    client.send(b'GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n')
    response = client.recv(4096)
    print(response.decode())
    client.close()
```
### UDP Client
```python
import socket

target_host = '127.0.0.1'
target_port = 9998

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b'AAABBBCCC', (target_host, target_port))
    data, addr = client.recvfrom(4096)
    print(data.decode())
    client.close()
```
### TCP Server
```python
import socket
import threading

ip = "0.0.0.0"
port = 9998

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b"ACK")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(5)
    print(f'[*] Listening on {ip}:{port}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()

# Output for server:
    [*] Listening on 0.0.0.0:9998
    [*] Accepted connection from 127.0.0.1:49048
    [*] Received: GET / HTTP/1.1
    HOST: google.com
# Output for client:
    ACK
```