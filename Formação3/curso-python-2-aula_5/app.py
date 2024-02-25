from modelos.Cardapio.bebidas import Bebidas
from modelos.Cardapio.pratos import Pratos
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida1 = Bebidas("Cerveja", 5.00, "250ml")
prato1 = Pratos("Macarrão",10.00,"Espaghetti ao sugo com medalhões de filé mignon")

restaurante_praca.adicionar_no_cardapio(bebida1)
restaurante_praca.adicionar_no_cardapio(prato1)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()