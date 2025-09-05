from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

# Configurações do cliente
HOST = 'localhost'
PORT = 5555

def receive_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            print(msg)
        except:
            break

def start_client():
    client_socket = socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
    except:
        print("Não foi possível conectar ao servidor.")
        return

    Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == "sair":
            break
        client_socket.send(msg.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
