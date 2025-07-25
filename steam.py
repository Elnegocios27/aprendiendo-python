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

    print(f"price in pesos: ${precio_final:,.2f}")
else:
    print("fatal error")