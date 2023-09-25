# Adicione 2 atributos e 2 métodos à classe Mago.

#obs: o exemplo utilizado em aula continha 4 atributos: Nome,Poder,Idade e EscolaMagia
# e 3 métodos: Andar(), Falar(), InvocarMagia()

class Mago:
  def __init__(self, nivel, manaMaxima):
    self.nivel = nivel
    self.manaMaxima = manaMaxima
    
  def upar_nivel(self):
    self.nivel = self.nivel + 1
    self.manaMaxima = self.manaMaxima + (self.nivel * 0.3)
    print(f'Parabéns! Agora você é nível {self.nivel}')

  def checar_nivel(self):
    print(f'Você está no nível {self.nivel}')

