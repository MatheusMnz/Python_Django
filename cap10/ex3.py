file_path = '/home/matheus/work/python_django/cap10/dados_list.txt'

# Abrindo o arquivo no modo de leitura binária
with open(file_path, 'rb') as file:
    # Lendo todo o conteúdo do arquivo e decodificando em UTF-8
    file_content = file.read().decode('utf-8')

# Substituindo os bytes de quebra de linha (\n) pelo caractere de quebra de linha '\n' (Substituo os bytes '\n' pela string '\n' para visualização na saída)
file_content = file_content.replace('\n', '\n')

# Exibindo o conteúdo
print(file_content)
