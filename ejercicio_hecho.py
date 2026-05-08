from random import randint

num1 = int(input("Ingrese numero inferior : "))
num2 = int(input("Ingrese numero superior : "))

numeroAleatorio = randint(num1,num2)

if num1 < num2:
    # que el residuo sea diferente a 1 
    if numeroAleatorio %2 != 0:
        if numeroAleatorio + 1 <= num2:
            numeroAleatorio = numeroAleatorio + 1

        else:
            numeroAleatorio = numeroAleatorio - 1

        intento1 = int(input("Ingrese 1er internto"))
        if intento1 == numeroAleatorio:
            print("Ganaste")
        if intento1 < numeroAleatorio:
            print("su numero es mayor")
        else:
            print("su numero es menor ")

        intento2 = int(input("Ingrese 2do internto"))
        if intento2 == numeroAleatorio:
            print("Ganaste")
        else:
            if intento2 < numeroAleatorio:
                print("su numero es mayor")
            else:
                print("su numero es menor ")
            distancia1 = abs(intento1 - numeroAleatorio)
            distancia2 = abs(intento2 - numeroAleatorio)

            if distancia1 < distancia2:
                print(" El intento 1 estuvo mas cerca")
            else:
                print("El intento 2 estuvo mas cerca")

            intento3 = int(input("Ingrese 3er intento"))
            if intento3 == numeroAleatorio:
                print("ganaste")
            else:
                print("perdiste",numeroAleatorio)