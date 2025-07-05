import requests

# URL de la API
url = "https://jsonplaceholder.typicode.com/users"

# Hacer la solicitud
respuesta = requests.get(url)

# Verificar si salió bien (status 200)
if respuesta.status_code == 200:
    datos = respuesta.json()  # Convertimos a JSON (diccionario/lista)
    
    for usuario in datos:
        print("Nombre:", usuario["name"])
        print("Email:", usuario["email"])
        print("-" * 30)
else:
    print("Error al acceder a la API:", respuesta.status_code)
