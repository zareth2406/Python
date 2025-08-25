#Pràctica 1

inten = 3
saldoact = 1000
pin = 4321

def Menu():
    return int(input("BIENVENIDO AL MENU DE SU BANCA\nMENU:\n1.Consultar saldo\n2.Retirar dinero\n3.Depositar dinero\n4.Salir\n"))

def Consultacuenta(saldoact):
    print("Su saldo actual es de: $" + str(saldoact))

def Retirarmoni(saldoact):
    retiro = int(input("Ingrese la cantidad a retirar: $"))
    if retiro > saldoact:
        print("FONDOS INSUFICIENTES")
    else:
        saldoact -= retiro
        print("  Retiro exitoso. Su nuevo saldo es de: $" + str(saldoact))
    return saldoact

def Depositarmoni(saldoact):
    deposito = int(input("Ingrese la cantidad a depositar: $"))
    saldoact += deposito
    print("  Depósito exitoso. Su nuevo saldo es de: $" + str(saldoact))
    return saldoact

while inten > 0:
    pininten = int(input("BIENVENIDO AL CAJERO\nIngrese el PIN:\n"))
    if pininten == pin:
        while True:
            opcc = Menu()
            if opcc == 1:
                Consultacuenta(saldoact)
            elif opcc == 2:
                saldoact = Retirarmoni(saldoact)
            elif opcc == 3:
                saldoact = Depositarmoni(saldoact)
            elif opcc == 4:
                print("Gracias por usar el cajero.")
                break
            else:
                print("Opción inválida.")
        break
    else:
        inten -= 1
        if inten > 0:
            print("PIN incorrecto, le quedan", inten, "intentos antes de que se bloquee su cuenta")
        else:
            print("Llamando a la policia y bloqueando cuenta...")
