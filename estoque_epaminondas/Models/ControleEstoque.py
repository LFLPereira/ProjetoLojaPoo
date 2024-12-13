from Models.Database import Database
from Controllers.utils import inputplus
from Controllers.utils import exibir_vetor

class ControleEstoque(Database):
    def __init__(self, bd):
        super().__init__(bd)
        self.__table = {
            'table':'Produto',
            'columns':{
                'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'Nome':'TEXT',
                'Quantidade':'INTEGER',
                'Preço': 'REAL'
            }
        }

        self.create_table(self.__table['table'],self.__table['columns'])

    def adicionar_produto(self, nome, qde, preco):
        prod = {
            'table': 'Produto',
            'values': {
                'Nome': nome,
                'Quantidade':qde,
                'Preço': preco
            }
        }

        return self.insert_values(prod['table'], prod['values'])
    
    def listar_produtos(self):
        return self.get_all('Produto')
