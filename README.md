# Chat Server - Sincronização de Processos

## Descrição do Projeto
Este projeto implementa um **Servidor de Chat** que permite múltiplos usuários se conectarem e trocarem mensagens em tempo real. No entanto, o servidor só pode gerenciar um número limitado de conexões simultâneas. O problema envolve aceitar novas conexões, gerenciar mensagens entre os usuários conectados e garantir que o servidor não sobrecarregue. Considerações: Use semáforos ou para controlar o número de conexões ativas e garantir que novas conexões só sejam aceitas quando houver capacidade disponível (exemplo: número máximo de conexões = 5). Implemente uma lógica de fila para mensagens, garantindo que elas sejam entregues na ordem correta e sem perda de dados.

O objetivo principal é aplicar conceitos de **sincronização de processos** usando **semáforos**, garantindo que o servidor não exceda o número máximo de conexões simultâneas e que as mensagens sejam entregues na ordem correta.

O servidor foi implementado em **Python** utilizando threads, filas e semáforos para controlar o fluxo de conexão e comunicação entre os clientes.

---

## Equipe
- **Aluno 1:** Anderson da Silva Passos  
- **Aluno 2:** Francisco Colatino de Lima
- **Aluno 3:** Jônatas Duarte Vital Leite

**Tema do Trabalho:** Servidor de Chat com controle de conexões e filas de mensagens  

**Curso:** Ciência da Computação  
**Disciplina:** Sistemas Operacionais  
**Professor:** Prof. Dr. Tércio Silva   

---

## Funcionalidades
1. Limite de conexões simultâneas com **semáforo** (ex: máximo 5 clientes conectados ao mesmo tempo).  
2. Aceitação de novas conexões apenas quando houver capacidade disponível.  
3. Gestão de mensagens com **fila**, garantindo entrega na ordem correta.  
4. Broadcast das mensagens para todos os clientes conectados.  
5. Tratamento de desconexões, liberando espaço no servidor para novos usuários.

---

## Tecnologias Utilizadas
- **Python 3.x**  
- Módulos: `socket`, `threading`, `queue`  
- Conceitos aplicados: **Concorrência**, **Semáforos**, **Filas de Mensagens**

---

## Estrutura do Projeto

````
chat-server-sincronizacao/
├── README.md # Documentação do projeto
├── requirements.txt # Bibliotecas necessárias
├── src/ # Código-fonte
│ ├── servidor.py # Servidor principal
│ └── cliente.py # Cliente para testes
│ └── simulacao.py # Simulação de clientes para testes
│ └── fila.py # Implementação da fila
│ └── semaforo.py # # Implementação do semáforo
````

---

## Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/chat-server-sincronizacao.git
cd chat-server-sincronizacao/src
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Rodar o servidor
```bash
python ./src/servidor.py
```

### 4. Conectar clientes
```bash
python ./src/cliente.py
```

### 5. Utilizar o Simulador
```bash
python ./src/simulacao.py
```

É possível rodar múltiplos clientes simultaneamente para testar o limite de conexões e o broadcast das mensagens.

## Exemplo de Uso

1. Inicie o servidor (servidor.py).

2. Abra 6 ou mais terminais e rode cliente.py em cada um.

3. Envie mensagens nos clientes e veja que todas são recebidas pelos demais em ordem correta.

4. Se o limite de conexões for atingido, novos clientes receberão mensagem de Servidor cheio e serão encerrados.

## Observações

- O servidor suporta apenas mensagens em broadcast (todos recebem a mesma mensagem).

- O número máximo de conexões pode ser alterado modificando MAX_CONNECTIONS no servidor.py.

- O código é uma implementação didática para sincronização de processos usando semáforos.

## Outro Exemplo de Uso

## Exemplo de Uso

1. Inicie o servidor (servidor.py).

2. Abra 1 ou 2 terminais e rode cliente.py em cada um.

3. Abra um terminal e rode o simulacao.py, nele você pode testar o limite de conexões e o broadcast de mensagens, além de conseguir testar a fila para mensagens, garantindo que elas sejam entregues na ordem correta e sem perda de dados.

## Licença

Este projeto é para fins acadêmicos e não possui licença comercial.
