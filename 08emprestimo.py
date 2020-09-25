class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Lending:
    def __init__(self, id, cliente, produto):
        self.id = id
        self.cliente = cliente
        self.produto = produto

class produto:
    def __init__(self, id, tipo):
        self.id = id
        self.descricao = tipo

produto01 = produto(1,'Furadeira')
produto02 = produto(2,'Serrote')
produto03 = produto(3,'Marreta')
produto04 = produto(4,'Talhadeira')
cliente01 = Cliente(1, 'Guilherme')
cliente02 = Cliente(2, 'Rafael')

Lending = Lending(1, cliente01, [produto02, produto04])

print(f'Foi emprestado o produto com codigo {lending.id} que esta com {lending.cliente.name} '
      f' \n ele emprestou: {lending.equipamento[0].descricao} e {lending.equipamento[1].descricao} ')