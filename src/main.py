import requests
from config import BASE_URL

print("Buscando citas de Extranjería...")

try:
    respuesta = requests.get(BASE_URL, timeout=20)

    if respuesta.status_code == 200:
        print("Página de Extranjería disponible.")
    else:
        print(f"Error: {respuesta.status_code}")

except Exception as e:
    print("No se pudo conectar:", e)
