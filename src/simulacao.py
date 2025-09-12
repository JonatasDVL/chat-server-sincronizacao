from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time
import random

HOST = 'localhost'
PORT = 5555

def simulate_client(name, delay):
    """
    Simula o comportamento de um cliente de chat.

    Parâmetros:
        name (str): Nome identificador do cliente.
        delay (float): Tempo em segundos para aguardar antes de conectar ao servidor.

    Comportamento:
        1. Aguarda o tempo definido em `delay`.
        2. Conecta ao servidor TCP.
        3. Envia 10 mensagens numeradas.
        4. Tenta receber respostas/broadcasts do servidor após cada envio.
        5. Desconecta automaticamente após o envio da 10ª mensagem.
    """
    
    time.sleep(delay)  # aguarda antes de conectar
    try:
        # Cria um socket para conectar ao servidor
        client_socket = socket(AF_INET, SOCK_STREAM)
        
        # Tenta conectar ao servidor
        client_socket.connect((HOST, PORT))
        
        # Exibe mensagem de conex o bem sucedida
        print(f"[{name}] conectado ao servidor (delay {delay:.1f}s)")

        # Envia 10 mensagens
        for i in range(1, 11):
            # Cria uma mensagem
            msg = f"{name}: mensagem {i}"
            
            try:
                # Envia mensagem ao servidor
                client_socket.send(msg.encode())
                
                # Exibe mensagem de envio bem sucedida
                print(f"[{name}] enviou -> {msg}")
                
                # Tenta receber broadcast
                try:
                    response = client_socket.recv(1024).decode()
                    
                    # Se houver resposta, exibe mensagem
                    if response:
                        print(f"[{name}] recebeu: {response.strip()}")
                except:
                    # Se houver erro ao receber, ignora
                    pass
                
            except Exception as e:
                # Se houver erro ao enviar, exibe mensagem de erro
                print(f"[{name}] erro ao enviar: {e}")
                break

            # Aguarda um tempo aleat rio entre 0.5 e 2 segundos antes de enviar a pr xima mensagem
            time.sleep(random.uniform(0.5, 2))  
        
        # Fecha a conex o com o servidor
        client_socket.close()
        
        # Exibe mensagem de desconexo
        print(f"[{name}] desconectado apos enviar 10 mensagens")

    except Exception as e:
        # Se houver erro geral, exibe mensagem de erro
        print(f"[{name}] erro: {e}")

def start_test():
    """
    Inicia a simulação com múltiplos clientes.

    Comportamento:
        - Cria um número definido de clientes (clients_count).
        - Cada cliente é iniciado em uma thread separada.
        - O tempo de entrada de cada cliente é escalonado (delay progressivo).
        - Aguarda todos os clientes terminarem antes de encerrar.
    """
    
    clients = [] # lista para armazenar threads de clientes
    clients_count = 6 # número total de clientes a simular
    for i in range(clients_count):
        # cada cliente entra em um tempo diferente
        delay = i * 2   # Cliente1 = 0s, Cliente2 = 2s, etc
        t = Thread(target=simulate_client, args=(f"Cliente{i+1}", delay)) # cria thread 
        clients.append(t) # adiciona thread na lista
        t.start() # inicia thread

    # Aguarda todos os clientes terminarem
    for t in clients:
        t.join()

if __name__ == "__main__":
    start_test()
