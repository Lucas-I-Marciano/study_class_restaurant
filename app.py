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

bebida_coca = ItemBebida("Coke", 12.99, "Grande")
bebida_coca.aplica_desconto(0.10)
prato_sushi_salmao = ItemPrato("Sashimi de Salmão", 25.50, "Fatias de salmão cru")
prato_sushi_atum = ItemPrato("Sashimi de Atum", 20, "Fatias de atum cru")
prato_sushi_atum.aplica_desconto(0.2)
prato_temaki = ItemPrato("Temaki", 12.99, "Temaki califórnia")
prato_misoshiro = ItemPrato("Misoshiro", 25, "Sopa de soja")
restaurante_kanpek.adiciona_item_no_cardapio(prato_sushi_salmao)
restaurante_kanpek.adiciona_item_no_cardapio(prato_sushi_atum)
restaurante_kanpek.adiciona_item_no_cardapio(prato_temaki)
restaurante_kanpek.adiciona_item_no_cardapio(prato_misoshiro)
restaurante_kanpek.adiciona_item_no_cardapio(bebida_coca)

def main():
    os.system('cls')
    restaurante_kanpek.lista_cardapio

    
    


if __name__ == "__main__" :
    main()