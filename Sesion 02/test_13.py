"""
Requisitos:
- Solicitar al usuario 4 números por consola
- Crear una función que devuelva cuál es el mayor número de los 4 ingresado por el usuario
- Finalmente elevar al cubo este resultado
"""
def mayor(a, b, c, d):
    # Encuentra el mayor número de los cuatro
    n_mayor = max(a, b, c, d)
    # Eleva el mayor número al cubo
    return n_mayor ** 3

# Solicitar los cuatro números al usuario
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
d = int(input("Ingresa el cuarto número: "))

# Llamar a la función y mostrar el resultado
resultado = mayor(a, b, c, d)
print(f"El mayor número elevado al cubo es: {resultado}")


