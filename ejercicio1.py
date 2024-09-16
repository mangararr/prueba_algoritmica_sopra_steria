numero = int(input("LEER NUMERO: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
    print("Pares descendentes:")
    for i in range(numero, -1, -2):
        print(i)
else:
    print(f"El número {numero} es impar.")
    print("Impares descendentes:")
    for i in range(numero, 0, -2):
        print(i)
