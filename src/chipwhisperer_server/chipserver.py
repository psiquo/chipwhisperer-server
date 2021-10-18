import os
from .utils import serv as s


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
            serv.quit()
            com_channel.close()
            break
        elif(command in commands.keys()):
            commands[command]()

