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

ultimo_resultado = None

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
    print("ans significa ultimo resultado")

    opcion = input("elegí una opción (1-5): ")
    
    if opcion == '5':
        print("saliendo de la calculadora")
        break

    entrada1 = input("ingrese el primer numero o ans: ")
    if entrada1 == 'ans':
        if ultimo_resultado is not None:
                num1 = ultimo_resultado
        else:
            print("no hubo un resultado anterior")
            continue
    else:
        try:
            num1 = float(entrada1)
        except ValueError:
            print("entrada invalida")
            continue

    entrada2 = input("ingrese el primer numero o ans: ")
    if entrada2 == 'ans':
        if ultimo_resultado is not None:
                num2 = ultimo_resultado
        else:
            print("no hubo resultado anterior")
            continue
    else:
        try:
             num2 = float(entrada2)
        except ValueError:
             print("entrada invalida")
             continue

    if opcion == '1':
        resultado = sumar(num1, num2)
    elif opcion == '2':
        resultado = restar(num1, num2)
    elif opcion == '3':
        resultado = multiplicar(num1, num2)
    elif opcion == '4':
        resultado = dividir(num1, num2)
    else:
        print("opcion no valida")
        continue

    print("resultado: ", resultado)
    if isinstance(resultado, (int, float)):
         ultimo_resultado = resultado