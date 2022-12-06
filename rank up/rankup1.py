# Complete o método/função para que ele converta palavras delimitadas por traço/sublinhado em camel case.
# A primeira palavra na saída deve ser maiúscula apenas se a palavra original estiver em maiúscula 
# (conhecida como Upper Camel Case, também conhecida como Pascal case).

# Exemplos
# "the-stealth-warrior" se converte em "theStealthWarrior"
# "The_Stealth_Warrior" se converte em "TheStealthWarrior"

from string import punctuation
def to_camel_case(text):
    # Retorna uma string vazia se o argumento for uma string vazia
    if text == '':
        return text
    # O argumento passado nesse desafio nunca será uma string só de letras, então entrará nessa condicional.
    if not text.isalpha():
        # Esse loop é para substituir todas as pontuações por espaço
        for i in punctuation:
            if i in text:
                text = text.replace(i, " ")
        # Essa condicional checa se o primeiro indice é minusculo, se verdadeiro ela 'splita' a string e deixa
        # somente a primeira palavra em minuscula, enquanto o resto dela fica capitalizada,
        # e então 'joina' ela novamente e retorna
        if text[0].islower():
            list_text = text.split()
            text = list_text[0]
            return text + " ".join(list_text[1::1]).title().replace(" ", "")

        # Essa condicional checa se o argumento já está capitalizado,
        # se verdadeiro ela só remove os espaços e o retorna
        if text.istitle():
            return text.replace(" ", "")

        # Essa condicional checa se o primeiro indice do argumento está maiusculo,
        # se verdadeiro ela irá 'splitar' a string, deixará tudo capitalizado, 'joina' novamente
        # e a retorna sem espaços 
        if text[0].isupper():
            text = text.split()
            return " ".join(text[::1]).title().replace(" ", "")
    
    
print(to_camel_case('The-Pippi-was_pippi'))

# Resolução mais eficiente

# def to_camel_case(text):
#     return text[0] + text.title().translate(None, "-_")[1:] if text else text