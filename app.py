from models.restaurant import Restaurante

restaurante_kanpek = Restaurante("Kanpek", "japonesa")
restaurante_brooks = Restaurante("Brooks", "lanche")
restaurante_kfc = Restaurante("KFC", "fast-food")
restaurante_sujinho = Restaurante("Sujinho", "brasileira")

def main():
    Restaurante.lista_restaurantes()
    


if __name__ == "__main__" :
    main()