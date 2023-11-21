from selenium import webdriver

# Especifica la ubicación del chromedriver.exe en tu sistema
# Puedes descargarlo desde https://sites.google.com/chromium.org/driver/
chromedriver_path = './chromedriver'

# Crea una instancia del navegador Chrome
options = webdriver.ChromeOptions()

# Deshabilita la interfaz gráfica de usuario (UI) para ejecutar en segundo plano
options.add_argument('--headless')

# Inicia el navegador con las opciones configuradas
browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

try:
    # Abre la página de Google
    browser.get('https://www.google.com')

    # Espera a que la página se cargue completamente (puedes ajustar este tiempo según sea necesario)
    browser.implicitly_wait(5)

    # Toma una captura de pantalla y guárdala en un archivo
    browser.save_screenshot('captura_de_pantalla.png')
    print("Captura de pantalla exitosa. Archivo guardado como 'captura_de_pantalla.png'.")

finally:
    # Cierra el navegador
    browser.quit()