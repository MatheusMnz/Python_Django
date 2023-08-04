cotacao_dolar = float(input("Insira a cotação atual do dólar: "))
valor_reais = float(input("Insira o valor em reais: "))

print(f'R${valor_reais:.2f} corresponde a ${valor_reais/cotacao_dolar:.2f} dólares')