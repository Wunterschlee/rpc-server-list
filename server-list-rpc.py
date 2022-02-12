from xmlrpc.server import SimpleXMLRPCServer

local_ip = 'localhost'

def get_servers ():
    print ("entered sus")
    return "sus"


rpc_server = SimpleXMLRPCServer((local_ip, 6789),allow_none=True)
rpc_server.register_function(get_servers, "sus")
rpc_server.serve_forever()
    
