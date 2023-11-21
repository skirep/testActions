from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open Google
    driver.get('https://www.google.com')

    # Wait 5 seconds
    driver.implicitly_wait(5)

    timestr = "capture-" + time.strftime("%Y%m%d-%H%M%S") + ".png"

    # Make screenshot
    driver.save_screenshot(timestr)
    print("Screenshot done.")


finally:
    # Cierra el navegador
    driver.quit()
