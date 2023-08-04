import os

file = open('/home/matheus/work/python_django/cap10/dados.txt', 'r+')
data_list = []

# Leio e armazeno os dados em uma lista
while True:
    line = file.readline()
    if line != '':
        # Convertendo a linha para um número inteiro (caso os números sejam inteiros)
        number = int(line.strip())
        data_list.append(number)
    else:
        break

# Fechando o arquivo após a leitura
file.close()

# Ordenando a lista
data_list.sort()