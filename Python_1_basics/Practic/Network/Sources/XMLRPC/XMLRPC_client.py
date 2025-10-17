import xmlrpc.client

if __name__ == "__main__":
    proxy = xmlrpc.client.ServerProxy('http://localhost:6789/')
    num = 7
    result = proxy.double(num)
    print(f'{num} * 2 = {result}')