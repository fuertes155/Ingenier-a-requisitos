def digitos(numero):
    return str(numero)[-4:]

print("Programa para poder generar un boleto de tren para los usuarios")


while True:
    print("Se encuentra en la estación Angeles")
    print("Seleccione su destino:")
    print("1. Santiago (Valor: $180,000)")
    print("2. Armenia (Valor: $250,000)")
    print("3. Melgar (Valor: $250,000)")
    print("4. Filtrap (Valor: $190,000)")
    nume_estacion = int(input("Digite el número de la estación de destino: "))

    if nume_estacion in [1, 2, 3, 4]:
        if nume_estacion == 1:
            valor_boleto = 150000
        elif nume_estacion == 2:
            valor_boleto = 50000
        elif nume_estacion == 3:
            valor_boleto = 200000
        else:
            valor_boleto = 130000

        print(f"El valor del boleto es: ${valor_boleto} COP")
        id = input("Por favor digite su número de Identificación: ")
        tarjeta = input("Digite su número de tarjeta (sin espacios): ")
        n_tarjeta = len(tarjeta)
        n_id = len(id)

        if n_tarjeta !=16 or not tarjeta.isdigit():
            print("Error --- Tarjeta no válida")
            break
        if n_id != 10 or not id.isdigit():
            print("Error --- Identificación no válida")
            break

        print(f"El valor total del boleto es: ${valor_boleto}")
        print(f"Su número de identificación es: {id}")
        print(f"El cobro se efectuará a la tarjeta terminada en: {digitos(tarjeta)}")
    else:
        print("Destino no válido. Inténtelo de nuevo.")
    break
