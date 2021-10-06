import os
import Pyro5.server
from .serv import CWServer

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(" ","\ ")


custom_daemon = Pyro5.server.Daemon(unixsocket = "/tmp/chipserver")
Pyro5.server.serve({
    CWServer: "chipwhisperer_server.CWServer"
})
