class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title() #iniciais com letra maiúscula
        self.categoria = categoria.upper()# todas as letras maiúscula
        self._ativo = False
        Restaurante.restaurantes.append(self)
# criando o próprio metododo
    
    def __str__(self):
      return f'{self.nome} | {self.categoria}'
# o metodo __str__ mostra o objeto em formato de texto

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
# modifica como o atributo vai ser lido.

restaurante_praca = Restaurante('praça' , 'Gourmet')                    
restaurante_pizza = Restaurante('pizza', 'italiana')

Restaurante.listar_restaurantes()