import math
from blessed import Terminal 
from datetime import datetime
term = Terminal() 
allowed = "0123456789+-*/()., "

while True:
    expr = input(">>> ")
    
    if not all(c in allowed or c.isalpha() for c in expr):
        print("error syntaxis")
        continue
    
    result = None
    try:
        result = eval(expr, {"__builtins__": None}, vars(math))
        print(term.green(str(result)))
    except Exception as e:
        print(term.red(f"error in evaluation: {e}"))

    if result is not None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("history.txt", "a") as f:
            f.write(f"{date} - {expr} = {result}\n")

