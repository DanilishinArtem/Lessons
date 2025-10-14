from xmlrpc.server import SimpleXMLRPCServer

def double(num):
    return num * 2

if __name__ == "__main__":
    server = SimpleXMLRPCServer(('localhost', 6789))
    server.register_function(double, 'double')
    server.serve_forever()