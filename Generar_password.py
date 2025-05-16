import string
import random

def gen_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(char) for i in range(length))

    if (any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)):
        return password
    else:
        return gen_password(length)

length = 20
password = gen_password(length)
print("La contraseña segura es: " + password)
