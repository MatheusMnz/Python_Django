""" Agenda Telefonica """

""" Classe que representa um contato """
class Contato:

    def __init__(self, fone: str, nome:str)->None:
        self.__fone = fone
        self.__nome = nome
    def __str__(self)->str:
        resultado = '\nNome: ' + self.__nome
        resultado += '\nFone: ' + self.__fone
        return resultado

    @property
    def fone(self)->str:
        return self.__fone

    @property
    def nome(self)->str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str)->None:
        self.__nome = nome

class RepositorioContatos:

    def __init__(self):
        self.__repositorio_contatos = []

    @property
    def repositorio_contatos(self)->str:
        return self.__repositorio_contatos

    def incluir(self, contato: Contato)->Contato:
        """ Recebe um objeto do tipo Contato e armazena-o no repositorio. """
        resultado = None
        if not contato == None:
            self.__repositorio_contatos.append(contato)
            resultado = contato
        else:
            print('Um contato deve ser fornecido.')
        return resultado

    def atualizar(self, indice: int, contato: Contato)->None:
        """ Recebe um objeto do tipo Contato, localiza-o no repositorio
            e atualiza seus dados. """
        resultado = None
        if (contato == None):
            print('Um contato deve ser fornecido.')
        elif (indice == None):
            print('Um indice deve ser fornecido.')
        elif (indice < 0):
            print('Indice nao deve ser negativo.')
        else:
            self.__repositorio_contatos[indice] = contato
            resultado = contato
        return resultado

    def excluir_por_indice(self, indice: int)->None:
        """ Recebe o índice de um contato do repositório e o remove. """
        resultado = None
        if (indice == None):
            print('Um indice deve ser fornecido.')
        elif (indice < 0):
            print('Indice nao deve ser negativo.')
        else:
            resultado = self.__repositorio_contatos.pop(indice)
        return resultado

    def consultar_indice_por_nome(self, nome: str)->int:
        """ Recebe o nome de um contato e, se ele existir no repositório,
            retorna seu indice; se não, retorna -1. """
        resultado = -1
        indice = -1
        for i in range(0, len(self.__repositorio_contatos)):
            contato = self.__repositorio_contatos[i]
            if contato.nome == nome:
                indice = i
        if indice != -1:
            resultado = indice
        return resultado

    def existe(self, contato: Contato)->bool:
        """ Recebe um objeto do tipo Contato e, caso haja algum contato com
            o mesmo telefone no repositório, retorna True;
            caso contrário, retorna False. """
        resultado = False
        for c in self.__repositorio_contatos:
            if c.fone == contato.fone:
                resultado = True
                break
        return resultado

    def vazio(self)->bool:
        """ Retorna um booleano, especificando se o repositorio esta vazio """
        return (len(self.__repositorio_contatos)==0)

class CadastroContatos:

    def __init__(self):
        self.__repositorio_contatos = RepositorioContatos()

    @property
    def repositorio_contatos(self)-> str:
        return self.__repositorio_contatos

    def incluir(self, contato: Contato)->Contato:
        """ Recebe um objeto do tipo Contato e, se ele não
            existir no repositório, insere-o e o devolve;
            caso contrário, exibe 'Contato ja cadastrado' e retorna None. """
        resultado = None
        if self.__repositorio_contatos.existe(contato):
            input('Contato ja cadastrado. Tecle enter...')
        else:
            resultado = self.__repositorio_contatos.incluir(contato)
        return resultado

    def alterar(self, contato: Contato)->Contato:
        """ Recebe um objeto do tipo Contato e, se houver
            houver um contato com o mesmo nome no repositorio, atualiza seu
            telefone; caso contrário, exibe 'Contato nao encontrado' e retorna
            None. """
        resultado = None
        if self.__repositorio_contatos.consultar_indice_por_nome(contato.nome) == -1:
            input('Contato nao encontrado. Tecle enter...')
        else:
            indice = self.__repositorio_contatos.consultar_indice_por_nome(contato.nome)
            resultado = self.__repositorio_contatos.atualizar(indice, contato)
        return resultado

    def excluir(self, contato: Contato)->Contato:
        """ Exclui um contato. Se não existir um contato com o número
            fornecido, exibe a mensagem 'Contato nao encontrado'. """
        resultado = None
        if not self.__repositorio_contatos.existe(contato):
            input('Contato nao encontrado. Tecle enter...')
        else:
            indice = self.__repositorio_contatos.consultar_indice_por_nome(contato.nome)
            if indice != -1:
                resultado = self.__repositorio_contatos.excluir_por_indice(indice)
        return resultado

    def consultar(self, nome: str)->Contato:
        """ Localiza um contato pelo nome. Se não existir um contato com
            o nome fornecido, exibe a mensagem 'Contato nao encontrado'. """
        resultado = None
        if not self.__repositorio_contatos.existe(nome):
            print('Contato nao encontrado.')
        else:
            indice = self.__repositorio_contatos.consultar_indice_por_nome(nome)
            if indice != -1:
                resultado = self.__repositorio_contatos.excluir_por_indice(indice)
        return resultado


class ContatosApp:

    def __init__(self):
        self.__regras_negocio = CadastroContatos()
        self.__loop_principal()
        
    def __exibe_menu(self)->None:
        """ Exibe o menu da aplicaçao """
        self.__limpar_tela()
        print('\n Selecione uma opçao: ')
        print('\n 1. Incluir novo contato')
        print('\n 2. Alterar telefone de um contato')
        print('\n 3. Excluir um contato')
        print('\n 4. Consultar contato por nome')
        print('\n 5. Listar todos os contatos cadastrados')
        print('\n 6. Sair')
        print('\n')

    def __limpar_tela(self)->None:
        print('\n' * 100)  # Limpar a tela
        
    def __opcao_selecionada(self)->int:
        opcao = input('Escolha uma opçao: ')
        if opcao == '':
            resultado = -1
        else:
            resultado = int(opcao)
        return resultado

    def __ler_dados_contato(self)->Contato:
       # self.__limpar_tela()
        fone = input('\nTelefone: ')
        nome = input('\nNome: ')
        resultado = Contato(fone, nome)
        return resultado
        
    def __loop_principal(self)->None:
        opcao = -1
        while opcao!=6:
            self.__exibe_menu()
            opcao = self.__opcao_selecionada()
            if opcao==1:
                contato = self.__ler_dados_contato()
                print(self.__regras_negocio.incluir(contato))
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

app = ContatosApp()