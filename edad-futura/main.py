AÑOS_A_SUMAR = 5

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  Este dato es obligatorio, por favor escríbalo")


def pedir_edad(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            edad = int(texto)
        except ValueError:
            print("  Valor no válido. Escriba la edad en números enteros, por ejemplo 18")
            continue
        if edad < 0:
            print("  La edad no puede ser negativa")
            continue
        return edad


def main():
    print("=== Edad futura ===")
    nombre = pedir_texto("Ingrese su nombre: ")
    edad_actual = pedir_edad("Ingrese su edad actual: ")

    edad_futura = edad_actual + AÑOS_A_SUMAR

    print()
    print(
        f"{nombre}, hoy tienes {edad_actual} años y dentro de "
        f"{AÑOS_A_SUMAR} años tendrás {edad_futura} años"
    )


if __name__ == "__main__":
    main()
