import socket
import os

class SocketListener:
    def __init__(self, file_socket = "chipserver") -> None:
        self.socket = (s := socket.socket(socket.AF_UNIX,socket.SOCK_STREAM))

        socket_file_path = "/tmp/" + file_socket

        if os.path.exists(socket_file_path):
            os.remove(socket_file_path)

        s.bind(socket_file_path)
        s.listen()
        self.conn,self.addr = s.accept()
    
    def close(self):
        self.conn.close()
        self.socket.close()
    
    def send_data(self,data : str):
        print(f"Sending data {data}")
        self.conn.sendall(bytearray(data,"utf-8"))
    
    def receive_data(self):
        s =  self.conn.recv(1024).decode("utf-8")
        print(f"Received data {s}")
        return s