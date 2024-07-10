
class Funcionario:

    def __init__(self,id,nome,sobrenome,email) -> None:
        self.id = id
        self.nome = nome
        self.sobremome = sobrenome
        self.emal = email


    def __str__(self) -> str:
        return f' {self.id} {self.nome} {self.sobremome} {self.emal}'
    
    def nome_completo(self):
        return f' {self.nome} {self.sobremome} '
    
    

