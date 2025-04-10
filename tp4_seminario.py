matriz = []


while True:
  
    print("-Menú: ")
    print("1. Ingresar persona")
    print("2. Mostrar datos")
    print("3. Buscar por DNI")
    print("4. Salir")
    
    opcion = input("Elige una opción: ").strip()
    
    
    
    if opcion == "1":
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
    
        telefonos = input("Teléfonos (separados por comas): ").split(",")
        hijos = input("Hijos (separados por comas): ").split(",")
        
      
        matriz.append([nombre, apellido, dni, [t.strip() for t in telefonos], [h.strip() for h in hijos]])
        print("Persona agregada.")



    elif opcion == "2":
        if not matriz:
            print("No hay personas registradas.")
        else:
        
            for p in matriz:
            
                print(f"{p[0]} {p[1]}, DNI: {p[2]}, {len(p[3])} Teléfono(s), {len(p[4])} Hijo(s)")
            print("Matriz:", matriz)

    elif opcion == "3":
        dni_buscar = input("DNI a buscar: ").strip()
        
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
