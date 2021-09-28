import socket
import os

class SocketListener:
    def __init__(self, file_socket = "chipserver") -> None:
        self.socket = (s := socket.socket(socket.AF_UNIX,socket.SOCK_STREAM))
        self.intialized = False

        socket_file_path = "/tmp/" + file_socket

        if os.path.exists(socket_file_path):
            os.remove(socket_file_path)

        s.bind(socket_file_path)

    def initialize_channel(self):
        self.socket.listen()
        self.conn,self.addr = self.socket.accept()
        self.intialized = True
    
    def close(self):

        if not self.intialized:
            self.initialize_channel()
            
        self.conn.close()
        self.socket.close()
    
    def send_data(self,data : str):

        if not self.intialized:
            self.initialize_channel()

        print(f"###### SOCKET LISTENER #####\n Sending data {data}\n###########\n")
        self.conn.sendall(bytearray(data,"utf-8"))
    
    def receive_data(self, decode = True):

        if not self.intialized:
            self.initialize_channel()

        s =  self.conn.recv(1024)

        if decode:
            s = s.decode("utf-8")

        print(f"###### SOCKET LISTENER #####\nReceived data {s}\n###########\n")
        return s