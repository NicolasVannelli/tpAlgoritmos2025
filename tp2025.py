import msvcrt
import os
import datetime
""" 
                                        Iniciacion de variables
password->string
iniciarPrograma->bool
ch->string
command->string
usuarioAdmin->string
constraseñaAdmin->string
novedad1->string
novedad2->string
novedad3->string
intentos->int
usuario->string
contraseña->string
menuAdministrador->bool
linea->string
opcion->int
gestionAerolineas->bool
nombre->string
codigo->string
descripcion->string
pais->string
seguir->bool
arg->int
bra->int
chi->int
continuar->string
pais_mayor->string
mayor_cantidad->int
pais_menor->string
menor_cantidad->int
gestionNovedades->bool
codigo->string
nuevo_texto->string
"""
            #Inicio de funciones esteticas
# Función para ocultar contraseña con asteriscos
def input_con_asteriscos(prompt=''):
    print(prompt, end='', flush=True)
    password = ''
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
    if os.name == 'nt':
        command = 'cls'
    else:
        command = 'clear'#Por si utiliza max o linux
    os.system(command)
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
def validar_hora(hora_str):
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False
#Para la despedida
def carteldeasteriscos(cadena):
    linea = '*' * (4 + len(cadena))
    return(f'{linea}\n* {cadena} *\n{linea}')


            #Fin funciones esteticas
# Para el logeo  cod=0  usuario=1                     pass=2  tipo=3 
def buscarAerolinea(codigo):
    i=0
    while aerolineas[i]!= codigo and i<= 4:
        i+=1
    if aerolineas[i]== codigo:
        return True
    else:
        return False
usuarios = [
    ["admin@ventaspasajes777.com","admin","administrador"],
    ["ceo1@ventaspasajes777.com","ceo123","ceo"],
    ["ceo2@ventaspasajes777.com","ceo456","ceo"],
    ["ceo3@ventaspasajes777.com","ceo789","ceo"],
    ["ceo4@ventaspasajes777.com","ceo012","ceo"],
    ["ceo5@ventaspasajes777.com","ceo345","ceo"],
    ["usuario1@ventaspasajes777.com","usuario123","usuario"],   
    ["usuario2@ventaspasajes777.com","usuario456","usuario"],
    [],
    []
    ]
vuelos = [["" for j in range(5)] for i in range(20)]   
 # Datos iniciales de novedades
novedad1="Promoción de verano"
novedad2="Nuevo destino agregado"
novedad3="Descuento por fidelidad"
aerolineas=["AA","LATAM","FLY","GOL","IBERIA"]

def iniciar():
    inicio= input("¿Desea registrarse o desea iniciar sesión? (r/i): ").lower()
    while inicio != "r" and inicio != "i":
        inicio = input("Opción inválida. Ingrese 'r' para registrarse o 'i' para iniciar sesión: ").lower()
    if inicio == "r":
        limpiar()
        registrarse()
    elif inicio == "i":
        limpiar()
        login()
# Función para logear
def registrarse():
    limpiar()
    print("Registro de usuario")
    email = input("Ingrese su correo electrónico: ")
    while email != "" or "@" not in email:
        email = input("Correo inválido. Ingrese un correo electrónico válido: ")
    
    contraseña = input_con_asteriscos("Ingrese su contraseña: ")
    while len(contraseña) < 6:
        contraseña = input_con_asteriscos("Contraseña demasiado corta. Ingrese una contraseña de al menos 6 caracteres: ")

    tipo_usuario = "usuario"

    usuarios.append([email, contraseña, tipo_usuario])
    print("Registro exitoso.")
    input("Presione enter para continuar.")
    limpiar()
def login():
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese usuario: ")
        contraseña = input_con_asteriscos("Ingrese contraseña: ")
        try:
            for i in usuarios:
                if i[0] == usuario and i[1] == contraseña:
                    if i[2] == "administrador":
                        limpiar()
                        menu_administrador()
                        return
                    elif i[2] == "ceo":
                        limpiar()
                        menu_ceo()
                        return
                    elif i[2] == "usuario":
                        limpiar()
                        print("Bienvenido usuario, esta sección está en construcción.")
                        input("Presione enter para continuar.")
                        limpiar()
                        return
        except:
            limpiar()
            print("Usuario o contraseña incorrectos.")
            intentos += 1
    print("El sistema se cerrará, hasta luego!.")
def menu_ceo():
    menuCeo = True
    while menuCeo:
        print("\nMenú del CEO")
        print("1. Gestión de Vuelo")
        print("2. Gestión de Promociones")
        print("3. Reportes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            gestionDeVuelo()
        elif opcion == "2":
            limpiar()
            gestionDePromociones()
        elif opcion == "3":
            limpiar()
            reportes()
        elif opcion == "4":
            limpiar()
            print("Saliendo del sistema.")
            menuCeo= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
def gestionDeVuelo():
    
    menuVuelo = True
    while menuVuelo:
        
        print("\nMenú de vuelos")
        print("1. Crear Vuelo")
        print("2. Modificar Vuelo")
        print("3. Eliminar Vuelo")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            crearVuelo()
        elif opcion == "2":
            limpiar()
            modificarVuelo()
        elif opcion == "3":
            limpiar()
            eliminarVuelo()
        elif opcion == "4":
            limpiar()
            print("Saliendo del sistema.")
            menuVuelo= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
def verVuelos():
    print("\nVuelos actuales:")
    i=0
    while i < 20:
        if vuelos[i][0]!="":
            print("Vuelo", i+1, ":",vuelos[i])
        i+=1
def crearVuelo():
    print("Bienvenido a la creación de vuelos.")
    verVuelosCargados=input("¿Desea ver los vuelos actuales? (s/n): ").lower()
    if verVuelosCargados == "s":
        verVuelos()
    seguirCreando=True
    limite=0
    while seguirCreando and limite<=20:
        print("\nIngrese los datos del vuelo:")
        print("Codigos de aerolíneas disponibles:\nAA(Aerolineas Argentinas)\nLATAM(LATAM Airlines)\nFLY\nGOL\nIBERIA")
        vuelos[limite][0]= input("Ingrese el código de la aerolínea: ").upper()
        while buscarAerolinea(vuelos[limite][0]) == False:
            print("Codigos de aerolíneas disponibles:\nAA(Aerolineas Argentinas)\nLATAM(LATAM Airlines)\nFLY\nGOL\nIBERIA")
            vuelos[limite][0] = input("Código de aerolínea inválido. Ingrese un código válido: ").upper()
        vuelos[limite][1] = input("Ingrese el origen del vuelo: ")
        vuelos[limite][2] = input("Ingrese el destino del vuelo: ")
        vuelos[limite][3] = input("Ingrese la fecha de salida (DD/MM/AAAA): ")
        while validar_fecha(vuelos[limite][3]) == False:
            vuelos[limite][3] = input("Fecha inválida. Ingrese una fecha válida (DD/MM/AAAA): ")
        vuelos[limite][4] = input("Ingrese la hora de salida (HH:MM): ")
        while validar_hora(vuelos[limite][4]) == False:
            vuelos[limite][4] = input("Hora inválida. Ingrese una hora válida (HH:MM): ")
        limite += 1
        continuar = input("¿Desea cargar otro vuelo? (s/n): ").lower()
        if continuar != "s":
            seguirCreando = False
        
def gestionDePromociones():

def reportes():
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
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "3":
            limpiar()
            gestion_novedades()
        elif opcion == "4":
            limpiar()
            print("En construcción…")
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "5":
            limpiar()
            print("Saliendo del sistema.")
            menuAdministrador= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
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
    input("Presione enter para volver al menú anterior.")
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
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "b":
            modificar_novedad()
        elif opcion == "d":
            ver_novedades()
            input("Presione enter para continuar.")
            limpiar()
        elif opcion == "e":
            gestionNovedades = False
            limpiar()
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")

# Modificar novedad
def modificar_novedad():
    global novedad1, novedad2, novedad3 
    ver_novedades()
    codigo = input("Ingrese el código de la novedad que desea modificar: ").upper
    while codigo != "N1" and codigo != "N2" and codigo != "N3":
        codigo = input("Código inválido. Ingrese N1, N2 o N3: ").upper()
    if codigo == "N1":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 1: "))
        novedad1 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione enter para volver al menú anterior.")
    elif codigo == "N2":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 2: "))
        novedad2 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione enter para volver al menú anterior.")
    elif codigo == "N3":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 3: "))
        novedad3 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione enter para volver al menú anterior.")

# Ver novedades
def ver_novedades():
    limpiar()
    print("\nNovedades actuales:")
    print("N1:", novedad1[0])
    print("N2:", novedad2[0])  
    print("N3:", novedad3[0])  
# Ejecución del programa
print(novedad1)
login()

print(carteldeasteriscos('Este trabajo fue hecho por Nicolás Vannelli, Mateo Paolizzi, Agustín Andrenacci,Mateo Glich Vargas .'))