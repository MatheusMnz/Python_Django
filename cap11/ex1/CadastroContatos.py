from Contato import Contato
from RepositorioContatos import RepositorioContatos


class CadastroContatos:
    def __init__(self) -> None:
        self.__repositorio_contatos = RepositorioContatos()

    @property
    def repositorio_contatos(self) -> str:
        return self.__repositorio_contatos
    

    def incluir(self, contato:Contato) -> Contato:
        resultado = None
        if self.__repositorio_contatos.existe(contato) == True:
            input("Contato já cadastrado. Tecle <ENTER>.")
        else:
            resultado = self.__repositorio_contatos.incluir(contato)
        return resultado
    

    def alterar(self, contato: Contato) -> Contato:
        resultado = None
        indice = self.__repositorio_contatos.consultar_indice_por_nome(contato.nome)
        if indice == -1:
            input("Contato não encontrado. Tecle <ENTER>.")
        else:
            resultado = self.__repositorio_contatos[indice]
            resultado.nome = contato.nome
            resultado.telefone = contato.telefone
        return resultado
    
    def excluir(self, telefone: str) -> Contato:
        resultado = None
        indice = self.__repositorio_contatos.consultar_indice_por_telefone(telefone)
        if indice != -1:
            resultado = self.__repositorio_contatos[indice]
            self.__repositorio_contatos.excluir_por_indice(indice)
        else:
            print("Contato não encontrado.")
        return resultado


    def consultar(self, nome: str) -> Contato:
        resultado = None
        indice = self.__repositorio_contatos.consultar_indice_por_nome(nome)
        if indice != -1:
            resultado = self.__repositorio_contatos[indice]
        return resultado

    
if __name__ == "__main__":
    # Teste da classe CadastroContatos
    cadastro = CadastroContatos()
    contato1 = Contato("João", "123456789")
    cadastro.incluir(contato1)

    contato2 = Contato("Maria", "987654321")
    cadastro.incluir(contato2)

    # Alterar o contato de nome "João"
    contato_alterado = Contato("João Silva", "999999999")
    cadastro.alterar(contato_alterado)

    # Excluir um contato pelo telefone
    cadastro.excluir("987654321")

    # Consultar contato pelo nome
    contato_consultado = cadastro.consultar("João Silva")
    print(contato_consultado)