from Models.Produto import Produto
from Models.ControleEstoque import ControleEstoque
from Models.Polymorph import Polymorph
from Controllers.utils import clear
from Controllers.utils import exibir_vetor
from Controllers.utils import inputplus
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main():
    
    polymorph = False

    while True:
        clear()

        if polymorph:
            estoque = Polymorph('Banco/estoque.db')
        else:
            estoque = ControleEstoque('Banco/estoque.db')

        print(estoque.logo())
        

        print("Menu:")
        print("")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Remover Produto")
        print("5 - Buscar Produto")
        print("6 - Vender Produto")
        print("7 - Polimorfismo")
        print("0 - Fechar")
        print("")

        menu = input("Escolha a opção: ")
              
        match menu:
            case "1":
                nome = input('Nome: ')
                qde = inputplus(False, 'Quantidade: ') #int
                preco = inputplus(True, 'Preço: ') #float

                NewProduto = Produto()
                NewProduto.set_prod('', nome, qde, preco)

                if estoque.adicionar_produto(NewProduto.get_nome(), NewProduto.get_qde(), NewProduto.get_preco()):
                    print("Produto adicionado:", NewProduto.get_nome())
                    input("Aperte Enter para continuar.")
                else:
                    print('Erro ao adicionar produto')
                    input("Aperte Enter para continuar.")

            case "2":
                for i in estoque.listar_produtos():
                    exibir_vetor(i)
                input("Aperte Enter para continuar.")

            case "3":
                existe = False
                nome = ''
                nome_ou_id = input("Procurar por nome? (S/N) ")
                alterar_nome = input("Alterar nome? (S/N) ")

                if nome_ou_id.lower() == "s":
                    nome_og = input("Nome: ")
                    if estoque.nome_existe(nome_og):
                        existe = True
                        id = estoque.id_por_nome(nome_og)
                else:
                    id = input("ID: ")
                    if estoque.id_existe(id):
                        existe = True
                        nome_og = estoque.listar_por_id(id)[1]
                
                if existe:
                    exibir_vetor(estoque.listar_por_id(id))
                    if alterar_nome.lower() == 's':
                        nome = input('Novo Nome: ')
                    qde = inputplus(False, 'Nova quantidade: ') #int
                    preco = inputplus(True, 'Novo preço: ') #float

                    if alterar_nome.lower() != 's' or nome == nome_og:
                        alter_nome = False
                    else:
                        alter_nome = True

                    NewProduto = Produto()
                    NewProduto.set_prod(id, nome, qde, preco)
                    
                    if estoque.atualizar_produto(alter_nome, NewProduto.get_id(), NewProduto.get_nome(), NewProduto.get_qde(), NewProduto.get_preco()):
                        print("Produto atualizado:", NewProduto.get_nome())
                        input("Aperte Enter para continuar.")
                    else:
                        print('Erro ao atualizar produto')
                        input("Aperte Enter para continuar.")
                else:
                    print('Produto não existe.')
                    input("Aperte Enter para continuar.")

            case "4":
                existe = False
                nome = ''
                nome_ou_id = input("Procurar por nome? (S/N) ")

                if nome_ou_id.lower() == "s":
                    nome = input("Nome: ")
                    if estoque.nome_existe(nome):
                        existe = True
                        id = estoque.id_por_nome(nome)
                else:
                    id = input("ID: ")
                    if estoque.id_existe(id):
                        existe = True
                
                if existe:
                    exibir_vetor(estoque.listar_por_id(id))
                    confirmacao = input('Deseja realmente excluir o item? (S/N) ')
                    if confirmacao.lower() == 's':
                        NewProduto = Produto()
                        NewProduto.set_prod(estoque.listar_por_id(id)[0], estoque.listar_por_id(id)[1], estoque.listar_por_id(id)[2], estoque.listar_por_id(id)[3])

                        if estoque.excluir_produto(NewProduto.get_id()):
                            print("Produto excluido:", NewProduto.get_nome())
                            input("Aperte Enter para continuar.")
                        else:
                            print('Erro ao atualizar produto')
                            input("Aperte Enter para continuar.")
                    else:
                        input("Aperte Enter para continuar.")
                else:
                    print('Produto não existe.')
                    input("Aperte Enter para continuar.") 

            case "5":
                existe = False
                nome = ''
                nome_ou_id = input("Procurar por nome? (S/N) ")

                if nome_ou_id.lower() == "s":
                    nome = input("Nome: ")
                    if estoque.nome_existe(nome):
                        existe = True
                        id = estoque.id_por_nome(nome)
                else:
                    id = input("ID: ")
                    if estoque.id_existe(id):
                        existe = True
                
                if existe:
                    exibir_vetor(estoque.listar_por_id(id))
                    input("Aperte Enter para continuar.") 
                else:
                    print('Produto não existe.')
                    input("Aperte Enter para continuar.") 

            case "6":
                existe = False
                nome = ''
                nome_ou_id = input("Procurar por nome? (S/N) ")

                if nome_ou_id.lower() == "s":
                    nome = input("Nome: ")
                    if estoque.nome_existe(nome):
                        existe = True
                        id = estoque.id_por_nome(nome)
                else:
                    id = input("ID: ")
                    if estoque.id_existe(id):
                        existe = True
                
                if existe:
                    exibir_vetor(estoque.listar_por_id(id))

                    qde_vendida = inputplus(False, 'Quantidade vendida: ')

                    if qde_vendida <= estoque.listar_por_id(id)[2]:
                        nova_qde = estoque.listar_por_id(id)[2] - qde_vendida
                        venda = qde_vendida * estoque.listar_por_id(id)[3]

                        NewProduto = Produto()
                        NewProduto.set_prod(estoque.listar_por_id(id)[0], estoque.listar_por_id(id)[1], nova_qde, estoque.listar_por_id(id)[3])

                        if estoque.atualizar_produto(False, NewProduto.get_id(), NewProduto.get_nome(), NewProduto.get_qde(), NewProduto.get_preco()):
                            print("Produto vendido:", NewProduto.get_nome())
                            print("Valor da venda:", locale.currency(venda, grouping=True))
                            input("Aperte Enter para continuar.")
                        else:
                            print('Erro ao vender produto')
                            input("Aperte Enter para continuar.")
                    else:
                        print(qde_vendida)
                        print(estoque.listar_por_id(id)[2])
                        print("Não há estoque suficiente")
                        input("Aperte Enter para continuar.")
                else:
                    print('Produto não existe.')
                    input("Aperte Enter para continuar.") 
            
            case "7":
                if polymorph:
                    polymorph = False
                else:
                    polymorph = True
            
            case "0":
                break

            case _:
                pass

if __name__ == "__main__":
    main()