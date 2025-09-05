tupla = (12, "Sabritas", False) #sin empaquetar
tupla2 = 15, "Refresco", True #empaquetado
tupla3 = (1,5,9,0) #sin empaquetar
#se elimina con "del"
mintupla3 = (min(tupla3)) #imprime el numero menor en la tupla
print("min: ", mintupla3)
maxtupla3 = (max(tupla3)) #imprime el numero mayor en la tupla
print("max: ", maxtupla3)
sumtupla3 = (sum(tupla3)) #suma los elementos en la tupla
print("sum: ", sumtupla3)
print("in: ", 10 in tupla3) #busca el elemento "10" en la tupla, si lo encuentra true, si no false 
k = 0
while k<len(tupla) :
    print(tupla[k])
    k += 1

for t in tupla :
    print(t)

