from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo, ligado=False) -> None:
        super().__init__(marca, modelo, ligado)
        self.tipo = tipo
   
    def __str__(self) -> str:
        return f'{self.marca} | {self.modelo} | {self._ligado} | {self.tipo}'
    
