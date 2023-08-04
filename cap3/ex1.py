# Recebo a quantidade de valores
n = int(input("Digite a quantidade de valores: "))

# Recebo os valores
list_values = []
for i in range(n):
    value = int(input(f"Insira o valor {i + 1}: "))
    list_values.append(value)

# Calcula a média
media = sum(list_values) / n

# Calcula mediana
list_values.sort()
mediana = list_values[n//2] # Pegando a divisão inteira

# Exibindo dados
print(f'A média é {media:.2f} e a mediana é {mediana:.2f}')