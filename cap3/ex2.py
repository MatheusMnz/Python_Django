def is_triangular():
    sides_values = []
    for i in range(3):
        sides_values.append(int(input(f"Insira o {i + 1}º valor: ")))

    sides_values.sort()
    hip = sides_values[-1]  # Pega o último elemento

    return True if hip ** 2 == sides_values[0] ** 2 + sides_values[1] ** 2 else False

if is_triangular():
    print("É um triângulo retângulo!")
else:
    print("Não é um triângulo retângulo.")
