while True:
    print("======================")
    print("       calculadora     ")
    print("======================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("======================")

    def sumar(a, b):
        return a + b
    def restar(a, b):
        return a - b
    def multiplicar(a, b):
        return a * b
    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division por cero no permitida."
    
    opcion = input("elegí una opción (1-5):")
    if opcion == '1':
        num1 = float(input("primer numero:"))
        num2 = float(input("segundo numero:"))
        resultado = num1 + num2
        print("resultado:", resultado)
    if opcion == '2':
        num1 = float(input("primer numero:"))
        num2 = float(input("segundo numero:"))
        resultado = num1 - num2
        print("resultado:", resultado)
    if opcion == '3':
        num1 = float(input("primer numero:"))
        num2 = float(input("segundo numero:"))
        resultado = num1 * num2
        print("resultado:", resultado)
    if opcion == '4':
        num1 = float(input("primer numero:"))
        num2 = float(input("segundo numero:"))
        resultado = num1 / num2
        print("resultado:", resultado)
    if opcion == '5':
        print("saliendo de la calculadora")
        break