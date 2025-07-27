import requests
print("//welcome to steam calculator//")
print("this program can give a price of a game of dolars to pesos")
print("Type a number in dollars or 'history' to see the saved conversions.")
print("Type 'exit' to exit.")

while True:
    entrance = input("write an amount of dolars:").strip().lower()
    if entrance == "exit":
        print("exit ok")
        break

    if entrance == "history":
        try:
            with open("history_convertion.txt", "r", encoding="utf-8") as archivo:
                print("//historial of conversions//")
                print(archivo.read())
        except FileNotFoundError:
            print("history not found")
        continue

    try:
        usd = float(entrance)
    except ValueError:
        print("error, invalid entry")
        continue

    url = "https://dolarapi.com/v1/dolares/blue"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    price = data["venta"]
    usd_with_iva = usd * 1.21
    price_finally = usd_with_iva * price

    with open("history_convertion.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"USD {usd} → ${price_finally:,.2f} ARS (IVA include)\n")

    print(f"price in pesos: ${price_finally:,.2f}")
else:
    print("fatal error")