from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, ligado=False) -> None:
        super().__init__(marca, modelo, ligado)
        self.portas = portas
    
    def __str__(self) -> str:
        return f'{self.marca} | {self.modelo} | {self._ligado} | {self.portas}'
    