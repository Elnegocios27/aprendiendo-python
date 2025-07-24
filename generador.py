import string
import random

print("/////creador de contraseñas/////")
largo = int(input("ingrese una cantidad de caracteres:"))
caracteres = string.digits + string.ascii_letters
contraseña = ''.join(random.choice(caracteres) for _ in range(largo))
print("contraseña: ", contraseña)
