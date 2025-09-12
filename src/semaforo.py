import threading

class Semaforo:
    def __init__(self, valor_inicial: int = 1) -> None:
        """
        Cria um semáforo com valor inicial especificado.

        Parâmetros:
            valor_inicial (int): Número máximo de recursos disponíveis. Default = 1

        Atributos:
            self.valor: contador interno do semáforo.
            self.lock: Lock para garantir exclusão mútua.
            self.condicao: Condition para gerenciar espera de threads.
        """
        self.valor = valor_inicial
        self.lock = threading.Lock()
        self.condicao = threading.Condition(self.lock)

    def adquirir(self) -> None:
        """
        Adquire o semáforo, bloqueando a thread se nenhum recurso estiver disponível.

        Comportamento:
            1. Bloqueia a thread enquanto self.valor == 0 (espera que um recurso seja liberado)
            2. Quando houver recurso disponível, decrementa self.valor e prossegue.
        """
        with self.lock:
            while self.valor == 0:
                # 1. Bloqueia a thread enquanto self.valor == 0
                self.condicao.wait()
            # 2. Decrementa self.valor e prossegue
            self.valor -= 1

    def liberar(self) -> None:
        """
        Libera o semáforo, aumentando o valor de recursos disponíveis.

        Comportamento:
            1. Incrementa self.valor
            2. Notifica uma thread que possa estar esperando (condicao.notify)
        """
        with self.lock:
            # 1. Incrementa self.valor
            self.valor += 1
            # 2. Notifica uma thread que possa estar esperando
            self.condicao.notify()

    def tentar_adquirir(self) -> bool:
        """
        Tenta adquirir o semáforo sem bloquear a thread.

        Retorno:
            True se conseguiu adquirir (self.valor > 0)
            False caso contrário
        """
        with self.lock:
            if self.valor > 0:
                # Decrementa self.valor e prossegue
                self.valor -= 1
                return True
            # Caso contrário, retorna False
            return False

