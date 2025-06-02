import os, time, msvcrt
menu = f"""--- MENÚ ---
1) Agregar alumnos
2) Ver alumnos
3) Salir
{"-"*20}"""

while True:
    os.system("cls || clear")
    print(menu)
    opt=input("Ingrese opción: ")
    os.system("cls || clear")
    if opt=="1":
        pass
    elif opt=="2":
        pass
    elif opt=="3":
        pass
    else:
        print("ERROR! Elija una opción válida")
        print("\nPresione una tecla para continuar...")
        msvcrt.getch()