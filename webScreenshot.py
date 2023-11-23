from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1920, 1080)

try:
    # Open Google
    driver.get(os.environ["WEB_URL"])

    # Wait 5 seconds
    driver.implicitly_wait(8)

    timestr = "capture-" + time.strftime("%Y%m%d-%H%M%S") + ".png"

    driver.find_element(By.ID, 'didomi-notice-agree-button').click()
    
    # Make screenshot
    driver.save_screenshot(timestr)
    print("Screenshot done.")


finally:
    # Cierra el navegador
    driver.quit()
