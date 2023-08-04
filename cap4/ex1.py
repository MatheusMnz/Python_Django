nomes = ['', '', '', '', '']
notas = [0.0, 0.0, 0.0, 0.0, 0.0]

for cont in range(5):
    print(f'Entre com o nome do aluno {cont + 1}: ')
    nomes[cont] = input()
    print(f'Entre com a nota do aluno {nomes[cont]}: ')
    notas[cont] = float(input())

media = sum(notas) / 5
print(f'A media da turma é {media:.3f}')

# Ordena de forma decrescente
notas.sort(reverse=True)

# Printa em ordem decrescente
print(notas)