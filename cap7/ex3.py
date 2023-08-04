import math

limite = int(input("Digite o valor limite: "))
raiz = math.isqrt(limite)  # Utilize math.isqrt() para encontrar a raiz inteira

# Criar uma lista de booleanos inicialmente definidos como True
bool_list = [True] * (limite + 1)
bool_list[0] = bool_list[1] = False  # 0 e 1 não são primos

for i in range(2, raiz + 1):  # Corrija o limite superior do range para incluir a raiz
    if bool_list[i]:
        for j in range(i+1, limite+1):  # Marque os múltiplos como False
            if j % i == 0: # Marco os multiplos do primo como Falsos
                bool_list[j] = False

# Exibir os números primos encontrados
print("Números primos até o limite:")
for m in range(limite + 1):
    if bool_list[m]:
        print(m)
