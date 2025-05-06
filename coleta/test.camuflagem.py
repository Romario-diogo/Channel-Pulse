from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.36"

options = Options()
options.add_argument(f"user-agent={user_agent}")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Utilizando o DevTools Protocol (CDP) para modificar o navigator.userAgent via JS
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": f"""
        // Sobrescreve o getter de navigator.userAgent
        Object.defineProperty(navigator, 'userAgent', {{
            get: () => '{user_agent}'
        }});
        """
    }
)

driver.get("https://amiunique.org/fingerprint")
driver.maximize_window()
# Espera para garantir carregamento
time.sleep(15)

# Captura o HTML renderizado
# with open("amiunique_selenium.html", "w", encoding="utf-8") as f:
#     f.write(driver.page_source)
time.sleep(125)
driver.quit()
