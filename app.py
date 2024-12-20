import os
from models.restaurant import Restaurante
from models.cardapio.itemBebida import ItemBebida
from models.cardapio.itemPrato import ItemPrato

restaurante_kanpek = Restaurante("Kanpek", "japonesa")
restaurante_brooks = Restaurante("Brooks", "lanche")
restaurante_kfc = Restaurante("KFC", "fast-food")
restaurante_sujinho = Restaurante("Sujinho", "brasileira")

restaurante_kanpek.alterna_status()
restaurante_kanpek.adiciona_avaliacao("Lucas", 5)
restaurante_kanpek.adiciona_avaliacao("Thaina", 5)
restaurante_kanpek.adiciona_avaliacao("Adriana", 4)
# ---------------------------------------------------------------

bebida_coca = ItemBebida("Coke", 12, "Grande")
prato_strogo = ItemPrato("Sashimi", 25, "Fatias de salmão cru")

def main():
    os.system('cls')    
    print(prato_strogo)
    print(bebida_coca)

    
    


if __name__ == "__main__" :
    main()