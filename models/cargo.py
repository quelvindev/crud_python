
class Cargo:
    def __init__(self,id,cargo) -> None:
        self.id = id
        self.cargo = cargo

    def __str__(self) -> str:
        return f'{self.id} {self.cargo}'
    
    