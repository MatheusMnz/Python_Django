import re

# Regras:
'''
Inicia com letra maiscula
tem no minimo seis caracteres
pelo menos 2 caracteres númericos
pelo menos 3 letras
tamanho de até 10
'''

def validar_string(s):
    regex = r'^(?=.*[A-Z])(?=.*\d.*\d)(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z]).{6,}$'
    return bool(re.match(regex, s))


logins_list = []
choice = 'sim'


while choice == 'sim':
    login = input("Insira um login: ")
    if validar_string(login):
        print("Login Válido")
        choice = input("Deseja inserir outro usuário? (sim) ou (nao)")
        logins_list.append(login)
        if choice == 'sim':
            continue
        else:
            break
    else:
        print("Login inválido")
        choice = input("Deseja inserir outro usuário? (sim) ou (nao)")

# Verifico se a lista está vazia
if not logins_list:
    print("A lista está vazia.")
else:
    logins_string = '#'.join(logins_list)
    split_list = logins_string.split('#')
    print(split_list)