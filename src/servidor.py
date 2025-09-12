from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from fila import Fila
from semaforo import Semaforo

# Configurações do servidor
HOST = 'localhost'
PORT = 5555
MAX_CONNECTIONS = 5

# Semáforo para limitar conexões simultâneas
semaphore = Semaforo(MAX_CONNECTIONS)

# Fila de mensagens
message_queue = Fila()

# Lista de clientes conectados
clients = []

def handle_client(client_socket, addr):
    """
    Gerencia a conexão de um cliente.

    - Adiciona o cliente à lista de conectados.
    - Recebe mensagens em loop e coloca na fila de mensagens.
    - Remove o cliente da lista ao desconectar.
    - Libera uma vaga no semáforo após o encerramento.
    """
    try:
        clients.append(client_socket)
        print(f"[CONEXÃO] {addr} conectado. Total de clientes: {len(clients)}")
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
        semaphore.liberar()
        print(f"[DESCONECTADO] {addr} saiu. Total de clientes: {len(clients)}")

def broadcast_messages():
    """
    Responsável por distribuir mensagens a todos os clientes conectados.

    - Fica em loop infinito.
    - Pega a próxima mensagem da fila.
    - Envia para todos os clientes na lista de conectados.
    """
    while True:
        msg = message_queue.get()
        for client in clients:
            try:
                client.send(msg.encode())
            except:
                pass

def start_server():
    """
    Inicializa o servidor de chat.

    1. Cria e configura o socket TCP.
    2. Inicia a thread de broadcast.
    3. Aceita conexões em loop:
        - Se houver vaga no semáforo, cria uma thread para o cliente.
        - Caso contrário, recusa a conexão enviando mensagem de erro.
    4. Fecha o servidor ao encerrar.
    """
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(MAX_CONNECTIONS)
    print(f"[SERVIDOR INICIADO] Rodando em {HOST}:{PORT}")

    Thread(target=broadcast_messages, daemon=True).start()

    try:
        while True:
            client_socket, addr = server.accept()
            if semaphore.tentar_adquirir():
                Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()
            else:
                client_socket.send("[ERRO] Servidor cheio, tente novamente mais tarde.\n".encode())
                client_socket.close()
                print(f"[RECUSADO] {addr} - Limite de conexões atingido")     
    except:
        pass
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
