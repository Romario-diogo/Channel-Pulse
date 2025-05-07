import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

# Configurar opções do navegador
options = uc.ChromeOptions()

# Recomendações para reduzir detecção
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
#options.add_argument("--lang=pt-BR,pt")
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
)
options.binary_location = r"E:\Pasta (R)\Programas\chrome110\GoogleChromePortable64\App\Chrome-bin\110.0.5481.104\chrome.exe"

driver = uc.Chrome(
    version_main=110,
    options=options,
    driver_executable_path=r"C:\SeleniumDrivers\chromedriver_110\chromedriver.exe"
)


# Injeções de camuflagem via CDP
scripts = [
    # 🧬 Spoof Canvas
    """
    const toDataURLBackup = HTMLCanvasElement.prototype.toDataURL;
    HTMLCanvasElement.prototype.toDataURL = function() {
        const ctx = this.getContext("2d");
        ctx.fillStyle = "rgb(100,100,100)";
        ctx.fillRect(0, 0, this.width, this.height);
        return toDataURLBackup.apply(this, arguments);
    };
    const getImageDataBackup = CanvasRenderingContext2D.prototype.getImageData;
    CanvasRenderingContext2D.prototype.getImageData = function(x, y, w, h) {
        for (let i = 0; i < arguments.length; i++) {
            arguments[i] = Math.floor(arguments[i] * Math.random());
        }
        return getImageDataBackup.apply(this, arguments);
    };
    """,

    # 🧬 Spoof Lista de Fontes (JS)
    """
    const originalFonts = ['Arial', 'Verdana', 'Times New Roman'];
    const originalCheck = FontFaceSet.prototype.check;
    FontFaceSet.prototype.check = function(font, text) {
        if (originalFonts.some(f => font.includes(f))) {
            return true;
        }
        return originalCheck.call(this, font, text);
    };
    """,

    # 🧬 Spoof WebGL Renderer
    """
    const getParameterBackup = WebGLRenderingContext.prototype.getParameter;
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
        if (parameter === 37445) return "Intel Inc."; // UNMASKED_VENDOR_WEBGL
        if (parameter === 37446) return "Intel Iris OpenGL Engine"; // UNMASKED_RENDERER_WEBGL
        return getParameterBackup.call(this, parameter);
    };
    """,

    # 🧬 WebGL Supported Extensions
    """
    const getExtensionsBackup = WebGLRenderingContext.prototype.getSupportedExtensions;
    WebGLRenderingContext.prototype.getSupportedExtensions = function() {
        return ['EXT_blend_minmax', 'EXT_color_buffer_float', 'WEBGL_lose_context'];
    };
    """,

    # 🧬 Navigator Properties (plugins, languages, platform, etc.)
    """
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    Object.defineProperty(navigator, 'languages', { get: () => ['pt-BR', 'en-US'] });
    Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
    Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });
    Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 4 });
    Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });
    """
]

# Injetar todos os scripts
for script in scripts:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})


# Acessar o site de fingerprint
driver.get("https://amiunique.org/fingerprint")


# Esperar carregar a página e gerar fingerprint
time.sleep(10)  # Tempo para o fingerprint ser gerado

# Opcional: fazer screenshot da página com resultado
driver.save_screenshot("fingerprint_test.png")

time.sleep(150)
# Fechar
driver.quit()
