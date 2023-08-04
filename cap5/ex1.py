from math import pow, sqrt

x, y, z = map(int, input("Digite as coordenadas x, y e z do ponto A: ").split())
point_a = (x, y, z)

x, y, z = map(int, input("Digite as coordenadas x, y e z do ponto B: ").split())
point_b = (x, y, z)

x, y, z = map(int, input("Digite as coordenadas x, y e z do ponto C: ").split())
point_c = (x, y, z)


print(x.key())
# Calculo lado A D(a, b)
dist_a = sqrt(pow(point_b[0] - point_a[0], 2) + pow(point_b[1] - point_a[1], 2) + pow(point_b[2] - point_a[2], 2))

# Calculo lado B D(b, c)
dist_b = sqrt(pow(point_c[0] - point_b[0], 2) + pow(point_c[1] - point_b[1], 2) + pow(point_c[2] - point_b[2], 2))

# Calculo lado C D(a, c)
dist_c = sqrt(pow(point_c[0] - point_a[0], 2) + pow(point_c[1] - point_a[1], 2) + pow(point_c[2] - point_a[2], 2))

# Verifico condição de existência de um triângulo
if dist_a < dist_b + dist_c and dist_b < dist_a + dist_c and dist_c < dist_a + dist_b:
    print("As coordenadas fornecidas formam um triângulo.")
else:
    print("As coordenadas fornecidas não formam um triângulo.")
