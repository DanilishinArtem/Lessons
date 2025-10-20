# Four parts of the tcp-proxy
- interaction between local and remote systems in console (hexdump)
- Accepting datas from local or remote system by using incoming socket (receive_from)
- Determing direction of the traffic of messaging local and remote systems (proxy_handler)
- Prepare listening socket and pass to it our proxy_handler's (server_loop)

```python
import sys
import socket
import threading
import logging

logging.basicConfig(level=logging.DEBUG)

# Filter for str symbols (they have len in repr == 3)
HEX_FILTER = ''.join(
    [chr(i) if len(repr(chr(i))) == 3 else '.' for i in range(256)]
)

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode()
    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        results.append(f'{i:04x} {hexa:<{hexwidth}} {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results


def request_handler(buffer):
    return buffer


def response_handler(buffer):
    return buffer


def receive_from(connection):
    buffer = b''
    connection.settimeout(5)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        pass
    return buffer


def proxy_handler(client_socket, remote_host: str, remote_port: int, receive_first: bool):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info(f'Trying to connect to {remote_host}:{remote_port}')
    remote_socket.connect((remote_host, int(remote_port)))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

    remote_buffer = response_handler(remote_buffer)
    if len(remote_buffer):
        print(f'[<==] Sending {len(remote_buffer)} bytes to localhost.')
        client_socket.send(remote_buffer)
    
    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print(f'[==>] Received {len(local_buffer)} bytes from localhost.')
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print(f'[==>] Sent to remote.')

        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print(f'[<==] Received {len(remote_buffer)} bytes from remote.')
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print(f'[<==] Sent to localhost')

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print(f'[*] No more data. Closing connections.')
            break


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        logging.info(f'Trying to bind to {local_host}:{local_port}')
        server.bind((local_host, int(local_port)))
    except Exception as e:
        print(f'Problem on bind: {e}')
        print(f'[!!] Failed to listen on {local_host}:{local_port}')
        print(f'[!!] Check for other listening sockets or correct permissions.')
        sys.exit()

    print(f'[*] Listening on {local_host}:{local_port}')
    server.listen(50)
    while True:
        client_socket, addr = server.accept()
        # show information about local connection
        print(f'[==>] Received incoming connection from {addr[0]}:{addr[1]}')
        # creating thread for interaction with remote server
        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()


def main():
    if len(sys.argv[1:]) != 5:
        print(f'Usage: ./proxy.py [localhost] [localport]')
        print(f'[remotehost] [remoteport] [receive_first]')
        print(f'Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True')
        sys.exit()
    
    local_host = sys.argv[1]
    local_port = sys.argv[2]
    remote_host = sys.argv[3]
    remote_port = sys.argv[4]
    receive_first = sys.argv[5]

    if 'True' in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)

# sudo /home/adanilishin/miniconda3/envs/python/bin/python ./Sources/proxy.py  127.0.0.1 21 ftp.sun.ac.za 21 True
# ftp 127.0.0.1 21

# anonymous
# guest
if __name__ == "__main__":
    main()
```

Outputs for server:
```python
[*] Listening on 127.0.0.1:21
[==>] Received incoming connection from 127.0.0.1:45556
0000 32 32 30 20 57 65 6C 63 6F 6D 65 20 74 6F 20 66  220 Welcome to f
0010 74 70 2E 73 75 6E 2E 61 63 2E 7A 61 0D 0A        tp.sun.ac.za..
[<==] Sending 30 bytes to localhost.
[==>] Received 16 bytes from localhost.
0000 55 53 45 52 20 61 6E 6F 6E 79 6D 6F 75 73 0D 0A  USER anonymous..
[==>] Sent to remote.
[<==] Received 34 bytes from remote.
0000 33 33 31 20 50 6C 65 61 73 65 20 73 70 65 63 69  331 Please speci
0010 66 79 20 74 68 65 20 70 61 73 73 77 6F 72 64 2E  fy the password.
0020 0D 0A                                            ..
[<==] Sent to localhost
[==>] Received 12 bytes from localhost.
0000 50 41 53 53 20 67 75 65 73 74 0D 0A              PASS guest..
[==>] Sent to remote.
[<==] Received 23 bytes from remote.
0000 32 33 30 20 4C 6F 67 69 6E 20 73 75 63 63 65 73  230 Login succes
0010 73 66 75 6C 2E 0D 0A                             sful...
[<==] Sent to localhost
[==>] Received 6 bytes from localhost.
0000 53 59 53 54 0D 0A                                SYST..
[==>] Sent to remote.
[<==] Received 19 bytes from remote.
0000 32 31 35 20 55 4E 49 58 20 54 79 70 65 3A 20 4C  215 UNIX Type: L
0010 38 0D 0A                                         8..
```

Outputs for client
```python
Connected to 127.0.0.1.
220 Welcome to ftp.sun.ac.za
Name (127.0.0.1:adanilishin): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```