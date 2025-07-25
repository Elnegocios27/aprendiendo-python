import requests
print("//welcome to steam calculator//")
print("this program can give a price of a game of dolars to pesos")
print("Type a number in dollars or 'historial' to see the saved conversions.")
print("Type 'salir' to exit.")

while True:
    entrada = input("write an amount of dolars:").strip().lower()
    if entrada == "salir":
        print("exit ok")
        break

    if entrada == "historial":
        try:
            with open("historial_conversión.txt", "r", encodin="utf-8") as archivo:
                print("//historial of conversions//")
                print(archivo.read())
        except FileNotFoundError:
            print("history not found")
        continue

    try:
        usd = float(entrada)
    except ValueError:
        print("error, invalid entry")
        continue

    url = "https://dolarapi.com/v1/dolares/blue"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    cotizacion = data["venta"]
    usd_con_iva = usd * 1.21
    precio_final = usd_con_iva * cotizacion

    with open("historial_conversión.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"USD {usd} → ${precio_final:,.2f} ARS (IVA incluido)\n")

    print(f"price in pesos: ${precio_final:,.2f}")
else:
    print("fatal error")