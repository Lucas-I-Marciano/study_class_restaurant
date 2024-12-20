from models.cardapio.itemCardapio import ItemCardapio

class ItemPrato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'{self._nome.ljust(20)} : R$:{str(self._preco).ljust(5)} | {self._descricao}'