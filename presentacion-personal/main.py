def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  Este dato es obligatorio, por favor escríbalo")


def main():
    print("=== Presentación personal ===")
    nombre = pedir_texto("Ingrese su nombre: ")
    ciudad = pedir_texto("Ingrese su ciudad: ")
    programa = pedir_texto("Ingrese su programa académico: ")

    mensaje = (
        f"Hola, mi nombre es {nombre}, vivo en la ciudad de {ciudad} "
        f"y estudio {programa}"
    )

    print()
    print(mensaje)


if __name__ == "__main__":
    main()
