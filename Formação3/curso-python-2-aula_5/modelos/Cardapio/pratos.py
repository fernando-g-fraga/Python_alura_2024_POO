from modelos.Cardapio.item_cardapio import ItemCardapio

class Pratos(ItemCardapio):
    def __init__(self,nome,preco,descricao) -> None:
        super().__init__(nome,preco)
        self.descricao = descricao

      