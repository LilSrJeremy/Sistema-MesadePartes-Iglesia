from datetime import date


def generar_codigo(archivo_nombre, prefijo):
    archivo = open(archivo_nombre, "a")
    archivo.close()

    archivo = open(archivo_nombre, "r")
    registros = archivo.readlines()
    archivo.close()

    anio = str(date.today().year)
    numero = 1

    for registro in registros:
        if registro.startswith(prefijo + "-" + anio):
            numero += 1

    return prefijo + "-" + anio + "-" + str(numero).zfill(4)


def guardar_registro(archivo_nombre, datos):
    archivo = open(archivo_nombre, "a")
    archivo.write("|".join(datos) + "\n")
    archivo.close()


def listar_registros(archivo_nombre, titulo):
    archivo = open(archivo_nombre, "a")
    archivo.close()

    archivo = open(archivo_nombre, "r")
    registros = archivo.readlines()
    archivo.close()

    print("\n---", titulo, "---")

    if len(registros) == 0:
        print("No hay registros.")
    else:
        for registro in registros:
            datos = registro.strip().split("|")
            print("-------------------------")
            for dato in datos:
                print(dato)
    print("-------------------------")


def buscar_registro(busqueda, archivos):
    encontrado = False

    for archivo_nombre in archivos:
        archivo = open(archivo_nombre, "a")
        archivo.close()

        archivo = open(archivo_nombre, "r")
        registros = archivo.readlines()
        archivo.close()

        for registro in registros:
            if busqueda.lower() in registro.lower():
                datos = registro.strip().split("|")
                encontrado = True

                print("\n--- REGISTRO ENCONTRADO ---")
                for dato in datos:
                    print(dato)
                print("--------------------------")

    if encontrado == False:
        print("No se encontraron registros.")
