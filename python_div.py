def main():
    try:
        divisor = float(input("Ingresa un número para dividir 10 entre él: "))
        result = 10 / divisor
        print(f"El resultado de la división es: {result}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Ingresa un valor numérico válido. :D ")

main()