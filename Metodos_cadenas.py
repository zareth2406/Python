#Para que la primera letra se ponga mayus
cadena1 = "zareth"
print("capitalize ", cadena1.capitalize())
#Para que las mayus las ponga en minusculas
cadena2 = "SoS"
print("casefold", cadena2.casefold())
#Para centrar texto
print(cadena2.center(10,"*"))
cadena3 = ["Memo es gei", "Nathalia es lesbiana", "Luis es furro"]
for cadena3 in cadena3 :
    print(cadena3.center(30,"."))
#contar cuantas veces aparece un caracter en una cadena
cadena4 = "Memo es gei y se besa con Luis y Leif"
print(cadena4.count("e"))