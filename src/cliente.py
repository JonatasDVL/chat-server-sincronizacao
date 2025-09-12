from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

# Configurações do cliente
HOST = 'localhost'
PORT = 5555

# Função para receber mensagens do servidor
def receive_messages(client_socket):
    """
    Thread responsável por receber mensagens do servidor.

    - Aguarda mensagens do servidor em loop.
    - Imprime as mensagens recebidas na tela do cliente.
    - Encerra a conexão caso:
        * A mensagem recebida seja vazia (servidor desconectou).
        * A mensagem comece com "[ERRO]" (servidor recusou ou limite atingido).
    """
    while True:
        try:
            # Recebe mensagem do servidor
            msg = client_socket.recv(1024).decode()
            
            # Se a mensagem for vazia, sai do loop
            if not msg:
                break
            
            # Imprime a mensagem recebida
            print(msg)
            
            # Se a mensagem for de erro, sai do programa
            if msg.startswith("[ERRO]"):
                print("Encerrando cliente...")
                client_socket.close()
        except:
            # Se houver erro, sai do loop
            break

# Função para iniciar o cliente
def start_client():
    """
    Inicializa o cliente de chat TCP.

    1. Tenta se conectar ao servidor no host/porta definidos.
    2. Inicia uma thread para ouvir mensagens do servidor (função receive_messages).
    3. Aguarda entrada do usuário (input):
        - Se a mensagem for "sair", encerra a conexão.
        - Caso contrário, envia a mensagem digitada ao servidor.
    4. Fecha a conexão ao sair.
    """
    client_socket = socket(AF_INET, SOCK_STREAM)
    try:
        # Conecta ao servidor
        client_socket.connect((HOST, PORT))
    except:
        # Se não conectar, imprime mensagem de erro e sai
        print("Não foi possível conectar ao servidor.")
        return

    # Inicia thread para receber mensagens do servidor
    Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    
    while True:
        try:
            # Pega input do usuário
            msg = input()
            
            # Se o input for "sair", sai do loop
            if msg.lower() == "sair":
                break
            
            # Envia mensagem para o servidor
            client_socket.send(msg.encode())
        except:
            # Se houver erro, sai do loop
            break
    
    # Fecha a conexão com o servidor
    client_socket.close()

if __name__ == "__main__":
    start_client()

