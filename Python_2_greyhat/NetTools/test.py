import socket

target_host = '172.31.239.69'
target_port = 9995

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    client.send(b'GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n')
    response = client.recv(4096)
    print(response.decode())
    client.close()


string = '''
if __name__ == "__main__":
    print('[INFO] Hello world')
'''
