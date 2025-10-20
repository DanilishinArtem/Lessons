import paramiko
import logging

logging.basicConfig(level=logging.DEBUG)

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    logging.info('Client created')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info('Seted policy')
    client.connect(ip, port=port, username=user, password=passwd)
    logging.info('Client connected')

    _, stdout, stderr = client.exec_command(cmd)
    logging.info('Command executed')
    output = stdout.readlines() + stderr.readlines()
    logging.info(f'Output: {output}')
    if output:
        print('---Output---')
        for line in output:
            print(line.strip())


if __name__ == "__main__":
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)