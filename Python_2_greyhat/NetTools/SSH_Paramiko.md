# SSH by using Paramiko
In python for creation SSH-client or server we can use raw sockets and crypto libraries. For example we can use Paramiko, which basen on BCrypt, and can get us access to protocol SSH2.
```python
import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('---Output---')
        for line in output:
            print(line.strip())


if __name__ == "__main__":
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '127.0.0.1'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)
```
Output
```python
# Username: artemdanilisin
# Password: 
# Enter server IP: 127.0.0.1
# Enter port or <CR>: 22
# Enter command or <CR>: whoami
# ---Output---
# artemdanilisin
```




<!-- 44 -->