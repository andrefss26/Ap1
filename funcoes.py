def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    return "Acima do peso"


def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor


def calcular_frete(peso):
    if peso <= 5:
        return 10.0
    if peso <= 10:
        return 20.0
    return 35.0


def senha_valida(senha):
    if len(senha) < 8:
        return False
    return any(c.isdigit() for c in senha)


def aplicar_desconto(valor, desconto):
    if desconto < 0 or desconto > 100:
        raise ValueError("Desconto inválido")
    return valor - (valor * desconto / 100)


def calcular_media(notas):
    if not notas:
        raise ValueError("Lista de notas vazia")
    return sum(notas) / len(notas)


def main():
    print(classificar_imc(20.0))
    print(sacar(100, 40))
    print(calcular_frete(8))
    print(senha_valida("senha123"))
    print(aplicar_desconto(100, 20))
    print(calcular_media([8, 9, 10]))