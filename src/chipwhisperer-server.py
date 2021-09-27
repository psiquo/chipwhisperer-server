import os
import utils.serv as s
import utils.socket_listener as soc

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(" ","\ ")


def listen(com_channel):
    serv = s.CWServer(com_channel)
    commands = {
        "i" : serv.init,
        "t" : serv.start_trace,
        "x" : serv.stop_trace,
    }

    while(True):
        command = com_channel.receive_data()
        if(command == "q"):
            com_channel.close()
            break
        elif(command in commands.keys()):
            commands[command]()

if __name__ == "__main__":
    so = soc.SocketListener()
    listen(so)