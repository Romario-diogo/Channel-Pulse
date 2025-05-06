from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# === 1. Configurações do navegador ===
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# === 2. Inicia o driver ===
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# === 3. Injeta spoof de fingerprint ===
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    // WebDriver = false
    Object.defineProperty(navigator, 'webdriver', { get: () => false });

    // Idiomas
    Object.defineProperty(navigator, 'languages', { get: () => ['pt-BR', 'pt', 'en-US'] });

    // Threads e memória
    Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 4 });
    Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });

    // Plataforma
    Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });

    // Plugins fake
    Object.defineProperty(navigator, 'plugins', {
      get: () => [{
        name: 'Chrome PDF Plugin',
        filename: 'internal-pdf-viewer',
        description: 'Portable Document Format'
      }]
    });

    // WebGL spoof
    const getParameter = WebGLRenderingContext.prototype.getParameter;
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
        if (parameter === 37445) return 'NVIDIA Corporation';
        if (parameter === 37446) return 'NVIDIA GeForce RTX 3060';
        return getParameter.call(this, parameter);
    };

    // Canvas spoof real
    const toDataURL = HTMLCanvasElement.prototype.toDataURL;
    HTMLCanvasElement.prototype.toDataURL = function() {
        const ctx = this.getContext('2d');
        ctx.fillStyle = '#f00';
        ctx.fillRect(0, 0, this.width, this.height);
        return toDataURL.call(this);
    };

    // Chrome spoof
    Object.defineProperty(window, 'chrome', {
      get: () => ({ runtime: {} })
    });

    // Permissions spoof
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.query = (parameters) => (
        parameters.name === 'notifications'
          ? Promise.resolve({ state: Notification.permission })
          : originalQuery(parameters)
    );
    """
})

# === 4. Acesso ao site e coleta ===
driver.get("https://amiunique.org/fingerprint")
time.sleep(15)

with open("amiunique_selenium.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.save_screenshot("amiunique_selenium.png")

time.sleep(120)
driver.quit()
