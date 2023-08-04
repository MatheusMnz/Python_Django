from datetime import datetime

gender = str(input("Insira o seu gênero: (male/female): "))
birthdate = str(input("Insira a sua data de nascimento: "))
parser_birthdate = datetime.strptime(birthdate, '%d/%m/%Y')
count_jobs = int(input("Atuou em quantos empregos? "))

# Lista com a quantidade de anos trabalhados
years_worked = []

for i in range(count_jobs):
    in_date = str(input("Insira a data de admissão (dd/mm/yyyy): "))
    out_date = str(input("Insira a data de rescisão (dd/mm/yyyy): "))
    in_parser_date = datetime.strptime(in_date, '%d/%m/%Y')
    out_parser_date = datetime.strptime(out_date, '%d/%m/%Y')
    years_worked.append((out_parser_date.date() - in_parser_date.date()).days // 365)

match gender:
    case "male":
        if sum(years_worked) >= 35 and ((datetime.date.today() - parser_birthdate.date()).days // 365 >= 65):
            print("Já pode se aposentar!")
        elif sum(years_worked) >= 35 and ((datetime.date.today() - parser_birthdate.date()).days // 365 < 65):
            print("Você possui a contribuição necessária, entretanto, não tem a idade suficiente!")
        else:
            print(f"Faltam {35 - sum(years_worked)} anos de contribuição")
    case "female":
        if sum(years_worked) >= 32 and ((datetime.date.today() - parser_birthdate.date()).days // 365 >= 62):
            print("Já pode se aposentar!")
        elif sum(years_worked) >= 32 and ((datetime.date.today() - parser_birthdate.date()).days // 365 < 62):
            print("Você possui a contribuição necessária, entretanto, não tem a idade suficiente!")
        else:
            print(f"Faltam {35 - sum(years_worked)} anos de contribuição")
    case _:
        print("Gênero não identificado.")
