from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor) -> None:
        super().__init__(marca, modelo)
        self.cor = cor
    
    def ligar(self):
        pass
