class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
# criando o próprio metododo
    

    def __str__(self):
      return f'{self.nome} | {self.categoria}'
# o metodo __str__ mostra o objeto em formato de texto

    def listar_restaurantes():
         for restaurante in Restaurante.restaurantes:
             print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('praça' , 'Gourmet')
restaurante_pizza = Restaurante('pizza', 'italiana')

Restaurante.listar_restaurantes()