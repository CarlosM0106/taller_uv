PORCENTAJE_DESCUENTO = 10

def pedir_precio(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(texto)
        except ValueError:
            print("  Valor no válido. Escriba solo el número, por ejemplo 100000")
            continue
        if valor <= 0:
            print("  El precio debe ser mayor que cero")
            continue
        return valor


def formatear(numero):
    numero = round(numero, 2)
    return str(int(numero)) if numero.is_integer() else str(numero)


def main():
    print("=== Precio con descuento ===")
    precio_original = pedir_precio("Ingrese el precio original del producto: ")

    descuento = precio_original * PORCENTAJE_DESCUENTO / 100
    precio_final = precio_original - descuento

    print()
    print(f"Precio original:        {formatear(precio_original)}")
    print(f"Descuento ({PORCENTAJE_DESCUENTO}%):        {formatear(descuento)}")
    print(f"Precio final a pagar:   {formatear(precio_final)}")


if __name__ == "__main__":
    main()
