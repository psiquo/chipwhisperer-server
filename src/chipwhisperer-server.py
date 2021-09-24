import os
import utils.serv as s

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(" ","\ ")

def main():
    serv = s.CWServer()
    commands = {
        "i" : serv.init,
        "t" : serv.start_trace,
        "x" : serv.stop_trace,
    }

    while(True):
        command = input()
        if(command == "q"):
            break
        elif(command in commands.keys()):
            commands[command]()

if __name__ == "__main__":
    main()