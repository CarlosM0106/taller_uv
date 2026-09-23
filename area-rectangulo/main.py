def pedir_medida(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(texto)
        except ValueError:
            print("  Valor no válido. Escriba un número, por ejemplo 6 o 2.5")
            continue
        if valor <= 0:
            print("  La medida debe ser mayor que cero")
            continue
        return valor


def formatear(numero):
    numero = round(numero, 4)
    return str(int(numero)) if numero.is_integer() else str(numero)


def main():
    print("=== Área de un rectángulo ===")
    base = pedir_medida("Ingrese la base: ")
    altura = pedir_medida("Ingrese la altura: ")

    area = base * altura

    print()
    print(f"Base ingresada:   {formatear(base)}")
    print(f"Altura ingresada: {formatear(altura)}")
    print(f"Área obtenida:    {formatear(area)}")


if __name__ == "__main__":
    main()
