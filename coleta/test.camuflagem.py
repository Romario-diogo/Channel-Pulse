from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # Seletor de elemento 

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://amiunique.org/")
driver.maximize_window()

time.sleep(10)
botao = driver.find_element(By.CSS_SELECTOR,"#app > div > main > div > div > section > div > div.text-left.col-md-6.col-12 > div > a")
botao.click()
time.sleep(10)
