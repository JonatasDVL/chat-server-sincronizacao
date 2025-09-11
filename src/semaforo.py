import threading

class Semaforo:
    def __init__(self, valor_inicial: int = 1) -> None:
        self.valor = valor_inicial
        self.lock = threading.Lock()
        self.condicao = threading.Condition(self.lock)

    def adquirir(self) -> None:
        with self.lock:
            while self.valor == 0:
                self.condicao.wait()
            self.valor -= 1

    def liberar(self) -> None:
        with self.lock:
            self.valor += 1
            self.condicao.notify()

    def tentar_adquirir(self) -> bool:
        with self.lock:
            if self.valor > 0:
                self.valor -= 1
                return True
            return False
