import threading
import socket
from queue import Queue

# Configurações do servidor
HOST = 'localhost'
PORT = 5555
MAX_CONNECTIONS = 5

# Semáforo para limitar conexões simultâneas
semaphore = threading.Semaphore(MAX_CONNECTIONS)

# Fila de mensagens
message_queue = Queue()

# Lista de clientes conectados
clients = []

def handle_client(client_socket, addr):
    with semaphore:
        clients.append(client_socket)
        print(f"[CONEXÃO] {addr} conectado. Total de clientes: {len(clients)}")
        try:
            while True:
                msg = client_socket.recv(1024).decode()
                if not msg:
                    break
                message_queue.put(f"{addr}: {msg}")
        except:
            pass
        finally:
            clients.remove(client_socket)
            client_socket.close()
            print(f"[DESCONECTADO] {addr} saiu. Total de clientes: {len(clients)}")

def broadcast_messages():
    while True:
        msg = message_queue.get()
        for client in clients:
            try:
                client.send(msg.encode())
            except:
                pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(MAX_CONNECTIONS)
    print(f"[SERVIDOR INICIADO] Rodando em {HOST}:{PORT}")

    threading.Thread(target=broadcast_messages, daemon=True).start()

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
