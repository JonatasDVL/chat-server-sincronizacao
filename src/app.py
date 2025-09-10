from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Estrutura:
waiting_queue = []  # lista de (sid, username) esperando
active_clients = {}  # {sid: username} clientes ativos no chat

MAX_ACTIVE = 5  # por exemplo, só 3 clientes ativos ao mesmo tempo

# Rota admin
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Rota cliente
@app.route('/')
def client():
    return render_template('client.html')

# Cliente conecta
@socketio.on('connect')
def handle_connect():
    print(f"Cliente conectado: {request.sid}")

# Cliente envia nome para entrar na fila
@socketio.on('join')
def handle_join(data):
    username = data['username']
    # adiciona à fila
    waiting_queue.append((request.sid, username))
    print(f"{username} entrou na fila.")

    try_activate_clients()
    update_admin()

def try_activate_clients():
    """Move clientes da fila para ativo se houver vaga"""
    while waiting_queue and len(active_clients) < MAX_ACTIVE:
        sid, username = waiting_queue.pop(0)
        active_clients[sid] = username
        # avisa o cliente que ele está ativo
        socketio.emit('activated', {}, to=sid)
        print(f"{username} agora está ativo.")

# Cliente envia mensagem
@socketio.on('message')
def handle_message(data):
    if request.sid not in active_clients:
        return  # só clientes ativos podem mandar mensagem
    user = active_clients[request.sid]
    msg = data['msg']
    emit('message', {'user': user, 'msg': msg}, broadcast=True)

# Cliente clica em sair
@socketio.on('leave')
def handle_leave():
    # remove de ativos ou da fila
    if request.sid in active_clients:
        username = active_clients.pop(request.sid)
        print(f"{username} saiu do chat ativo.")
    else:
        for i, (sid, username) in enumerate(waiting_queue):
            if sid == request.sid:
                waiting_queue.pop(i)
                print(f"{username} saiu da fila.")
                break
    try_activate_clients()
    update_admin()
    # Confirma para o cliente
    emit('left', {})

# Cliente desconecta
@socketio.on('disconnect')
def handle_disconnect():
    # remove de ativos ou da fila
    if request.sid in active_clients:
        username = active_clients.pop(request.sid)
        print(f"{username} saiu do chat ativo.")
    else:
        # remover da fila se ainda estava esperando
        for i, (sid, username) in enumerate(waiting_queue):
            if sid == request.sid:
                waiting_queue.pop(i)
                print(f"{username} saiu da fila.")
                break
    try_activate_clients()  # ativa próximos da fila
    update_admin()

def update_admin():
    """Atualiza admin com lista de ativos e fila"""
    emit('update_admin', {
        'active': list(active_clients.values()),
        'waiting': [name for _, name in waiting_queue]
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
