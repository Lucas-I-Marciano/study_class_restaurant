class Restaurante:
    def __init__(self, nome, categoria) :
        self.nome = nome
        self.categoria = categoria
        self.ativo = False


restaurante_sushi = Restaurante('Sushi', 'japonesa')
print('\n',restaurante_sushi.nome)

restaurante_praca = Restaurante('Praca', 'italiana')
print('\n',restaurante_praca.nome) 

print('\ndir: ', dir(restaurante_sushi))
print('\nvars: ', vars(restaurante_sushi))
print('\nrestaurante_sushi', restaurante_sushi)
