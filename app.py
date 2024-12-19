from models.restaurant import Restaurante

restaurante_kanpek = Restaurante("Kanpek", "japonesa")
restaurante_brooks = Restaurante("Brooks", "lanche")
restaurante_kfc = Restaurante("KFC", "fast-food")
restaurante_sujinho = Restaurante("Sujinho", "brasileira")

restaurante_kanpek.alterna_status()
restaurante_kanpek.adiciona_avaliacao("Lucas", 5)
restaurante_kanpek.adiciona_avaliacao("Thaina", 5)
restaurante_kanpek.adiciona_avaliacao("Adriana", 4)


def main():
    Restaurante.lista_restaurantes()
    


if __name__ == "__main__" :
    main()