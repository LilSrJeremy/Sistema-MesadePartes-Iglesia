from almacenamiento import generar_codigo, guardar_registro, listar_registros


def registrar_matrimonio():
    codigo = generar_codigo("matrimonios.txt", "MAT")

    print("\n--- REGISTRO DE MATRIMONIO ---")
    print("Codigo de acta:", codigo)

    contrayente1 = input("Nombre del primer contrayente: ")
    contrayente2 = input("Nombre del segundo contrayente: ")
    fecha = input("Fecha de ceremonia: ")
    pastor = input("Pastor encargado: ")
    testigos = input("Testigos: ")
    lugar = input("Lugar de ceremonia: ")

    datos = [codigo, contrayente1, contrayente2, fecha, pastor, testigos, lugar]

    guardar_registro("matrimonios.txt", datos)

    print("Matrimonio registrado correctamente.")
    print("Codigo:", codigo)


def ver_matrimonios():
    listar_registros("matrimonios.txt", "LISTA DE MATRIMONIOS")

