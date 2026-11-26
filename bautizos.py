from almacenamiento import generar_codigo, guardar_registro, listar_registros


def registrar_bautizo():
    codigo = generar_codigo("bautizos.txt", "BAU")

    print("\n--- REGISTRO DE BAUTIZO ---")
    print("Codigo de acta:", codigo)

    nombre = input("Nombre completo: ")
    nacimiento = input("Fecha de nacimiento: ")
    fecha = input("Fecha de bautizo: ")
    pastor = input("Pastor encargado: ")
    padrinos = input("Padrinos: ")
    lugar = input("Lugar de bautizo: ")

    datos = [codigo, nombre, nacimiento, fecha, pastor, padrinos, lugar]

    guardar_registro("bautizos.txt", datos)

    print("Bautizo registrado correctamente.")
    print("Codigo:", codigo)


def ver_bautizos():
    listar_registros("bautizos.txt", "LISTA DE BAUTIZOS")