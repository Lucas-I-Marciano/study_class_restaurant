class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_sushi = Restaurante()
restaurante_sushi.nome = 'Sushi'
restaurante_sushi.categoria = 'japonesa'

print('\ndir: ', dir(restaurante_sushi))
print('\nvars: ', vars(restaurante_sushi))

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praca'
restaurante_praca.categoria = 'italiana'