print("\n\n")
frase = input("Ingresa la oracion que quieras: ")
print("Lista de palabras: ", frase.split())
print("Palabras en mayus:")
frase = frase.upper()
for frase in frase.split():
    print(frase)