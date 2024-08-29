class BombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):

        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):

        litros = valor / self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print(f"Você abasteceu {litros:.2f} litros.")
            return litros
        else:
            print(f"Quantidade de combustível insuficiente na bomba. Restante: {self.quantidadeCombustivel:.2f} litros.")
            return 0

    def abastecerPorLitro(self, litros):

        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            valor = litros * self.valorLitro
            print(f"Valor a ser pago: R$ {valor:.2f}")
            return valor
        else:
            print(f"Quantidade de combustível insuficiente na bomba. Restante: {self.quantidadeCombustivel:.2f} litros.")
            return 0

    def alterarValor(self, novoValor):

        self.valorLitro = novoValor
        print(f"Valor do litro atualizado para R$ {novoValor:.2f}.")

    def alterarCombustivel(self, novoTipo):

        self.tipoCombustivel = novoTipo
        print(f"Tipo de combustível atualizado para {novoTipo}.")

    def alterarQuantidadeCombustivel(self, novaQuantidade):

        self.quantidadeCombustivel = novaQuantidade
        print(f"Quantidade de combustível atualizada para {novaQuantidade:.2f} litros.")

# Criando uma bomba de combustível
bomba = BombaCombustivel("Gasolina", 5.50, 1000)

# Exemplos de uso
bomba.abastecerPorValor(50)
bomba.abastecerPorLitro(20)
bomba.alterarValor(5.75)
bomba.alterarCombustivel("Diesel")
bomba.alterarQuantidadeCombustivel(800)
