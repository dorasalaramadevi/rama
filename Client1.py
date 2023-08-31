import json
import socket

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

host = config['host']
port = config['port']
buffer_size = config['buffer_size']

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))
print("Connected to server.")

while True:
    message = input("You: ")
    client_socket.send(message.encode())

    if message.lower() == 'exit':
        break

    data = client_socket.recv(buffer_size).decode()
    print("Server:", data)

client_socket.close()

