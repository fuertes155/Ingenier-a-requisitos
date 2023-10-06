#Funcion 1
def suma(A, B):
    return A + B
#Funcion 2
def resta(A, B):
    return A - B
#Funcion 3
def multiplicacion(A, B):
    return A * B
#Funcion 4
def division(A, B):
    if B == 0:
        return "No se puede dividir por cero"
    else:
        return A / B

# Menú de la calculadora
while True:
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elije una opción (1,2,3,4,5): ")
    
    if opcion == '5':
        print("¡Chao!")
        break
    
    numer1 = float(input("Digite el primer número: "))
    numer2 = float(input("Digite el segundo número: "))
    
    if opcion == '1':
        print("Resultado:", suma(numer1, numer2))
    elif opcion == '2':
        print("Resultado:", resta(numer1, numer2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(numer1, numer2))
    elif opcion == '4':
        print("Resultado:", division(numer1, numer2))
    else:
        print("Esta opcion no es valida.Elija cualquiera de las otras opciones (1,2,3,4,5).")