from src.chipwhisperer_server.chipserver import listen
import src.chipwhisperer_server.utils.socket_listener as soc

if __name__ == "__main__":
    so = soc.SocketListener()
    listen(so)