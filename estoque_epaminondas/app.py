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
                NewProduto.set_prod('', nome, qde, preco)

                if estoque.adicionar_produto(NewProduto.get_nome(), NewProduto.get_qde(), NewProduto.get_preco()):
                    print("Produto adicionado", NewProduto.get_nome())
                    input("Aperte Enter para continuar.")
                else:
                    print('Erro ao adicionar produto')
                    input("Aperte Enter para continuar.")

            case "2":
                for i in estoque.listar_produtos():
                    exibir_vetor(i)
                input("Aperte Enter para continuar.")

            case "3":
                nome = ''
                nome_ou_id = input("Procurar por nome? (S/N) ")
                alterar_nome = input("Alterar nome? (S/N) ")
                if nome_ou_id.lower() == "s":
                    nome_og = input("Nome: ")
                    id = estoque.id_por_nome(nome_og)
                    exibir_vetor(estoque.listar_por_id(id))
                    if alterar_nome.lower() == 's':
                        nome = input('Novo Nome: ')
                else:
                    id = input("ID: ")
                    if estoque.id_existe(id):
                        exibir_vetor(estoque.listar_por_id(id))
                        nome_og = estoque.listar_por_id(id)[1]
                    else:
                        id = 0
                    if alterar_nome.lower() == 's':
                        nome = input("Nome: ")
                qde = input('Quantidade: ')
                preco = input('Preço: ')

                if alterar_nome.lower() != 's' or nome == nome_og:
                    alter_nome = False
                else:
                    alter_nome = True

                NewProduto = Produto()
                NewProduto.set_prod(id, nome, qde, preco)
                
                if estoque.atualizar_produto(alter_nome, NewProduto.get_id(), NewProduto.get_nome(), NewProduto.get_qde(), NewProduto.get_preco()):
                    print("Produto atualizado", NewProduto.get_nome())
                    input("Aperte Enter para continuar.")
                else:
                    print('Erro ao atualizar produto')
                    input("Aperte Enter para continuar.")


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