from models.avaliacoes import Avaliacoes

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) : 
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self) :
        return f'{self._nome} | {self._categoria} | {self.ativo}'

    def alterna_status(self):
        self._ativo = not self._ativo

    @classmethod
    def lista_restaurantes(cls) :
        linha = '*'*90
        print(linha)
        print('Nome'.ljust(20), "|", "Categoria".ljust(20), "|", "Avaliações".ljust(20), "|", "Status")
        print(linha)
        for restaurante in cls.restaurantes :
            print(restaurante._nome.ljust(20), "|", restaurante._categoria.ljust(20), "|", str(restaurante.calcula_media_avaliacoes).ljust(20), "|", restaurante.ativo)

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    def adiciona_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5 :
            return print("Nota deve estar entre 0 e 5")
        avaliacao = Avaliacoes(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def calcula_media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum([avaliacao._nota for avaliacao in self._avaliacoes])
        total_de_notas = len(self._avaliacoes)
        return round(soma_das_notas / total_de_notas, 1)

