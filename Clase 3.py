calf = int(input("Captura calificacion: "))

def calcularcalificacion(calf) :
    if calf == 10 :
        print("Alumno excelente")

    if calf >= 6 :
        print("Aprobado con la calificacion de " ,calf)

    if calf < 6 :
        print("Que wey, no pasaste")

    if calf == 0 :
        print("Alumno de baja")

    if calf <100 :
        print("fin")

calcularcalificacion(calf)