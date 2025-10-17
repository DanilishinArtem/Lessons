from jsonrpcclient import request

if __name__ == "__main__":
    num = 7
    response = request('http://localhost:5000', double, num)
    print('num * 2 = {response}')