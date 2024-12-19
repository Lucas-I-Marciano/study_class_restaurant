class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) :
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) :
        return f'{self.nome} | {self.categoria} | {self.ativo}'

    @classmethod
    def lista_restaurantes(cls) :
        print('-'*60)
        print('Nome'.ljust(20), "|", "Categoria".ljust(20), "|", "Status")
        print('-'*60)
        for restaurante in cls.restaurantes :
            print(restaurante.nome.ljust(20), "|", restaurante.categoria.ljust(20), "|", restaurante.ativo)

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"


restaurante_sushi = Restaurante('Sushi', 'japonesa')
restaurante_praca = Restaurante('Praca', 'italiana')

print('\nrestaurante_sushi:', restaurante_sushi)

Restaurante.lista_restaurantes()

