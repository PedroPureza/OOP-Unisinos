# 1. Faça um programa que simule um "dado virtual". O dado deve ser modelado como uma classe,
# possuindo apenas o número de faces e o método Rolar, que retorna o valor sorteado. O número
# de faces deve ser definido na criação do objeto (construtor com parâmetro). Deve ser instanciado
# um dado com 6, 8 e 12 faces no main(). Cada dado deve ser jogado 3 vezes e o resultado de cada
# jogada deve ser impresso na tela. Não deve ser usado print dentro da classe.
import random

class Dado:
  def __init__(self, numeroDeFaces):
    self.numeroDeFaces = numeroDeFaces

  def rolar_dado(self):
    return random.randint(1, self.numeroDeFaces)


dado6 = Dado(6)

print('Dado 6:', dado6.rolar_dado())
print('Dado 6:', dado6.rolar_dado())
print('Dado 6:', dado6.rolar_dado())

dado8 = Dado(8)
print('Dado 8:', dado8.rolar_dado())
print('Dado 8:', dado8.rolar_dado())
print('Dado 8:', dado8.rolar_dado())

dado12 = Dado(12)
print('Dado 12:', dado12.rolar_dado())
print('Dado 12:', dado12.rolar_dado())
print('Dado 12:', dado12.rolar_dado())