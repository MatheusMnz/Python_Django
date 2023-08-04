import random

player_1 = str(input('Digite seu nome: '))
player_2 = str(input('Digite seu nome: '))

# Gerando o valor dos dados
number_player1 = random.choice(range(1,7))
number_player2 = random.choice(range(1,7))

infos_player1 = {'Nome': player_1, 'Número': number_player1}
infos_player2 = {'Nome': player_2, 'Número': number_player2}

if infos_player1['Número'] > infos_player2['Número']:
    print(f'{infos_player1["Nome"]} venceu!')
else:
    print(f'{infos_player2["Nome"]} venceu!')