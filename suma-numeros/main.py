def pedir_numero(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("  Valor no válido. Escriba un número, por ejemplo 8 o 12.5")


def formatear(numero):
    return str(int(numero)) if numero.is_integer() else str(numero)


def main():
    print("=== Suma de dos números ===")
    primero = pedir_numero("Ingrese el primer número: ")
    segundo = pedir_numero("Ingrese el segundo número: ")

    suma = primero + segundo

    print(f"La suma de {formatear(primero)} + {formatear(segundo)} es {formatear(suma)}")


if __name__ == "__main__":
    main()
