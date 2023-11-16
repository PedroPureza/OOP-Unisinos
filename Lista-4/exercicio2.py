class Assinatura:
    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass

class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        return 29.99

    def exibir_detalhes(self):
        print("Assinatura Simples: Acesso a filmes e séries em qualidade padrão.")

class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print("Assinatura Premium: Acesso a filmes e séries em qualidade HD e Ultra HD.")

assinatura_simples = AssinaturaSimples()
assinatura_premium = AssinaturaPremium()

assinaturas = [assinatura_simples, assinatura_premium]

for assinatura in assinaturas:
    print(f"Tipo de Assinatura: {type(assinatura).__name__}")
    print(f"Preço: R$ {assinatura.calcular_preco()}")
    assinatura.exibir_detalhes()
    print()
