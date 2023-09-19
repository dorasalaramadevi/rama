import socket
import json

class ChatClient:
    def __init__(self, server_ip, server_port,buffer_size):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        self.buffer_size = buffer_size

    def send_message(self, message):
        try:
            self.client_socket.send(message.encode())
        except Exception as e:
            print(f"Error sending message: {str(e)}")

# Load server configurations from JSON file 
with open('config_2server_client.json', 'r') as f:
    servers_config = json.load(f)

server1_client = ChatClient(servers_config['server1_ip'], servers_config['server1_port'],servers_config['buffer_size'])
server2_client = ChatClient(servers_config['server2_ip'], servers_config['server2_port'],servers_config['buffer_size'])

while True:
    try:
        message = input("Send message: ")
        server1_client.send_message(message)
        server2_client.send_message(message)

        if message.lower() == "exit":
            break
