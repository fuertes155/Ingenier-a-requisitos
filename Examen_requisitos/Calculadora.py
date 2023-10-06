
def suma(a, b):
    return a + b

# F
def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b

# Menú de la calculadora
while True:
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elije una opción (1/2/3/4/5): ")
    
    if opcion == '5':
        print("¡Hasta luego!")
        break
    
    num1 = float(input("Digite el primer número: "))
    num2 = float(input("Digite el segundo número: "))
    
    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5).")