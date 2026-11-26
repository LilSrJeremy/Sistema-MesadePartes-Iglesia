from almacenamiento import generar_codigo, guardar_registro, listar_registros


def registrar_presentacion():
    codigo = generar_codigo("presentaciones.txt", "PRE")

    print("\n--- PRESENTACION DE NIÑO ---")
    print("Codigo de registro:", codigo)

    nombre = input("Nombre del niño: ")
    padres = input("Nombre de los padres: ")
    fecha = input("Fecha de presentacion: ")
    ministro = input("Ministro encargado: ")
    lugar = input("Lugar: ")

    datos = [codigo, nombre, padres, fecha, ministro, lugar]

    guardar_registro("presentaciones.txt", datos)

    print("Presentacion registrada correctamente.")
    print("Codigo:", codigo)


def ver_presentaciones():
    listar_registros("presentaciones.txt", "LISTA DE PRESENTACIONES")
