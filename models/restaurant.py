class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) :
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) :
        return f'{self.nome} | {self.categoria} | {self.ativo}'

    def lista_restaurantes() :
        print('-'*30)
        print('nome'.ljust(20), "|", "categoria")
        print('-'*30)
        for restaurante in Restaurante.restaurantes :
            print(restaurante.nome.ljust(20), "|", restaurante.categoria)


restaurante_sushi = Restaurante('Sushi', 'japonesa')
print('\n',restaurante_sushi.nome)

restaurante_praca = Restaurante('Praca', 'italiana')
print('\n',restaurante_praca.nome) 

print('\ndir: ', dir(restaurante_sushi))
print('\nvars: ', vars(restaurante_sushi))
print('\nrestaurante_sushi:', restaurante_sushi)

Restaurante.lista_restaurantes()

