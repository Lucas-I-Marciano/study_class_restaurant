from models.avaliacoes import Avaliacoes
from models.cardapio.itemCardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) : 
        """Função para inicializar minhas instâncias da classe Restaurante

        Args:
            nome (string): nome do restaurante
            categoria (string): categoria do restaurante
            ativo (boolean): parâmetro para avaliar o status do restaurante na plataforma
            avaliacoes(list[class]): Lista de classe de avaliações 
        """       
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self) :
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria} | {self.ativo}'

    def alterna_status(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    @classmethod
    def lista_restaurantes(cls) :
        """Exibe uma lista formatada de todos os restaurantes."""
        linha = '*'*90
        print(linha)
        print('Nome'.ljust(20), "|", "Categoria".ljust(20), "|", "Avaliações".ljust(20), "|", "Status")
        print(linha)
        for restaurante in cls.restaurantes :
            print(restaurante._nome.ljust(20), "|", restaurante._categoria.ljust(20), "|", str(restaurante.calcula_media_avaliacoes).ljust(20), "|", restaurante.ativo)

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return "☑" if self._ativo else "☐"

    def adiciona_avaliacao(self, cliente, nota):
        """Adiciona uma avaliação para o restaurante

        Args:
            cliente (string): nome do cliente que está avaliando
            nota (float): nota dada pelo cliente para o restaurante

        Returns:
            (string): Mensagem caso o valor esteja inadequado
        """        
        if 0 <= nota <= 5 :
            avaliacao = Avaliacoes(cliente, nota)
            self._avaliacoes.append(avaliacao)
            return
        return print("Nota deve estar entre 0 e 5")

    @property
    def calcula_media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante.

        Returns:
            (float): média das notas das avaliações
        """
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum([avaliacao._nota for avaliacao in self._avaliacoes])
        total_de_notas = len(self._avaliacoes)
        return round(soma_das_notas / total_de_notas, 1)

    def adiciona_item_no_cardapio(self, item) :
        if isinstance(item, ItemCardapio) :
            self._cardapio.append(item)

    @property
    def lista_cardapio(self):
        titulo = f'Cardápio do {self._nome}'
        print(titulo)
        print('-'*len(titulo))
        subtitulo = f'{'Item'.ljust(4)} | {'Nome'.ljust(25)} | {'Preço'.ljust(5)} |'
        print(subtitulo)
        print('*'*len(subtitulo))
        for i,item in enumerate(self._cardapio):
            mensagem = f'.{str(i).ljust(3)} | {item._nome.ljust(25)} | {str(round(item._preco, 2)).ljust(5)}'
            if hasattr(item, '_descricao') :
                mensagem = f'{mensagem} | {item._descricao}'
            if hasattr(item, '_tamanho') :
                mensagem = f'{mensagem} | {item._tamanho}'
            print(mensagem)

