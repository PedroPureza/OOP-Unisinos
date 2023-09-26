# 3. Crie uma classe Data, com os seguintes atributos: dia, mês e ano. Além do construtor padrão, a
# classe deverá ter um construtor personalizado que recebe dia, mês e ano por parâmetro. Essa classe
# deve ter também dois métodos: imprimirData, que não recebe parâmetro, e
# imprimirDataPorExtenso, que recebe o nome de uma cidade por parâmetro. Ambos os métodos
# não retornam dados.

class Data:
  def __init__(self, dia, mes, ano):
    self.dia = dia
    self.mes = mes
    self.ano = ano
  
  def imprimirData(self):
    print({self.dia}/{self.mes}/{self.ano})
  
  def imprimirDataPorExtenso(self, cidade):
    print(f'Hoje é {self.dia}/{self.mes}/{self.ano} em {cidade}')
  



