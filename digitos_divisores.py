# Codifica aquí tu programa
usuario = int(input("Introducir enteros: "))

divisor = 0

for valor in str(usuario):
    valor = int(valor)
    if valor != 0 and usuario % valor == 0:
        divisor += 1

print(divisor)
