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

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone




if __name__ == "__main__":
    # Teste da classe Contato
    contato1 = Contato("João", "123456789")
    print(contato1)