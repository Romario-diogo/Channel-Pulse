from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializa navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/@inglesfacilcomprofessormar6592")
driver.maximize_window()

link_tag = driver.find_element(By.CSS_SELECTOR, 'link[rel="canonical"]')

time.sleep(6)
# Extrai o href
canonical_url = link_tag.get_attribute("href")
time.sleep(2)
# Usa regex ou split para extrair o ID
channel_id = canonical_url.split("/")[-1]  # ou com regex
time.sleep(5)
print(f"✅ ID do canal: {channel_id}")

time.sleep(10)

driver.quit()
