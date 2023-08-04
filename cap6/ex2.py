import re

answer = str(input("Digite a resposta: ")).lower()
copy_ans = answer
correct_case = len(answer) * '*'
letras_corretas = []
lifes = 6

while lifes > 0:

    if copy_ans == correct_case:
        break

    char_selected = str(input("Digite uma letra: "))
    matches = [match.start() for match in re.finditer(char_selected, copy_ans, re.IGNORECASE)]

    # Verifico se está vazia
    if not matches:
        lifes -= 1
        continue
    else:
        if char_selected not in letras_corretas:
            letras_corretas.append(char_selected)
            for aux in matches:
                copy_ans = copy_ans.replace(char_selected,'*')
        else:
            continue

if copy_ans == correct_case:
    print(f"Você acertou, a palavra é: {answer}")
else:
    print(f"Você não acertou. A palavra era {answer}")
