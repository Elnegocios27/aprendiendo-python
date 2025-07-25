import requests
print("//welcome to steam calculator//")
print("this program can give a price of a game of dolars a pesos")
usd = float(input("write an amount of dolars:"))

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