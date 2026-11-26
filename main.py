from matrimonios import registrar_matrimonio, ver_matrimonios
from bautizos import registrar_bautizo, ver_bautizos
from presentaciones import registrar_presentacion, ver_presentaciones
from almacenamiento import buscar_registro, listar_registros


def main():
    opcion = ""

    while opcion != "9":
        print("\n===================================")
        print(" SISTEMA DE DOCUMENTACION DE IGLESIA")
        print("===================================")
        print("1. Registrar matrimonio")
        print("2. Registrar bautizo")
        print("3. Registrar presentacion de niño")
        print("4. Ver matrimonios")
        print("5. Ver bautizos")
        print("6. Ver presentaciones")
        print("7. Buscar acta por codigo o nombre")
        print("8. Ver todos los registros")
        print("9. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_matrimonio()
        elif opcion == "2":
            registrar_bautizo()
        elif opcion == "3":
            registrar_presentacion()
        elif opcion == "4":
            ver_matrimonios()
        elif opcion == "5":
            ver_bautizos()
        elif opcion == "6":
            ver_presentaciones()
        elif opcion == "7":
            busqueda = input("Ingrese codigo o nombre: ")
            archivos = ["matrimonios.txt", "bautizos.txt", "presentaciones.txt"]
            buscar_registro(busqueda, archivos)
        elif opcion == "8":
            ver_matrimonios()
            ver_bautizos()
            ver_presentaciones()
        elif opcion == "9":
            print("Gracias por utilizar el sistema.")
        else:
            print("Opcion no valida.")
if __name__ == "__main__":
    main()            