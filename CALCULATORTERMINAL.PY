import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    return math.sqrt(a)



def calculadora():
    print("Bienvenido a la calculadora científica.")
    
    while True:
        print("Selecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("0. Salir")
        
        opcion = input("Ingrese el número de la operación deseada: ")
        
        if opcion == "0":
            print("¡Hasta luego!")
            break
        
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            num1 = float(input("Ingrese el primer número: "))
            
            if opcion != "6":
                num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == "1":
                resultado = suma(num1, num2)
            elif opcion == "2":
                resultado = resta(num1, num2)
            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
            elif opcion == "4":
                resultado = division(num1, num2)
            elif opcion == "5":
                resultado = potencia(num1, num2)
            elif opcion == "6":
                resultado = raiz_cuadrada(num1)
            
            print("El resultado es:", resultado)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

calculadora()




































