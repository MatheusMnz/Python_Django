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

# Exibindo 100 números:
for i in range(100):
    print(data_list[i])

# Abrindo um arquivo de forma binária onde irei inserir essa lista
file_to_write = open('/home/matheus/work/python_django/cap10/dados_list.txt', 'w+')

# Escrevendo a lista ordenada no arquivo
for item in data_list:
    # Convertendo o número inteiro de volta para string antes de escrever no arquivo
    file_to_write.write(str(item) + '\n')

# Fechando o arquivo após a escrita
file_to_write.close()
