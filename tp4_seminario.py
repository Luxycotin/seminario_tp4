matriz = []
#Creo una lista vacía para guardar los datos de las personas

while True:
    #Se crea un bucle infinito para que el programa no termine hasta que el usuario lo decida :)
    print("-Menú: ")
    print("1. Ingresar persona")
    print("2. Mostrar datos")
    print("3. Buscar por DNI")
    print("4. Salir")
    
    opcion = input("Elige una opción: ").strip()
    #El "strip" se usa para eliminar los espacios en blanco que el usuario pueda ingresar por error
    
    
    if opcion == "1":
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
        #Uso el split para separar los datos que el usuario ingrese por comas
        telefonos = input("Teléfonos (separados por comas): ").split(",")
        hijos = input("Hijos (separados por comas): ").split(",")
        
        #Uso del [t.strip() for t in telefonos] para eliminar los espacios en cada teléfono ingresado, y lo mismo para los hijos
        matriz.append([nombre, apellido, dni, [t.strip() for t in telefonos], [h.strip() for h in hijos]])
        print("Persona agregada.")



    elif opcion == "2":
        if not matriz:
            print("No hay personas registradas.")
        else:
            #En caso de haber personas registradas, se recorre la matriz con un for y muestra los resultados
            for p in matriz:
                # p[0] = nombre, p[1] = apellido, p[2] = DNI
                # p[3] = lista de teléfonos, p[4] = lista de hijos  
                print(f"{p[0]} {p[1]}, DNI: {p[2]}, {len(p[3])} Teléfono(s), {len(p[4])} Hijo(s)")
            print("Matriz:", matriz)

    elif opcion == "3":
        dni_buscar = input("DNI a buscar: ").strip()
        # 'next()' devuelve la primera coincidencia o 'None' si no encuentra nada
        persona = next((p for p in matriz if p[2] == dni_buscar), None)

        if persona:
            print(f"{persona[0]} {persona[1]}, DNI: {persona[2]}, {len(persona[3])} Teléfono(s), {len(persona[4])} Hijo(s)")
        else:
            print("DNI no encontrado.")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
