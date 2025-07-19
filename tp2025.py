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
import msvcrt
import os
import datetime
from colorama import Style,init,Fore
import random
init()
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
def limpiar():
    command = 'limpiar'
    if os.name == 'nt':
        command = 'cls'
    else:
        command = 'clear'#Por si utiliza max o linux
    os.system(command)
def carteldeasteriscos(cadena):
    linea = '*' * (4 + len(cadena))
    return(f'{linea}\n* {cadena} *\n{linea}')
def carteldebarras(cadena):
    linea = '-' * (4+ len(cadena))
    return(f'{linea}\n| {cadena} |\n{linea}') 
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
    ["","",""],
    ["","",""]]
vuelos = [["" for j in range(5)] for i in range(20)]   
 # Datos iniciales de novedades
novedad1="Promoción de verano"
novedad2="Nuevo destino agregado"
novedad3="Descuento por fidelidad"
cantVuelos=[["Aerolíneas Argentinas ",0],
            ["LATAM Airlines",0],
            ["Flybondi",0],
            ["GOL",0],
            ["IBERIA",0]]
vuelos = [[""]*7 for i in range(20)]
precioVuelos = [0.0]*20   
aerolineas=["AA","LATAM","FLY","GOL","IBERIA"]
matrizAsientos = [[""]*7 for i in range(40)]
vuelosUsuario = [[""]*7 for i in range(20)]
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
def registrarse():
    limpiar()
    print("Registro de usuario")
    email = input("Ingrese su correo electrónico: ")
    while "@" not in email and email !="":
        email = input("Correo inválido. Ingrese un correo electrónico válido: ")
    
    contraseña = input_con_asteriscos("Ingrese su contraseña: ")

    tipo_usuario = "usuario"
    i=0
    try:
        while i < 10:
            if usuarios[i][0] =="":
                usuarios[i][0] = email
                usuarios[i][1] = contraseña
                usuarios[i][2] = tipo_usuario
                
            i+=1
    except IndexError:
        limpiar()
        print("No se pudo registrar el usuario, intente nuevamente más tarde.")
        input("Presione enter para continuar.")
        limpiar()
        return
    print("\nRegistro exitoso.")
    input("Presione enter para continuar.")
    limpiar()
    login()
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
                        menu_usuario()
                        return
        except:
            limpiar()
            print("Usuario o contraseña incorrectos.")
            intentos += 1
    print("El sistema se cerrará, hasta luego!.")
def generar_asientos():
    lugarVacio= 0
    while lugarVacio < 40 and matrizAsientos[lugarVacio][0] == '':       
        for i in range(40):
            fila=[""]*7
            for j in range(7):
                if j == 3:
                    fila[j]=("")
                else:
                    fila[j]=(random.choice(["L", "O", "R"]))
            matrizAsientos[lugarVacio] = fila
            lugarVacio += 1    
def mostrar_asientos_vuelo(nro_vuelo):
    inicio = nro_vuelo * 40
    fin = inicio + 40
    for i in range(inicio, fin):
        print(f"Fila {i - inicio + 1}: {matrizAsientos[i]}")
def listarVuelosAerolineas():
    print("Reporte de vuelos vigentes por aerolinea")
    for i in range(5):
        for j in range(5):
            if cantVuelos[i][1]>cantVuelos[j][1]:
                aux = cantVuelos[i]
                cantVuelos[i] = cantVuelos[j]
                cantVuelos[j] = aux
    print("="*65)
    print("REPORTE DE VUELOS VIGENTES POR AEROLÍNEA")
    print("="*65)
    print(f"{'POSICIÓN':<10} {'AEROLÍNEA':<30} {'CANTIDAD DE VUELOS':>20}")
    print("-"*65)

    total_vuelos = 0

    for i in range(5):
        nombre = cantVuelos[i][0]
        cantidad = cantVuelos[i][1]
        print(f"{i:<10} {nombre:<30} {cantidad:>20}")
        total_vuelos += cantidad

    print("-"*65)
    print(f"{'TOTAL DE VUELOS VIGENTES:'}{total_vuelos}")            
    print(f"{'Aerolinea con MAYOR cantidad de vuelos:'}{cantVuelos[0][0]} ({cantVuelos[0][1]})")            
    print(f"{'Aerolinea con MENOR cantidad de vuelos:'}{cantVuelos[4][0]} ({cantVuelos[4][1]})")            
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
            print("Vuelo", i+1, ":",
                  "Aerolinea:",vuelos[i][2], 
                  Fore.GREEN + "Origen:",vuelos[i][3], 
                  Fore.CYAN + "Destino:", vuelos[i][4], 
                  Fore.LIGHTGREEN_EX + "Fecha:", vuelos[i][5], 
                  "Hora:", vuelos[i][6],
                  Style.RESET_ALL)
        i+=1
def crearVuelo():
    
    print("Bienvenido a la creación de vuelos.")
    verVuelosCargados=input("¿Desea ver los vuelos actuales? (s/n): ").lower()
    while verVuelosCargados != "s" and verVuelosCargados != "n":
        verVuelosCargados = input("Opción inválida. Ingrese 's' para ver los vuelos actuales o 'n' para no verlos: ").lower()
    if verVuelosCargados == "s":
        verVuelos()
    seguirCreando=True
    while seguirCreando:
        limite=0
        try:
            while limite <= 20 and vuelos[limite][0] == '':
                print("\nIngrese los datos del vuelo:")
                print("Codigos de aerolíneas disponibles:\nAA(Aerolineas Argentinas)\nLATAM(LATAM Airlines)\nFLY\nGOL\nIBERIA")
                vuelos[limite][2]= input("Ingrese el código de la aerolínea: ").upper()
                while buscarAerolinea(vuelos[limite][0]) == False:
                    print("Codigos de aerolíneas disponibles:\nAA(Aerolineas Argentinas)\nLATAM(LATAM Airlines)\nFLY\nGOL\nIBERIA")
                    vuelos[limite][0] = input("Código de aerolínea inválido. Ingrese un código válido: ").upper()
                vuelos[limite][3] = input("Ingrese el origen del vuelo: ")
                vuelos[limite][4] = input("Ingrese el destino del vuelo: ")
                vuelos[limite][5] = input("Ingrese la fecha de salida (DD/MM/AAAA): ")
                while validar_fecha(vuelos[limite][5]) == False:
                    vuelos[limite][5] = input("Fecha inválida. Ingrese una fecha válida (DD/MM/AAAA): ")
                vuelos[limite][6] = input("Ingrese la hora de salida (HH:MM): ")
                while validar_hora(vuelos[limite][6]) == False:
                    vuelos[limite][6] = input("Hora inválida. Ingrese una hora válida (HH:MM): ")
                if vuelos[limite][5] <= datetime.now().strftime("%d/%m/%Y"):
                    if vuelos[limite][1] == "AA":
                        cantVuelos[0][1] += 1
                    elif vuelos[limite][0] == "LATAM":
                        cantVuelos[1][1] += 1
                    elif vuelos[limite][0] == "FLY":
                        cantVuelos[2][1] += 1
                    elif vuelos[limite][0] == "GOL":
                        cantVuelos[3][1] += 1
                    elif vuelos[limite][0] == "IBERIA":
                        cantVuelos[4][1] += 1
                vuelos[limite][7]= limite
                vuelos[limite][0]= "A"
                try:
                    precioVuelos[limite] = float(input("Ingrese el precio del vuelo: "))
                    while precioVuelos[limite] <= 0:
                        print("El precio es erroneo, intente nuevamente")
                        precioVuelos[limite] = float(input("Ingrese el precio del vuelo: "))
                except ValueError:
                    print("Precio inválido. Debe ser un número.")
                generar_asientos()
                limite += 1
                continuar = input("¿Desea cargar otro vuelo? (s/n): ").lower()
                if continuar != "s":
                    listarVuelosAerolineas()
                    mostrar_asientos_vuelo(limite)
                    seguirCreando = False
        except IndexError:
            limpiar()
            listarVuelosAerolineas()
            print("No hay mas espacio para cargar vuelos, intente mas tarde.")
            input("Presione enter para continuar.")
            seguirCreando = False
def modificarVuelo():
    modificarVuelos = True
    while modificarVuelos:
        if vuelos[0][0] == "":
            print("No hay vuelos cargados para modificar.")
            input("Presione enter para continuar.")
            modificarVuelos = False
        else:
            print("Modificación de vuelo")
            verVuelos()
            vueloAModificar=input("Ingrese el código del vuelo a modificar: ")
            i=0
            while i < 20 and vuelos[i][1] != vueloAModificar:
                i += 1
            if vuelos[i][1] == vueloAModificar:
                if vuelos[i][0] == "B":
                    baja=input("El vuelo está dado de baja, desea modificarlo? (s/n): ")
                    while baja != "s" and baja != "n":
                        baja = input("Opción inválida. Ingrese 's' para modificar el vuelo o 'n' para no modificarlo: ").lower()
                    if baja == "s":
                        vuelos[i][0] = "A"
                        print("Datos del vuelo a modificar:", vuelos[i])
                        vuelos[i][0]= input("Ingrese el código de la aerolínea: ").upper()
                        while buscarAerolinea(vuelos[i][0]) == False:
                            print("Codigos de aerolíneas disponibles:\nAA(Aerolineas Argentinas)\nLATAM(LATAM Airlines)\nFLY\nGOL\nIBERIA")
                            vuelos[i][0] = input("Código de aerolínea inválido. Ingrese un código válido: ").upper()
                        vuelos[i][1] = input("Ingrese el nuevo origen del vuelo: ")
                        vuelos[i][2] = input("Ingrese el nuevo destino del vuelo: ")
                        vuelos[i][3] = input("Ingrese la nueva fecha de salida (DD/MM/AAAA): ")
                        while validar_fecha(vuelos[i][3]) == False:
                            vuelos[i][3] = input("Fecha inválida. Ingrese una fecha válida (DD/MM/AAAA): ")
                        vuelos[i][4] = input("Ingrese la nueva hora de salida (HH:MM): ")
                        while validar_hora(vuelos[i][4]) == False:
                            vuelos[i][4] = input("Hora inválida. Ingrese una hora válida (HH:MM): ")
                        try:
                            precioVuelos[i] = float(input("Ingrese el nuevo precio del vuelo: "))
                            while precioVuelos[i] <= 0:
                                print("El precio es erroneo, intente nuevamente")
                                precioVuelos[i] = float(input("Ingrese el nuevo precio del vuelo: "))
                        except ValueError:
                            print("Precio inválido. Debe ser un número.")
                    else:
                        modificarVuelos = False
                        print("Modificación cancelada.")                     
def eliminarVuelo():
    eliminarVuelo = True
    while eliminarVuelo:
        if vuelos[0][0] == "":
            print("No hay vuelos cargados para modificar.")
            input("Presione enter para continuar.")
            eliminarVuelo = False
        else:
            print("Eliminación de vuelos")
            verVuelos()
            vueloAEliminar=input("Ingrese el código del vuelo a modificar: ")
            i=0
            while i < 20 and vuelos[i][1] != vueloAEliminar:
                i += 1
            if vuelos[i][1] == vueloAEliminar:
                if vuelos[i][0] == "B":
                    print("El vuelo ya está dado de baja.")
                    input("Presione enter para continuar.")
                else:
                    print("Datos del vuelo a eliminar:", vuelos[i])
                    confirmacion = input("¿Está seguro que desea eliminar el vuelo? (s/n): ").lower()
                    while confirmacion != "s" and confirmacion != "n":
                        confirmacion = input("Opción inválida. Ingrese 's' para eliminar el vuelo o 'n' para no eliminarlo: ").lower()
                    if confirmacion == "s":
                        vuelos[i][0]= "B"
                    else:
                        eliminarVuelo = False
                        print("Eliminación cancelada.")
def gestionDePromociones():
    print(Fore.RED + carteldebarras("En construcción..."))
    input("Presione enter para volver al menú anterior.")
    print(Style.RESET_ALL)
def reportes():

    print(Fore.RED + carteldebarras("En construcción..."))
    input("Presione enter para volver al menú anterior.")
    print(Style.RESET_ALL)
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
def ver_novedades():
    limpiar()
    print("\nNovedades actuales:")
    print("N1:", novedad1[0])
    print("N2:", novedad2[0])  
    print("N3:", novedad3[0])  
def mostrar_matriz(codigo):
    i = 0
    while i < 40:
        j = 0
        while j < 7:
            if j == 3:
                print("|", end="  ")  # Pasillo
            else:
                print(matrizAsientos[codigo][j], end="  ")
            j += 1
        print()  # Salto de línea al final de cada fila
        i += 1
def buscarCodigo(codigo):
    i=0
    while vuelosUsuario[i][1]!= codigo and i<= 20:
        i+=1
    if vuelosUsuario[i][1]== codigo:
        return True
    else:
        return "n"
def verVuelosUsuario():
    print("\nVuelos actuales:")
    i=0
    while i < 20:
        if vuelosUsuario[i][0]!="" and vuelosUsuario[i][0]!="B":
            print("Vuelo", i+1, ":",
                  "Código:", vuelosUsuario[i][1],
                  "Aerolinea:",vuelosUsuario[i][2], 
                  Fore.GREEN + "Origen:",vuelosUsuario[i][3], 
                  Fore.CYAN + "Destino:", vuelosUsuario[i][4], 
                  Fore.LIGHTGREEN_EX + "Fecha:", vuelosUsuario[i][5], 
                  "Hora:", vuelosUsuario[i][6],
                    Fore.YELLOW + "Precio:", precioVuelos[i],
                  Style.RESET_ALL)
        i+=1
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
def buscarVuelo():
    fecha= input("Ingrese la fecha de salida (DD/MM/AAAA): ")
    while validar_fecha(fecha) == False:
        print("Fecha inválida. Por favor, ingrese una fecha en formato DD/MM/AAAA.")
        fecha = input("Ingrese la fecha de salida (DD/MM/AAAA): ")
    i=0
    while i < 20 and vuelos[i][0] != '':
        if vuelos[i][0]== "B":
            i=i
        elif vuelos[i][5] >= fecha:
            vuelosUsuario[i][0] = vuelos[i][0]
            vuelosUsuario[i][1] = vuelos[i][1]
            vuelosUsuario[i][2] = vuelos[i][2]
            vuelosUsuario[i][3] = vuelos[i][3]
            vuelosUsuario[i][4] = vuelos[i][4]
            vuelosUsuario[i][5] = vuelos[i][5]
            vuelosUsuario[i][6] = vuelos[i][6]
        i +=1
    verVuelosUsuario()
def buscarAsientos():
    try:
        codigo_vuelo = input("Ingrese el código del vuelo: ")
        while buscarCodigo(codigo_vuelo) == "n":
            codigo_vuelo = input("Código inválido. Ingrese un código de vuelo válido: ")
        codigo_vuelo = int(codigo_vuelo)
        mostrar_matriz(codigo_vuelo)
        input("Presione enter para continuar.")
    except IndexError:
        print("El código de vuelo no existe o no se ha ingresado correctamente.")
        print("En caso de que el problema persista, vuelva a buscar vuelos")
        input("Presione enter para volver al menú anterior.")
        limpiar()     
def menu_usuario():
    menuUsuario = True
    while menuUsuario:
        print("\nMenú de usuario")
        print("1. Buscar Vuelo")
        print("2. Buscar asientos")
        print("3. Reservar Vuelos")
        print("4. Gestionar Reservas")
        print('5. Ver historial de compras(reservas con estado "Confirmada")')
        print("6. Ver Novedades")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            buscarVuelo()
        elif opcion == "2":
            limpiar()
            buscarAsientos()
        elif opcion == "3":
            limpiar()
            reservarVuelo()
        elif opcion == "4":
            limpiar()
            gestionReservas()
        elif opcion == "5":
            limpiar()
            historial()
        elif opcion == "6":
            limpiar()
            ver_novedades()
        elif opcion == "7":
            limpiar()
            print("Saliendo del sistema.")
            menuUsuario= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
def gestionReservas():
    print(Fore.RED + carteldebarras("En construcción..."))
    input(Style.RESET_ALL+"Presione enter para volver al menú anterior.")
    limpiar()
def historial():
    print(Fore.RED + carteldebarras("En construcción..."))
    input(Style.RESET_ALL+"Presione enter para volver al menú anterior.")
    limpiar()
def reservarVuelo():
    print(Fore.RED + carteldebarras("En construcción..."))
    input(Style.RESET_ALL+"Presione enter para volver al menú anterior.")
    limpiar()
iniciar()

print(carteldeasteriscos('Este trabajo fue hecho por Nicolás Vannelli, Mateo Paolizzi, Agustín Andrenacci,Mateo Glich Vargas .'))