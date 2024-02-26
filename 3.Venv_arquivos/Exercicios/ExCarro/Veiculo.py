class Veiculo():
    def __init__(self,marca,modelo,ligado=False) -> None:
        self.marca = marca
        self.modelo = modelo
        self._ligado = ligado

    def __str__(self) -> str:
        return f'{self.marca} | {self.modelo} | {self._ligado}'
