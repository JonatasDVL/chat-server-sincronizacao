import threading

class Fila:
    def __init__(self):
        self.itens = []
        self.lock = threading.Lock()
        self.condicao = threading.Condition(self.lock)

    def put(self, item):
        with self.lock:
            self.itens.append(item)
            self.condicao.notify()

    def get(self):
        with self.lock:
            while not self.itens:
                self.condicao.wait()
            return self.itens.pop(0)
