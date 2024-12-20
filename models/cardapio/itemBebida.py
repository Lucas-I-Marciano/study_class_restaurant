from models.cardapio.itemCardapio import ItemCardapio

class ItemBebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho) :
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome.ljust(20)} : R$:{str(self._preco).ljust(5)} | {self._tamanho}'

    def aplica_desconto(self, desconto):
        self._preco -= self._preco * desconto
