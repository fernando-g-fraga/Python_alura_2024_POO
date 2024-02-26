from abc import ABC,abstractmethod

class Veiculo(ABC):
    def __init__(self,marca,modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    def __str__(self) -> str:
        return f'{self.marca} | {self.modelo}'


    @abstractmethod
    def ligar(self):
        pass


    