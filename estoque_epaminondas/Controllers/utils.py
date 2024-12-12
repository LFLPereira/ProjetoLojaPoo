import locale
import os

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def inputplus(int_or_float,string_question):
    inplus = -1
    while inplus < 0:
        inp = input(string_question)
        try:
            if int_or_float == True:
                if float(inp) >= 0:
                    inplus = float(inp)
                    return inplus
                else:
                    print("Valor invalido!")
            else:
                if int(inp) >= 0:
                    inplus = int(inp)
                    return inplus
                else:
                    print("Valor invalido!")
        except ValueError:
            print("Valor invalido!")

def exibir_vetor(vetor):

    print("ID:", vetor[0],"- Descrição:", vetor[1],"- Quantidade:", vetor[2], "- Valor:", locale.currency(vetor[3], grouping=True))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')