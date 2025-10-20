import sys
import socket
import threading
import logging

# logging.basicConfig(level=logging.DEBUG)

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