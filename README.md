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
- **Python 3.13.3**  
- Módulos: `socket`, `threading`, `queue`  
- Conceitos aplicados: **Concorrência**, **Semáforos**, **Filas de Mensagens**

---

## Estrutura do Projeto

````
chat-server-sincronizacao/
├── README.md # Documentação do projeto
├── requirements.txt # Bibliotecas necessárias
├── src/ # Código-fonte
│ ├── server.py # Servidor principal
│ └── client.py # Cliente para testes
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
python ./src/app.py
```

### 4. Acesse
<a href="http://127.0.0.1:5000/">Acesse o chat</a> e <a href="http://127.0.0.1:5000/admin">painel de controle</a>

É possível rodar múltiplos clientes simultaneamente para testar o limite de conexões e o broadcast das mensagens.

## Exemplo de Uso

1. Inicie o servidor (server.py).

2. Abra 3 ou mais terminais e rode client.py em cada um.

3. Envie mensagens nos clientes e veja que todas são recebidas pelos demais em ordem correta.

4. Se o limite de conexões for atingido, novos clientes receberão mensagem de Servidor cheio.

## Observações

- O servidor suporta apenas mensagens em broadcast (todos recebem a mesma mensagem).

- O número máximo de conexões pode ser alterado modificando MAX_CONNECTIONS no server.py.

- O código é uma implementação didática para sincronização de processos usando semáforos.

## Diagramas e Documentação

Toda a documentação adicional, diagramas de fluxo e prints de execução estão na pasta docs/.

## Licença

Este projeto é para fins acadêmicos e não possui licença comercial.