def mostrar_menu(nombre, opciones):  # incorporamos el parámetro para mostrar el nombre del menú
    print(f'# {nombre}. Seleccione una opción: ')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(nombre, opciones, opcion_salida):  # incorporamos el parámetro para mostrar el nombre del menú
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Numero 1', funcion1),
        '2': ('Numero 2', funcion2),  # la acción es una llamada a submenu que genera un nuevo menú
        '3': ('Numero 3', funcion3),
        '4': ('Salir', salir)
    }

    generar_menu('Bienvenido selecciona un Numero', opciones, '4')  # indicamos el nombre del menú

# A partir de aquí creamos las funciones que ejecutan las acciones de los menús
def funcion1():
    print('Has elegido la opción 1 activando la puerta')


def funcion2():
    print('Has elegido la opción 2 activando el panel solar')


def funcion3():
    print('Has elegido la opción 3 monitoreo de la puerta trasera')



def salir():
    print('Saliendo')
    if _name_ ==  '_main_' :
         menu_principal() # iniciamos el programa mostrando el menú principal
