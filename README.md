# 🛡️ CyberSim - Simulador de Ataques para Capacitación

Este proyecto consiste en un simulador educativo de ataques cibernéticos centrado en pruebas de fuerza bruta sobre aplicaciones web vulnerables como DVWA. El propósito es capacitar a estudiantes y profesionales en el reconocimiento de vulnerabilidades y respuesta ante ataques reales, en un entorno seguro y controlado mediante Docker.

---

## 🚀 Tecnologías utilizadas

- **Python 3.9+**
- **Docker & Docker Compose**
- **DVWA (Damn Vulnerable Web App)**
- **BeautifulSoup4**
- **Requests**
- **Visual Studio Code**

---

## 📦 Paquetes de Python utilizados

Los paquetes requeridos están definidos de forma directa en el script, pero pueden instalarse con:

```bash
pip install requests beautifulsoup4
```

- `requests`: Para realizar peticiones HTTP automatizadas al servidor.
- `beautifulsoup4`: Para analizar y extraer datos del HTML devuelto por DVWA.

---

## 🧰 Estructura del proyecto

```
cybersim-demo/
├── docker-compose.yml       # Levanta DVWA
├── scripts/
│   ├── brute_force.py       # Script de fuerza bruta en Python
│   └── venv/                # Entorno virtual de Python
```

---

## 🔧 Requisitos

1. Docker Desktop instalado y corriendo.
2. Python 3.9 o superior.
3. VS Code o cualquier editor compatible.
4. Git instalado.

---

## 🛠️ Pasos de instalación y despliegue

```bash
# Clona el repositorio
git clone https://github.com/tu_usuario/cybersim-demo.git
cd cybersim-demo

# Levanta DVWA en Docker
docker-compose up -d
```

### Configura DVWA en el navegador

1. Abre `http://localhost:8080/setup.php` y crea la base de datos.  
2. Inicia sesión con:  
   - Usuario: `admin`  
   - Contraseña: `password`  
3. Cambia el nivel de seguridad a **Low**.

```bash
# Prepara el entorno Python
cd scripts
python -m venv venv
source venv/Scripts/activate  # En Linux/Mac: source venv/bin/activate

# Instala las dependencias
pip install requests beautifulsoup4

# Ejecuta el script de fuerza bruta
python brute_force.py
```

---

## ⚠️ Advertencia

> Este entorno fue creado únicamente para fines académicos y de capacitación.  
> **No debe usarse para probar ataques en entornos reales o no autorizados.**

---

## 📚 Créditos

Proyecto académico desarrollado por:

- **Candelario Sánchez Ulises Ramses**
- **Licea Sahagún Chanel Xcaret**
- **Ochoa Díaz Santiago**

**Profesor:** José Rodrigo Ramírez Anguiano
