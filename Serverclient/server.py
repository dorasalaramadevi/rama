import socket
import json

def load_config():
    with open('config.json', 'r') as file:
        data = json.load(file)
    return data

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server started on {host}:{port}. Waiting for connection...')
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Client has disconnected.")
                    break
                print(f"Client: {data.decode()}")
                message = input("Server: ")
                if message == "exit":
                    break
                conn.sendall(message.encode())
config = load_config()

if __name__ == "__main__":
    start_server(config["server_ip"], config["port"])
