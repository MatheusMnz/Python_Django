list_numbers = []

for i in range (1,6):
    user_number = int(input("Digite um número: "))
    list_numbers.append(user_number)

# Printa de forma reversa
print(list_numbers[::-1])