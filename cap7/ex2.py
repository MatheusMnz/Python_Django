players = ['Matheus', 'Joao', 'Maria', 'Leticia', 'Afonsa', 'Thiago']
dict_time_lap = {}

for player in players:
    dict_time_lap[player] = []  # Inicializa uma lista vazia para cada jogador

for i in range(10):
    for player in players:
        time_lap = float(input(f"Insira o tempo gasto na volta {i+1} para {player}: "))
        dict_time_lap[player].append(time_lap)  # Adiciona o tempo à lista do piloto correspondente
        print(dict_time_lap)

# Encontrar o piloto com a melhor volta e o tempo da melhor volta
best_pilot = None
best_lap_time = float('inf')

for player, lap_times in dict_time_lap.items():
    min_lap_time = sum(lap_times)/10
    if min_lap_time < best_lap_time:
        best_pilot = player
        best_lap_time = min_lap_time

# Encontrar o número da volta em que o piloto obteve a melhor marca
best_lap_number = dict_time_lap[best_pilot].index(best_lap_time) + 1

print(f"O campeão é {best_pilot}, com o tempo de {best_lap_time:.2f} na volta {best_lap_number}.")