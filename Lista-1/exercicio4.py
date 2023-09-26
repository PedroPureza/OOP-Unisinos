# 4. Adapte o exercício de revisão (mini-spotify), proponto uma classe Musica. Quais seriam seus
# atributos? Quais seriam alguns dos seus possíveis métodos? Como poderíamos representar uma
# playlist?

class Musica:
  def __init__(self, id, nome, genero, ano, duracao, artista):
    self.id = id
    self.nome = nome
    self.genero = genero
    self.ano = ano
    self.duracao = duracao
    self.artista = artista

  def __str__(self):
    return f'{self.id},{self.nome},{self.genero},{self.ano},{self.duracao},{self.artista}'
  
class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def remover_musica(self, musica):
        self.musicas.remove(musica)

    def listar_musicas(self):
        for musica in self.musicas:
            print(musica)

# Exemplo de uso:
minha_playlist = Playlist("Minha Playlist")
thunderstruck = Musica(1, 'Thunderstruck', 'Rock', 1990, 300, 'AC/DC')
minha_playlist.adicionar_musica(thunderstruck)
minha_playlist.listar_musicas()