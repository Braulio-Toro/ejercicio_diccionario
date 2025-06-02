import os, time, msvcrt

menu = """--- Menú ---
1) Agregar alumnos
2) Ver alumnos
3) Salir
"""

#La lista vacía para almacenar diccionarios de alumnos
alumnos = []

while True:
    os.system("cls || clear")
    print(menu)
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        os.system("cls || clear")
        while True:
            nombre = input("Ingrese el nombre del alumno: ").strip().title()
            if len(nombre) < 3:
                print("ERROR! El nombre debe tener al menos 3 caracteres.")
                time.sleep(2)
            else:
                break
        while True:
            try:
                edad = int(input("Ingrese la edad del alumno: "))
                if edad < 17:
                    print("ERROR! La edad debe ser mayor o igual a 17 años.")
                    time.sleep(2)
                else:
                    break
            except ValueError:
                print("ERROR! Debe ingresar un número válido para la edad.")
                time.sleep(2)
        while True:
            try:
                codigo = int(input("Ingrese el código del alumno: "))
                if codigo <= 0:
                    print("ERROR! El código debe ser un número positivo.")
                    time.sleep(2)
                else:
                    break
            except ValueError:
                print("ERROR! Debe ingresar un número válido para el código.")
                time.sleep(2)

        # Si todo es válido, agregar alumno como diccionario
        alumno = {
            "nombre": nombre,
            "edad": edad,
            "código": codigo
        }
        alumnos.append(alumno)
        print("\nAlumno agregado correctamente.")
        time.sleep(3)

    elif opcion == "2":
        os.system("cls || clear")
        if len(alumnos) == 0:
            print("No hay información registrada.")
        else:
            print("--- Lista de Alumnos ---\n")
            for x in alumnos:
                for llave in x:
                    print(llave, "=>", x[llave])
                print("-" * 30)  # Separador entre alumnos
        time.sleep(1)
        print("\nPresione cualquier tecla para continuar... ")
        msvcrt.getch()

    elif opcion == "3":
        print("Saliendo del sistema, hasta luego!")
        break

    else:
        print("ERROR! Debe ingresar una opción válida (1, 2 o 3).")
        time.sleep(3)