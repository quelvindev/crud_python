

class Empresa:

    def __init__(self,id,empresa) -> None:
        self.id = id 
        self.empresa = empresa

    def __str__(self) -> str:
        return f'{self.id} {self.empresa}'