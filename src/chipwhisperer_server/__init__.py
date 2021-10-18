import os,sys,subprocess
import Pyro5.server
from .serv import CWServer

prefix = "### Chipwhisperer server ###\n\n"
suffix = "#" * len(prefix) + "\n"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(" ","\ ")

def start_pyro_server(serv_name = "CWServer"):

    print(prefix + "Starting Pyro name server\n\n")
    subprocess.Popen("pyro5-ns",stdout=sys.stdout, stderr = subprocess.DEVNULL)

    print("\n" + suffix)
   
    print(prefix + "Starting Pyro daemon\n\n" + suffix)

    Pyro5.server.serve({
        CWServer: serv_name
    })
