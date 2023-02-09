import random

hola = "12345678"

all = hola
ancho_contraseña = 8
contraseña = "".join(random.sample(all, ancho_contraseña))
print("tu contraseña es" + contraseña)