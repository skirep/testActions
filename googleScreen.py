from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time

service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--headless --window-size=1920,1080')

driver = webdriver.Chrome(service=service, options=options)

try:
    # Open Google
    driver.get(os.environ["WEB_URL"])

    # Wait 5 seconds
    driver.implicitly_wait(8)

    timestr = "capture-" + time.strftime("%Y%m%d-%H%M%S") + ".png"

    # Make screenshot
    driver.save_screenshot(timestr)
    print("Screenshot done.")


finally:
    # Cierra el navegador
    driver.quit()
