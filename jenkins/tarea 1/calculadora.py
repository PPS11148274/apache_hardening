def realizar_operacion(opcion, num1, num2):
    """Realiza la operación matemática correspondiente"""
    if opcion == '1' or opcion == '+':
        return num1 + num2
    elif opcion == '2' or opcion == '-':
        return num1 - num2
    elif opcion == '3' or opcion == '*':
        return num1 * num2
    elif opcion == '4' or opcion == '/':
        if num2 == 0:
            raise ValueError("No se puede dividir por cero")
        return num1 / num2
    else:
        raise ValueError("Operación no válida")

def calculadora():
    print("Calculadora Básica")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")

    while True:
        try:
            opcion = input("\nSeleccione una operación (1-5) o ingrese el símbolo: ")

            if opcion.lower() == 'salir' or opcion == '5':
                print("¡Hasta luego!")
                break

            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            resultado = realizar_operacion(opcion, num1, num2)
            print(f"Resultado: {num1} {opcion} {num2} = {resultado}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    calculadora()
