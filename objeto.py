import blessed
import math
from blessed import Terminal 
from datetime import datetime
term = Terminal() 
allowed = "0123456789+-*/()., "

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

while True:
    expr = input(">>> ")
    
    if not all(c in allowed or c.isalpha() for c in expr):
        print("error syntaxis")
        continue

    try:
        result = eval(expr, {"__builtins__": None}, vars(math))
        print(term.green(str(result)))
    except Exception as e:
        print(term.red(f"error in evaluation: {e}"))

    with open("history.txt", "a") as f:
        f.write(f"{date} - {expr} = {result}\n")