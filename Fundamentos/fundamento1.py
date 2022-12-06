# Muito simples, dado um inteiro ou um número de ponto flutuante, encontre seu oposto.
# Exemplos:
# 1: -1
# 14: -14
# -34: 34
while True:
    numero = input("Insira o numero: ")

    def opposite(number):
        if '.' in number:
            if '-' in str(number):
                number = str(number)
                number = number[1:]
                return float(number)

            elif not '-' in str(number):
                number = str(number)
                number = '-' + number
                return float(number)

        elif not '.' in number:
            if '-' in str(number):
                number = str(number)
                number = number[1:]
                return int(number)

            elif not '-' in str(number):
                number = str(number)
                number = '-' + number
                return int(number)

    print(opposite(numero))

# Resolução mais eficiente

# def opposite(number):
#     return number * -1

        


# print(opposite(-4.67674))
    