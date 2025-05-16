import random


def gen_pass(phrase):
    phrase = phrase.replace(" ", "")
    char_replace = {

        'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': 'U',

        'A': '4', 'E': '3', 'I': '1', 'O': '0', 'U': 'U'

    }
    password = ''.join(char_replace.get(char, char) for char in phrase)
    symbols = "!#$%&*"
    password = random.choice(symbols) + password + \
        random.choice(symbols) + str(random.randint(10, 99))
    return password


sentence = input("Ingrese una frase para mejorar como contraseña: ")
password = gen_pass(sentence)
print("La contraseña generada es:", password)
