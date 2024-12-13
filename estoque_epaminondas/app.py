from Models.Produto import Produto
from Models.ControleEstoque import ControleEstoque
from Controllers.utils import clear
from Controllers.utils import exibir_vetor
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
        
        estoque = ControleEstoque('Banco/estoque.db')
        
        match menu:
            case "1":
                nome = input('Nome: ')
                qde = input('Quantidade: ')
                preco = input('Preço: ')

                NewProduto = Produto()
                NewProduto.set_prod(nome, qde, preco)

                if estoque.adicionar_produto(NewProduto.get_nome(), NewProduto.get_qde(), NewProduto.get_preco()):
                    print("Produto adicionado", NewProduto.get_nome())
                else:
                    print('Erro ao adicionar produto')

            case "2":
                for i in estoque.listar_produtos():
                    exibir_vetor(i)
                input("Aperte Enter para continuar.")

            case "3":
                pass

            case "4":
                pass

            case "5":
                pass

            case "6":
                pass

            case "0":
                break

            case _:
                pass

if __name__ == "__main__":
    main()