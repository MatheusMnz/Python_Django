from CadastroContatos import CadastroContatos
from Contato import Contato
from io import open

class ContatosApp:
    def __init__(self) -> None:
        self.__regras_negocio = CadastroContatos()
        self.__loop_principal()

    def __exibe_menu(self) -> None:
        self.__limpar_tela()
        print("\n Selecione uma opção: ")
        print("\n 1. Incluir novo contato ")
        print("\n 2. Alterar telefone de um contato ")
        print("\n 3. Excluir um contato ")
        print("\n 4. Consultar por nome ")
        print("\n 5. Listar todos os contatos cadastrados ")
        print("\n 6. Sair ")


    def __limpar_tela(self) -> None:
        print("\n" * 100)
    

    def __opcao_selecionada(self) -> int:
        opcao = input("\nEscolha uma opção: ")
        if opcao == '':
            resultado = -1
        else:
            resultado = int(opcao)
        return resultado
    

    def __ler_dados_contato(self) -> Contato:
        self.__limpar_tela()
        telefone = input("\n Telefone: ")
        nome = input("\n Nome: ")
        resultado = Contato(nome, telefone)
        return resultado
    
    
    def salvar_contatos_em_arquivo(self, nome_arquivo: str) -> None:
        self.__regras_negocio.repositorio_contatos.salvar_em_arquivo(nome_arquivo)


    def __loop_principal(self)->None:
        opcao = -1
        while opcao!=6:
            self.__exibe_menu()
            opcao = self.__opcao_selecionada()
            if opcao==1:
                contato = self.__ler_dados_contato()
                if self.__regras_negocio.incluir(contato) != None:
                    print('\nContato cadastrado com sucesso.')
            elif opcao==2:
                contato = self.__ler_dados_contato()
                if self.__regras_negocio.alterar(contato) != None:
                    print('\nContato alterado com sucesso.')
            elif opcao==3:
                self.__limpar_tela()
                telefone = input('\nTelefone: ')
                if self.__regras_negocio.excluir(telefone) != None:
                    print('\nContato excluido.')
            elif opcao==4:
                self.__limpar_tela()
                nome = input('\nDigite o nome do contato a localizar: ')
                contato = self.__regras_negocio.consultar(nome)
                if contato != None:
                    print(f'Contato encontrado: \n{contato}\n')
            elif opcao==5:
                self.__limpar_tela()
                if not self.__regras_negocio.repositorio_contatos.vazio():
                    for contato in self.__regras_negocio.repositorio_contatos.repositorio_contatos:
                        print(f'\n{contato}\n')
                else:
                    print(f'\nNenhum contato cadastrado.')
            if opcao!=6:
                input('Tecle enter para retornar ao menu...')

        self.salvar_contatos_em_arquivo('/home/matheus/work/python_django_/cap11/ex1/contatos.txt')

app = ContatosApp()

        
    