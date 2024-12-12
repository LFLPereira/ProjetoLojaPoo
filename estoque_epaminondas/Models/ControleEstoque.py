import locale
import sqlite3
from Controllers.utils import inputplus
from Controllers.utils import exibir_vetor

class ControleEstoque:
    def __init__(self, db):
        self.__conn = sqlite3.connect(db)
        self.__cursor = self.__conn.cursor()

    def criar_tabela(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS loja (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            qde INTEGER NOT NULL,
            preco REAL NOT NULL
            )
        '''
        )
    
    def adicionar_produto(self, nome_add, qde_add, preco_add):
        self.__cursor.execute('INSERT INTO loja (nome, qde, preco) VALUES (?, ?, ?)',(nome_add, qde_add, preco_add))
        self.__cursor.execute('SELECT * FROM loja')
        self.__conn.commit()
        lista_loja = self.__cursor.fetchall()
        exibir_vetor(lista_loja[len(lista_loja)-1])
        input("Pressione Enter para continuar. ")

    def listar_produto(self):
        self.__cursor.execute('SELECT * FROM loja')
        lista_loja = self.__cursor.fetchall()
        for i in lista_loja:
            exibir_vetor(i)
        self.__cursor.execute('SELECT qde*preco FROM loja')
        valor_total = 0
        valores_loja = self.__cursor.fetchall()
        for j in valores_loja:
            valor_total += j[0]
        print("Valor Total do estoque:",locale.currency(valor_total, grouping=True))
        input("Pressione Enter para continuar. ")

    def atualizar_produto(self, id_update, nome_update, qde_update, preco_update):
        self.__cursor.execute(f'SELECT * FROM loja WHERE id = {id_update}')
        lista_loja = self.__cursor.fetchall()
        if len(lista_loja) > 0:
            exibir_vetor(lista_loja[len(lista_loja)-1])
            self.__cursor.execute(f"UPDATE loja SET nome = '{nome_update}', qde = {qde_update}, preco = {preco_update} WHERE id = {id_update}")
            self.__conn.commit()
            self.__cursor.execute(f'SELECT * FROM loja WHERE id = {id_update}')
            lista_loja = self.__cursor.fetchall()
            exibir_vetor(lista_loja[len(lista_loja)-1])
            print("Atualizado com sucesso!")
            input("Pressione Enter para continuar. ")
        else:
            print("Produto não encontrado")
            input("Pressione Enter para continuar. ")

    def remover_produto(self, id_remove):
        self.__cursor.execute(f'SELECT * FROM loja WHERE id = {id_remove}')
        lista_loja = self.__cursor.fetchall()
        if len(lista_loja) > 0:
            self.__cursor.execute(f'DELETE FROM loja WHERE id = {id_remove}')
            self.__conn.commit()
            exibir_vetor(lista_loja[len(lista_loja)-1])
            print("Removido com sucesso!")
            input("Pressione Enter para continuar. ")
        else:
            print("Produto não encontrado")
            input("Pressione Enter para continuar. ")
    def buscar_produto(self, search):
        self.__cursor.execute(f'SELECT * FROM loja WHERE id = {search}')
        lista_loja = self.__cursor.fetchall()
        if len(lista_loja)>0:
            exibir_vetor(lista_loja[len(lista_loja)-1])
            input("Pressione Enter para continuar. ")
        else:
            print("Produto não encontrado")
            input("Pressione Enter para continuar. ")

    def vender_produto(self):
        id_nome = input("Procurar por ID? (S/N) ")

        if id_nome.lower() == "s":

            search = inputplus(False,"ID: ")
            self.__cursor.execute(f'SELECT * FROM loja WHERE id = {search}')
            lista_loja = self.__cursor.fetchall()
            if len(lista_loja)>0:
                exibir_vetor(lista_loja[len(lista_loja)-1])

        else:
            search = input("Nome: ")
            self.__cursor.execute(f"SELECT * FROM loja WHERE nome = '{search}'")
            lista_loja = self.__cursor.fetchall()
            
            if len(lista_loja)>0:
                vetor_nome = lista_loja[len(lista_loja)-1]
                exibir_vetor(vetor_nome)
                search = vetor_nome[0]         
            
        if len(lista_loja)>0:
            vetor_venda = lista_loja[len(lista_loja)-1]
            qde_vendida = inputplus(False, "Quantidade vendida: ")
            if qde_vendida <= vetor_venda[2]:
                qde_nova = vetor_venda[2] - qde_vendida
                valor_venda = qde_vendida*vetor_venda[3]
                self.__cursor.execute(f"UPDATE loja SET qde = {qde_nova} WHERE id = {search}")
                self.__conn.commit()
                print("Valor da venda:", locale.currency(valor_venda, grouping=True))
                self.__cursor.execute(f'SELECT * FROM loja WHERE id = {search}')
                lista_loja = self.__cursor.fetchall()
                exibir_vetor(lista_loja[len(lista_loja)-1])
                input("Pressione Enter para continuar. ")
            else:
                print("Quantidade não disponível!")
                input("Pressione Enter para continuar. ")


        else:
            print("Produto não encontrado")
            input("Pressione Enter para continuar. ")