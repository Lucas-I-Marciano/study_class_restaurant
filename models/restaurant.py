class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) :
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) :
        return f'{self._nome} | {self._categoria} | {self.ativo}'

    def alterna_status(self):
        self._ativo = not self._ativo

    @classmethod
    def lista_restaurantes(cls) :
        print('-'*60)
        print('Nome'.ljust(20), "|", "Categoria".ljust(20), "|", "Status")
        print('-'*60)
        for restaurante in cls.restaurantes :
            print(restaurante._nome.ljust(20), "|", restaurante._categoria.ljust(20), "|", restaurante.ativo)

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

