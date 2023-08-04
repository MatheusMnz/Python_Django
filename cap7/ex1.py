# Criar pilha -> usar listas

#Declarando a pilha
stack = []

while(True):
        
    #Input do usuario
    identificador = int(input("Escolha o processo: (1) inserir, (2) remover, (3) sair: "))

    if identificador == 1:
        descricao = str(input("Digite a descrição do processo: "))
        id_code = int(input("Digite o código do processo: "))
        stack.append({descricao:id_code})
        print(f"Estado atual da stack: {stack}")
    elif identificador == 2:
        # Verifico se a lista não está vazia
        if stack: 
            stack.pop()
            print(f"Estado atual da stack: {stack}")
        else:
            print("Stack não está preenchida")
    elif identificador == 3:
        break
