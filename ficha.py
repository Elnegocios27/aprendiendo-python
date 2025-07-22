import requests

url = "https://pokeapi.co/api/v2/pokemon/charizard"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("ID:", data["id"])
    print("Habilidades:")
    for habilidad in data["abilities"]:
        print("-", habilidad["ability"]["name"])
        
    print("Nombre:", data["name"])
    print("Peso:", data["weight"])
else:
    print("Error al obtener los datos.")
    