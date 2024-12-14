from Models.Database import Database
from Controllers.utils import inputplus
from Controllers.utils import exibir_vetor

class ControleEstoque(Database):
    def __init__(self, bd):
        super().__init__(bd)
        self.__table = {
            'table':'Produtos',
            'columns':{
                'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'Nome':'TEXT',
                'Quantidade':'INTEGER',
                'Preço': 'REAL',
            }
        }

        self.create_table(self.__table['table'],self.__table['columns'])

    def adicionar_produto(self, nome, qde, preco):
        prod = {
            'table': 'Produtos',
            'values': {
                'Nome': nome,
                'Quantidade':qde,
                'Preço': preco
            }
        }
        if self.get_value_name(prod['table'], nome) == []:
            return self.insert_values(prod['table'], prod['values'])
        else:
            return False
    
    def listar_produtos(self):
        return self.get_all('Produtos')
    
    def listar_por_id(self, id):
        return self.get_value_id('Produtos', id)[0]
    
    def id_por_nome(self, nome):
        if self.get_value_name('Produtos', nome) != []:
            return self.get_value_name('Produtos', nome)[0][0]
        else:
            return 0
        
    def id_existe(self, id):
        if self.get_value_id('Produtos', id) != []:
            return True
        else:
            return False
    
    
    def atualizar_produto(self, alter_nome, id, nome, qde, preco):
        
        if alter_nome:
            prod = {
                'table': 'Produtos',
                'values': {
                    'Nome': nome,
                    'Quantidade':qde,
                    'Preço': preco
                },
                'conditions':{
                    'where':f'ID = {id}'
                }
            }
            if self.get_value_name(prod['table'], nome) == [] and id != 0:
                return self.update_values(prod['table'], prod['values'], prod['conditions'])
            else:
                return False
        else:
            prod = {
                'table': 'Produtos',
                'values': {
                    'Quantidade':qde,
                    'Preço': preco
                },
                'conditions':{
                    'where':f'ID = {id}'
                }
            }
                        
            if id != 0:
                return self.update_values(prod['table'], prod['values'], prod['conditions'])
            else:
                return False