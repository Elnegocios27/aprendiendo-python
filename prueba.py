from datetime import datetime
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def addition(a, b):
        return a + b
def subtract(a, b):
        return a - b
def multiply(a, b):
        return a * b
def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: division by zero not allowed."

last_result = None

while True:

    print("======================")
    print("       calculator     ")
    print("======================")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("6. History")
    print("======================")
    print("ans last result")

    option = input("option (1-5): ")
    
    if option == '5':
        print("leaving")
        break
    if option == '6':
        try:
            with open("history_calculator.txt", 'r', encoding='utf-8')as archivo:
                 print("previous calculations: ")
                 print(archivo.read())
        except ValueError:
             print("there were no previous calculations.")
        continue

    entry1 = input("enter the first number or ans: ")
    if entry1 == 'ans':
        if last_result is not None:
                num1 = last_result
        else:
            print("there were no previous number.")
            continue
    else:
        try:
            num1 = float(entry1)
        except ValueError:
            print("invalid entry")
            continue

    entry2 = input("enter the second number or ans: ")
    if entry2 == 'ans':
        if last_result is not None:
                num2 = last_result
        else:
            print("there were no previous number.")
            continue
    else:
        try:
             num2 = float(entry2)
        except ValueError:
             print("invalid entry")
             continue

    if option == '1':
        result = addition(num1, num2)
        symbol = '+'
    elif option == '2':
        result = subtract(num1, num2)
        symbol = '-'
    elif option == '3':
        result = multiply(num1, num2)
        symbol = '*'
    elif option == '4':
        result = divide(num1, num2)
        symbol = '/'
    else:
        print("invalid option.")
        continue 

    print("result: ", result)
    if isinstance(result, (int, float)):
         last_result = result

    operation = f"{num1} {symbol} {num2} = {result}"    
    
    with open("history_calculations_py.txt", 'a', encoding='utf-8')as archivo:
         archivo.write(f"[{date}] {operation}\n")