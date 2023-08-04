class Contato:
    def __init__(self, nome:str, telefone:str) -> None:
        self.__nome = nome
        self.__telefone = telefone

    def __str__(self) -> str:
        resultado = '\nNome: ' + self.__nome
        resultado += '\nTelefone: ' + self.__telefone
        return resultado
    

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def telefone(self) -> str:
        return self.__telefone
    
    @nome.setter
    def nome(self, nome:str ):
        self.__nome = nome

    