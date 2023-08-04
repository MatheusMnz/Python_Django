count_numbers = 0
for i in range(1000, 9001):  # O intervalo vai de 1000 a 9000 (9001 é exclusivo)
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0:
        count_numbers += 1

print(f'Existem {count_numbers} números divisíveis por 4 e 3 que sejam pares no intervalo de 1000 a 9000.')
