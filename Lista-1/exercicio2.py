# Instancie 3 objetos da classe mago e invoque seus métodos

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

mago = Mago(2, 120)
mago.checar_nivel()
mago.upar_nivel()
mago.checar_nivel()

mago2 = Mago(11, 120)
mago2.checar_nivel()
mago2.upar_nivel()
mago2.checar_nivel()

mago3 = Mago(5, 120)
mago3.checar_nivel()
mago3.upar_nivel()
mago3.checar_nivel()