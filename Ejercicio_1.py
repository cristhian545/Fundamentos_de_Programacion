edad = int(input("Ingrese su edad:"))

quintil = int(input("Ingrese su quintil:"))

plan_dental = 80000
radiografia_dental = 12000

if edad <= 25 and (quintil == 1 or quintil == 2):
    descuento = plan_dental * 0.18
    precio_Final = round(plan_dental-descuento)

    print("El valor de su plan dental es:",precio_Final)
    
    
elif edad <= 25 and (quintil == 3 or quintil == 4):
    descuento = plan_dental * 0.12
    precio_Final = round(plan_dental-descuento)
    

    print("El valor de su plan dental es:",precio_Final)
    
    
elif edad >= 26 and edad <= 45 and (quintil == 1 or quintil == 2):
    descuento = plan_dental * 0.12
    precio_Final = round(plan_dental-descuento)
    print("El valor de su plan dental es:",precio_Final)


elif edad >= 26 and edad <= 45 and (quintil == 3 or quintil == 4):
    descuento = plan_dental * 0.8
    precio_Final = round(plan_dental-descuento)
    print("El valor de su plan dental es:",precio_Final)
    
    