import msvcrt
import os
            #Inicio de funciones esteticas
# Función para ocultar contraseña con asteriscos
def input_con_asteriscos(prompt=''):
    print(prompt, end='', flush=True)
    password = ''#ch
    iniciarPrograma = True
    while iniciarPrograma:
        ch = msvcrt.getch()
        if ch == b'\r' or ch == b'\n':
            iniciarPrograma = False
        else:
                password += ch.decode('utf-8')
                print('*', end='', flush=True)
    return password
#Función para limpiar la consola
def limpiar():
    command = 'limpiar'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#Para la despedida
def carteldeasteriscos(cadena):
    linea = '*' * (4 + len(cadena))
    print(f'{linea}\n* {cadena} *\n{linea}')


            #Fin funciones esteticas
# Para el logeo
usuarioAdmin = "admin@ventaspasajes777.com"
constraseñaAdmin = "admin"
 # Datos iniciales de novedades
novedad1="Promoción de verano"
novedad2="Nuevo destino agregado"
novedad3="Descuento por fidelidad"
# Función para logear
def login():
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese usuario: ")
        contraseña = input_con_asteriscos("Ingrese contraseña: ")
        if usuario == usuarioAdmin and contraseña == constraseñaAdmin:
            limpiar()
            menu_administrador()
        else:
            print("Usuario o contraseña incorrectos.")
            intentos += 1
    print("Demasiados intentos. El sistema se cerrará.")

# Menú principal del administrador
def menu_administrador():
    menuAdministrador = True
    while menuAdministrador:
        print("\nMenú del Administrador")
        print("1. Gestión de Aerolíneas")
        print("2. Aprobar/Denegar Promociones")
        print("3. Gestión de Novedades")
        print("4. Reportes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            gestion_aerolineas()
        elif opcion == "2":
            limpiar()
            print("En construcción…")
            input("Presione cualquier tecla para volver al menú anterior.")
            limpiar()
        elif opcion == "3":
            limpiar()
            gestion_novedades()
        elif opcion == "4":
            limpiar()
            print("En construcción…")
            input("Presione cualquier tecla para volver al menú anterior.")
            limpiar()
        elif opcion == "5":
            limpiar()
            print("Saliendo del sistema.")
            menuAdministrador= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione cualquier tecla para volver al menú anterior.")
            limpiar()

# Gestión de aerolíneas
def gestion_aerolineas():
    gestionAerolineas=True
    while gestionAerolineas:
        print("\nGestión de Aerolíneas")
        print("1. Crear Aerolínea")
        print("2. Modificar Aerolínea")
        print("3. Eliminar Aerolínea")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            crear_aerolineas()
        elif opcion == "2":
            limpiar()
            print("La opción 2 está en construcción")
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "3":
            limpiar()
            print("La opción 3 está en construcción")
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "4":
            limpiar()
            gestionAerolineas = False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
            limpiar()

# Crear aerolíneas
def crear_aerolineas():
    arg=0
    bra=0
    chi=0

    seguir=True
    while seguir:
        nombre = input("Nombre de la aerolínea: ")
        codigo = input("Código IATA (máximo 3 caracteres): ").upper()
        while len(codigo) > 3:
            codigo = input("Código inválido. Ingrese nuevamente (máx 3 caracteres): ").upper()
        descripcion = input("Descripción: ")
        pais = input("Código de país (ARG, CHI, BRA): ").upper()
        while pais != "ARG" and pais != "CHI" and pais != "BRA":
            pais = input("Código inválido. Ingrese ARG, CHI o BRA: ").upper()
        if pais == "ARG":
            arg+=1
        elif pais == "BRA":
            bra+=1
        elif pais == "CHI":
            chi+=1    
        

        continuar = input("¿Desea cargar otra aerolínea? (s/n): ").lower()
        limpiar()
        if continuar != "s":
            seguir=False

    # Mostrar estadísticas
    pais_mayor = ""
    if arg >= bra and arg >= chi:
        pais_mayor = "Argentina"
        mayor_cantidad=arg
    elif bra >= arg and bra >= chi:
        pais_mayor = "Brasil"
        mayor_cantidad=bra
    elif chi >= arg and chi >= bra:
        pais_mayor = "Chile"
        mayor_cantidad=chi
    pais_menor = ""
    if arg <= bra and arg <= chi:
        pais_menor = "Argentina"
        menor_cantidad=arg
    elif bra <= arg and bra <= chi:
        pais_menor = "Brasil"
        menor_cantidad=bra
    elif chi <= arg and chi <= bra:
        pais_menor = "Chile"
        menor_cantidad=chi
    print(f"\nPaís con mayor cantidad de aerolíneas: {pais_mayor} con {mayor_cantidad} aerolinea/s ")
    print(f"País con menor cantidad de aerolíneas: {pais_menor} con {menor_cantidad} aerolinea/s")
    input("Presione cualquier tecla para volver al menú anterior.")
    limpiar()
# Gestión de novedades
def gestion_novedades():
    gestionNovedades=True
    while gestionNovedades:
        print("\nGestión de Novedades")
        print("a. Crear Novedad")
        print("b. Modificar Novedad")
        print("c. Eliminar Novedad")
        print("d. Ver Novedades")
        print("e. Volver")

        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a" or opcion == "c":
            limpiar()
            print("En construcción…")
            input("Presione cualquier tecla para volver al menú anterior.")
            limpiar()
        elif opcion == "b":
            modificar_novedad()
        elif opcion == "d":
            ver_novedades()
            input("Presione cualquier tecla para continuar.")
            limpiar()
        elif opcion == "e":
            gestionNovedades = False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione cualquier tecla para volver al menú anterior.")

# Modificar novedad
def modificar_novedad():
    global novedad1, novedad2, novedad3 
    ver_novedades()
    codigo = input("Ingrese el código de la novedad que desea modificar: ")
    if codigo == "N1":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 1: "))
        novedad1 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione cualquier tecla para volver al menú anterior.")
    elif codigo == "N2":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 2: "))
        novedad2 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione cualquier tecla para volver al menú anterior.")
    elif codigo == "N3":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 3: "))
        novedad3 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione cualquier tecla para volver al menú anterior.")
    else:
        print("Código de novedad no encontrado.")
        input("Presione cualquier tecla para volver al menú anterior.")

# Ver novedades
def ver_novedades():
    limpiar()
    print("\nNovedades actuales:")
    print("N1:", novedad1)
    print("N2:", novedad2)  
    print("N3:", novedad3)  
# Ejecución del programa
login()

print(carteldeasteriscos('Este trabajo fue hecho por Nicolás Vannelli, Mateo Paolizzi, Agustín Andrenacci,Mateo Glich Vargas .'))