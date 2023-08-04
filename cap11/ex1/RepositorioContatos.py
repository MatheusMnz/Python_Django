from Contato import Contato
from io import open

class RepositorioContatos:
    def __init__(self) -> None:
        self.__repositorio_contatos = []


    @property
    def repositorio_contatos(self)-> str:
        return self.__repositorio_contatos
    

    def incluir(self, contato: Contato) -> Contato:
        resultado = None
        if not contato == None:
            self.__repositorio_contatos.append(contato)
            resultado = contato
        else:
            print("Um contato deve ser fornececido.")
        return resultado
    

    def atualizar(self, indice:int, contato:Contato) -> None:
        resultado = None
        if contato == None:
            print("Um contato deve ser fornecido.")
        elif indice == None:
            print("Um índice deve ser fornecido.")
        elif indice < 0:
            print("O índice não pode ser negativo.")
        else:
            self.__repositorio_contatos[indice] = contato
            resultado = contato
        return resultado
    

    def excluir_por_indice(self, indice:int) -> Contato:
        resultado = None
        if indice == None:
            print("Um índice deve ser fornecido.")
        elif indice < 0:
            print("O índice não pode ser negativo.")
        else:
            resultado = self.__repositorio_contatos.pop(indice)
        return resultado


    def consultar_indice_por_nome(self, nome:str) -> int:
        resultado = -1
        indice = -1
        
        for i in range(0, len(self.__repositorio_contatos)):
            contato = self.__repositorio_contatos[i]
            if contato.nome == nome:
                indice = i
        if indice != -1:
            resultado = indice
        return resultado
    
    def consultar_indice_por_telefone(self, telefone: str) -> int:
        resultado = -1
        for i in range(len(self.__repositorio_contatos)):
            contato = self.__repositorio_contatos[i]
            if contato.telefone == telefone:
                resultado = i
                break
        return resultado

    def existe(self, nome:Contato) -> bool:
        resultado = False
        for i in range(0, len(self.__repositorio_contatos)):
            contato_atual = self.__repositorio_contatos[i]
            if contato_atual.nome == nome:
                resultado = True
                break
        return resultado
    
    
    def vazio(self) -> bool:
        return (len(self.__repositorio_contatos) == 0)
    

    def salvar_em_arquivo(self, nome_arquivo: str) -> None:
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                for contato in self.__repositorio_contatos:
                    arquivo.write(f"{contato.nome};{contato.telefone}\n")
            print("Contatos salvos com sucesso no arquivo.")
        except IOError as e:
            print(f"Erro ao salvar o arquivo: {str(e)}")
    