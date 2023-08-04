import random

number_user = int(input("Escolha um número inteiro de 0 a 100: "))

# verifico se é um número válido
while number_user < 0 or number_user > 100:
    number_user = int(input("Escolha um número inteiro de 0 a 100: "))

banca_number = random.randrange(1, 101)

if number_user == banca_number:
    print("Você venceu!")
    print
else:
    print("A banca sempre vence!")