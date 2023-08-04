largura = float(input("Insira o valor da largura da sala: "))
comprimento = float(input("Insira o valor do comprimento da sala: "))
tamanho_aresta = float(input("Insira o tamanho da aresta em cm: "))


area_sala = largura * comprimento
quantidade_ceramica = int(area_sala // (tamanho_aresta / 100) ** 2)# convertido pra m2


print(f'Será necessário {quantidade_ceramica} unidades de cerâmica')