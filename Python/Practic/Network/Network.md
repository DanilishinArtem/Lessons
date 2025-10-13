# Network
### Example of server-client connection through UDP
#### Part of server
```python
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

    print(f'[INFO] At {datetime.now()} client said {data}')
    server.sendto(b'Are you talking to me?',client)
    server.close()
# Output:
# [INFO] Starting the server at 2025-10-13 08:03:11.317736
# [INFO] Waiting for a client to call.
# [INFO] At 2025-10-13 08:03:13.488988 ('127.0.0.1', 45100) said b'HEY!'
```
#### Part of client
```python
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
# Output:
# [INFO] Starting the client at 2025-10-13 07:57:54.235570
# [INFO] At 2025-10-13 07:57:54.236300 ('127.0.0.1', 6789) said b'Are you talking to me?'
```
### Example of server-client connection through TCP
#### Part of server
```python
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
# output:
# [INFO] Starting the server at 2025-10-13 08:14:31.268608
# [INFO] Waiting for a client to call.
# [INFO] At 2025-10-13 08:14:41.164914 <socket.socket fd=4, family=2, type=1, proto=0, laddr=('127.0.0.1', 6789), raddr=('127.0.0.1', 52680)> said b'Hey!'
```
#### Part of client
```python
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
# Output:
# [INFO] Starting the client at 2025-10-13 08:14:41.164119
# [INFO] At 2025-10-13 08:14:41.165149 someone replied b'Are you talking to me?'
```
### General schema of using UDP and TCP protocols for passing messages
#### UDP protocol
```python
# Part of server
├── Server = Socket
    Server.bind(('ip_address',port))
    ├── Server.recvfrom
    └── Server.sendto

# Part of client
├── Client = Socket
    ├── Client.recvfrom
    └── Client.sendto
```
#### TCP protocol
```python
# Part of server
├── Server = Socket
    Server.bind(('ip_address',port))
    Server.listen()
    client, addr = Server.accept()
    ├── client.sendall
    └── client.recv

# Part of client
├── Client = Socket
    Client.connect(('ip_address',port))
    ├── Client.sendall
    └── Client.recv
```