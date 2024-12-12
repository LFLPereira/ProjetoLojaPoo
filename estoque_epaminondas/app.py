from Controllers.utils import clear
from Controllers.utils import inputplus

def main():
    while True:
        clear()
        print('''
        
        
        ''')
        print('''\u001b[31m▓█████  ██▓███   ▄▄▄       ███▄ ▄███▓ ██▓ ███▄    █  ▒█████   ███▄    █ ▓█████▄  ▄▄▄        ██████      ██████ ▄▄▄█████▓ ▒█████   ██▀███  ▓█████ 
▓█   ▀ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▒████▄    ▒██    ▒    ▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓█   ▀ 
▒███   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒░██   █▌▒██  ▀█▄  ░ ▓██▄      ░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▒███   
▒▓█  ▄ ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌░██▄▄▄▄██   ▒   ██▒     ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ▒▓█  ▄ 
░▒████▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒░██░▒██░   ▓██░░ ████▓▒░▒██░   ▓██░░▒████▓  ▓█   ▓██▒▒██████▒▒   ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒░▒████▒
░░ ▒░ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░
 ░ ░  ░░▒ ░       ▒   ▒▒ ░░  ░      ░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░▒  ░ ░   ░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░
   ░   ░░         ░   ▒   ░      ░    ▒ ░   ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░  ░ ░  ░   ░   ▒   ░  ░  ░     ░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░    ░   
   ░  ░               ░  ░       ░    ░           ░     ░ ░           ░    ░          ░  ░      ░           ░               ░ ░     ░        ░  ░
                                                                         ░                                                                       \u001b[0m''')
        
        print('''
        
        
        ''')
        print("Menu:")
        print("")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Remover Produto")
        print("5 - Buscar Produto")
        print("6 - Vender Produto")
        print("0 - Fechar")
        print("")

        menu = input("Escolha a opção: ")
        match menu:
            case "1":
                nome_add = input("Nome: ")
                qde_add = inputplus(False,"Quantidade: ")
                preco_add = inputplus(True,"Preço: ")

            case "2":
                pass

            case "3":
                id_update = inputplus(False,"ID: ")
                nome_update = input("Novo nome: ")
                qde_update = inputplus(False,"Nova quantidade: ")
                preco_update = inputplus(True,"Novo preço: ")

            case "4":
                id_remove = inputplus(False,"ID: ")

            case "5":
                id_nome = input("Procurar por ID? (S/N) ")
                if id_nome.lower() == "s":
                    search = inputplus(False,"ID: ")
                else:
                    search = input("Nome: ")

            case "6":
                pass

            case "0":
                break

            case _:
                pass

if __name__ == "__main__":
    main()