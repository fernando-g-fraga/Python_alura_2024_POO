from modelos.Cardapio.item_cardapio import ItemCardapio

class Bebidas(ItemCardapio):
    def __init__(self,nome,preco,tamanho) -> None:
        super().__init__(nome,preco)
        self._tamanho = tamanho

    def __str__(self) -> str:
        return self._nome