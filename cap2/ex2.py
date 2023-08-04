largura = float(input("Insira o valor da largura da sala: "))
comprimento = float(input("Insira o valor do comprimento da sala: "))
tamanho_aresta = float(input("Insira o tamanho da aresta em cm: "))
preco_m = float(input("Insira o preço do m^2 da cerâmica: "))

area_sala = largura * comprimento
quantidade_ceramica = area_sala / (tamanho_aresta / 100) ** 2 # convertido pra m2
custo = quantidade_ceramica * preco_m

print(f'Será necessário {quantidade_ceramica * (tamanho_aresta / 100) ** 2:.2f} m^2 de cerãmica e o custo total será de {custo:.2f} reais')