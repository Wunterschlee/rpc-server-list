from xmlrpc.server import SimpleXMLRPCServer
import threading
import time

class server:
    def __init__(self, adr, port, name, p_a):
        self.adress = adr
        self.port = port
        self.name = name
        self.players_amount = p_a
        self.self_removal_timer = 10

server_list = []

def check_present (s):
    trig = True
    for cur_s in server_list:
        if (s.port == cur_s.port)&(s.adress == cur_s.adress):
            trig = False
    return trig


def register (s):
    new_server = server (s.get('adress'), s.get('port'),s.get('name'),s.get('cur_players'))
    if check_present(new_server):
        server_list.append (new_server)
        print ("registered ", new_server.name)
    else: print("found copy of ", new_server.name)

def get_servers ():
    return server_list


def make_servers_older():
    while True:
        time.sleep(5)
        print ('entered loop')
        for serv in server_list:
            serv.self_removal_timer -= 1
            if serv.self_removal_timer < 1:
                print (f"Removing {serv.name} due to inactivity.")
                server_list.remove(serv)
              
def run_server():
    print ('running server')
    rpc_server.serve_forever()

#get my adress TO SMART GONNA ADD HEROKU MANUALY TO ADRESS
#hostname = socket.gethostname()
#local_ip = socket.gethostbyname(hostname)
local_ip = "https://server-list-rpc.herokuapp.com"

rpc_server = SimpleXMLRPCServer((local_ip, 6789),allow_none=True)
rpc_server.register_function(register, "register")
rpc_server.register_function(get_servers, "get_servers")

threading.Thread(target=make_servers_older).start()
threading.Thread(target=run_server).start()


    
