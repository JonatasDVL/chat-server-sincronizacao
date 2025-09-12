import threading

class Fila:
    def __init__(self):
        """
        Inicializa a fila vazia com suporte a threads.

        Atributos:
            self.itens: lista interna que armazena os elementos da fila.
            self.lock: Lock para garantir exclusão mútua ao acessar self.itens.
            self.condicao: Condition para gerenciar espera de threads quando a fila está vazia.
        """
        self.itens = []  # lista interna que armazena os elementos da fila
        self.lock = threading.Lock()  # Lock para garantir exclusão mútua ao acessar self.itens
        self.condicao = threading.Condition(self.lock)  # Condition para gerenciar espera de threads quando a fila está vazia

    def put(self, item):
        """
        Adiciona um item à fila.

        Parâmetros:
            item: objeto a ser inserido na fila.

        Comportamento:
            - Adiciona o item no final da lista (FIFO).
            - Notifica uma thread que esteja esperando por itens (self.condicao.notify()).
        """
        with self.lock:  # garante exclusão mútua ao acessar self.itens
            self.itens.append(item)  # adiciona o item no final da lista (FIFO)
            self.condicao.notify()  # notifica uma thread que esteja esperando por itens

    def get(self):
        """
        Remove e retorna o primeiro item da fila.

        Comportamento:
            - Bloqueia a thread se a fila estiver vazia (self.condicao.wait()).
            - Retorna o primeiro item assim que estiver disponível.
        """
        with self.lock:  # garante exclusão mútua ao acessar self.itens
            while not self.itens:  # bloqueia a thread se a fila estiver vazia
                self.condicao.wait()
            return self.itens.pop(0)  # retorna o primeiro item assim que estiver disponível

