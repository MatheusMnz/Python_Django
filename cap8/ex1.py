from datetime import datetime

birthdate = str(input("Insira sua data de nascimento: (dd/mm/yyyy)"))
cont_jobs = int(input("Quantos empregos você já teve? "))

# Lista vazia que vai armazenar os valores em cada emprego
days_worked = []

for i in range(cont_jobs):
    in_date = str(input("Insira a data de admissão: (dd/mm/yyyy)"))
    out_date = str(input("Insira a data de rescisão: (dd/mm/yyyy)"))
    in_parser_date = datetime.strptime(in_date, '%d/%m/%Y')
    out_parser_date = datetime.strptime(out_date, '%d/%m/%Y')
    dif_date = out_parser_date - in_parser_date
    days_worked.append(dif_date.days)  # Append the number of days as an integer

print(f'Você trabalhou {sum(days_worked)} dias atualmente')
