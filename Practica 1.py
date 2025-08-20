#Pràctica 1
intent=3
while intent > 0:
    pin=int(input("BIENVENIDO AL CAJERO\n Ingrese el PIN:\n"))
    if pin == 1234:
        intent==0
    else:
        intent -= 1
        if intent>0:
            print("PIN incorrecto, vuelva a ingresar su PIN, le quedan ", pin, "intentos antes de que se bloquee su cuenta")
        if intent<=0:
            print("Cuenta bloqueada, llamando a la policia y bloqueando cuenta...")
            


#opc=int(input("BIENVENIDO AL MENU DE SU BANCA\nMENU:\n1.Consultar saldo\n2.Retirar dinero\n3.Depositar dinero\n4.Salir"))