from datetime import datetime

def sumar(numeros):
    return numeros[0] + numeros[1]

def restar(numeros):
    return numeros[0] - numeros[1]

def multiplicar(numeros):
    return numeros[0] * numeros[1]

def dividir(numeros):
    if numeros[1] != 0:
        return numeros[0] / numeros[1]
    else:
        return "error division por cero"

fecha = datetime.now().strftime("%Y-%m-%d-%h:%M")

numeros = []

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

numeros.append(num1)
numeros.append(num2)

print("numeros guardados: ", numeros)

print("que operacion queres realizar?")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividr")
print("5. salir")

opcion = input("opcion: ")

if opcion == '1':
    resultado = sumar(numeros)
    operacion = "suma"

elif opcion == '2':
    resultado = restar(numeros)
    operacion = "restar"

elif opcion == '3':
    resultado = multiplicar(numeros)
    operacion = "multiplicar"

elif opcion == '4':
    resultado = dividir(numeros)
    operacion = "dividir"
else:
    print("operacion no valida")
    resutlado = None

if resultado is not None:
    print(f"Resultado de la {operacion}: {resultado}")

with open("historial.txt", "a", encoding='utf-8')as archivo:
    archivo.write(f"[{fecha}] {operacion}\n")