alunos = ['alice', 'bob', 'carl', 'daniel']
notas = [9.5, 8.0, 9.5, 8.0]

# Primeiro sempre recebe o índice e o segundo recebe o conteúdo da coleção
for indice, aluno in enumerate(alunos):
    print(f'Nome: {aluno} \t- Nota: {notas[indice]}')