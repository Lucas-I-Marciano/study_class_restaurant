class Avaliacoes:
    def __init__(self, cliente, nota):
        """Inicializa uma instância da classe Avaliações

        Args:
            cliente (string): Nome do cliente que está avaliando
            nota (float): Nota que o cliente deu para o restaurante
        """        
        self._cliente = cliente
        self._nota = nota