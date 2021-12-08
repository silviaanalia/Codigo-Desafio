Agenda = {}
Buscarcontacto = True

while Buscarcontacto:
    print()
    print("\t Agenda")
    print(" ********** *********")
    print("1. Cargar contacto")
    print("2. Buscar contacto")
    print("3. Salir")
    print("  *******************")

    opcion = ""
    while opcion not in ("1", "2", "3"):
        opcion = input("ingrese su opcion: ")

   
    if opcion == "1":
        cantidadcontacto = 0
        while cantidadcontacto <5:
            
            nombre = input("Nombre: ")
            if nombre in Agenda:
                print("Ese contacto ya existe en su agenda")
            else:
                numero = int(input("numero: "))
                Agenda[nombre]= numero
                cantidadcontacto += 1
                print("Su contacto fue agregado exitosamente")

    elif opcion == "2": 
        nombre = input("Nombre: ")
        if nombre not in Agenda:
            print("Este contacto no existe")   
        else:
            agenda1 = Agenda[nombre] 
            print("numero: ", agenda1) 

    elif opcion == "3":
        Buscarcontacto = False 
    

