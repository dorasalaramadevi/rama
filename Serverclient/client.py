import socket
import json

def load_config():
    with open('config.json', 'r') as file:
        data = json.load(file)
    return data

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("Client: ")
            if message == "exit":
                break
            s.sendall(message.encode())
            data = s.recv(1024)
            if not data:
                print("Server has disconnected.")
                break
            print(f"Server: {data.decode()}")
config = load_config()

if __name__ == "__main__":
    start_client(config["server_ip"], config["port"])

 
