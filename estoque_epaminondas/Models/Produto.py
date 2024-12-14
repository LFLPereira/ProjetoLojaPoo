class Produto:
    def __init__(self):
        self.__id = ''
        self.__nome = ''
        self.__qde = ''
        self.__preco = ''

    def set_prod(self, id, nome, qde, preco):
        self.__id = id
        self.__nome = nome
        self.__qde = qde
        self.__preco = preco

    def get_nome(self):
        return self.__nome
    
    def get_qde(self):
        return self.__qde
    
    def get_preco(self):
        return self.__preco
    
    def get_id(self):
        return self.__id
        