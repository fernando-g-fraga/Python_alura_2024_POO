from modelos.Cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco,tipo,tamanho) -> None:
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
    
    def __str__(self) -> str:
        return self._nome

    def aplicar_desconto(self):
        pass
