import socket
import json

class ChatServer:
    def __init__(self, ip, port,buffer_size):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(5)
        print("Server 1 listing....")
        self.client_socket, _ = self.server_socket.accept()
        self.buffer_size = buffer_size

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(self.buffer_size).decode()
                if not message:
                    print("Client disconnected.")
                    break
                print(f"receive msg from client: {message}")
            except Exception as e:
                print(f"Error receiving message: {str(e)}")
                break

# Load server configurations from JSON file
with open('Config.json', 'r') as f:
    servers_config = json.load(f)

server1 = ChatServer(servers_config['server1_ip'], servers_config['server1_port'],servers_config['buffer_size'])
server1.receive_messages()

