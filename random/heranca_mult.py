class Pessoa:
    def __init__(self) -> None:
        super().__init__()
        self._nome = 'João'
        self.idade = 25

    @property
    def nome(self) -> str:
        return self._nome
    
class Aluno:
    def __init__(self) -> None:
        super().__init__()
        self._nome_aluno = 'José'
        self.matricula = '555'

    @property
    def nome(self) -> str:
        return self._nome_aluno
    
class Residente(Pessoa, Aluno):
    def __init__(self) -> None:
        super().__init__()

    @property
    def nome(self) -> str:
        return self._nome

residente = Residente()
print("Nome:", residente.nome)         
print("Idade:", residente.idade)       
print("Matrícula:", residente.matricula)
