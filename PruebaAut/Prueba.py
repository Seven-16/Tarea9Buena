import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
import time
import os

# log
logging.basicConfig(filename="reporte_test.log", level=logging.INFO)
logging.info("Iniciando prueba con Selenium")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# Abrir
driver.get("http://localhost:5100/")


#Crea carpeta
if not os.path.exists("capturas"):
    os.makedirs("capturas")


driver.get_screenshot_as_file("capturas/captura1.png")
time.sleep(4)

# HTML Report Setup
html_report = """
<html>
<head>
    <title>Reporte de Prueba Selenium</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #4CAF50;
        }
        h2 {
            color: #333;
        }
        .step {
            margin: 10px 0;
            padding: 10px;
            background-color: #f1f1f1;
            border-left: 5px solid #4CAF50;
        }
        .screenshot {
            margin: 10px 0;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        .result {
            color: #333;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Reporte de Prueba Selenium</h1>
    <h2>Detalles de la prueba ejecutada:</h2>
"""

# Localizar insertar

#Boton Insertar clic
btnGuardar = driver.find_element(By.ID, "btnregistro") 
btnGuardar.click()
time.sleep(2)


#Matricula input
inputTitulo = driver.find_element(By.ID, "titulo") 
inputTitulo.send_keys("Prueba")
html_report += f"""
    <div class="step">
        <p>Ingresado Titulo: Prueba</p>
        <div class="screenshot">
            <img src="capturas/captura1.png" alt="Captura 1">
        </div>
    </div>
"""

#Nombre input
inputDescripcion = driver.find_element(By.ID, "descripcion") 
inputDescripcion.send_keys("Esto es una prueba.")
html_report += f"""
    <div class="step">
        <p>Ingresado Descripcion: Esto es una prueba.</p>
    </div>
"""


#Apellido input
inputImagen = driver.find_element(By.ID, "imagen") 
inputImagen.send_keys("https://d12i7q49526cmu.cloudfront.net/media/original_images/Selenium_Logo_1.png")
html_report += f"""
    <div class="step">
        <p>Ingresado Imagen: Logo de Selenium.</p>
    </div>
"""


#Curso input
inputFecha = driver.find_element(By.ID, "fecha") 
inputFecha.click()
inputFecha.send_keys("02-12-2024")
html_report += f"""
    <div class="step">
        <p>Ingresado Fecha: Actual</p>
    </div>
"""


#Captura formulario
driver.get_screenshot_as_file("capturas/captura2.png")
time.sleep(5)

btnGuardar = driver.find_element(By.ID, "btnguardar") 
btnGuardar.click()
time.sleep(5)

#Reporte
html_report += f"""
    <div class="step">
        <p>Formulario guardado.</p>
        <div class="screenshot">
            <img src="capturas/captura2.png" alt="Captura de pantalla formulario guardado">
            <img src="capturas/captura3.png" alt="Captura de pantalla formulario guardado">
        </div>
    </div>
"""

driver.get_screenshot_as_file("capturas/captura3.png")

# Cerrar
time.sleep(5)
driver.quit()

html_report += """
    <h2>Resultado de la prueba:</h2>
    <p class="result">Prueba ejecutada con éxito.</p>
</body>
</html>
"""

# Guardar HTML
with open("reporte_prueba.html", "w") as f:
    f.write(html_report)

logging.info("Prueba ejecutada exitosamente y reporte generado.")
