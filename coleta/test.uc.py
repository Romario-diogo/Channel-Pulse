import undetected_chromedriver as uc

options = uc.ChromeOptions()

driver = uc.Chrome(
    version_main=110,
    driver_executable_path=r"E:\Pasta (R)\Programas\chrome110\chromedriver.exe",
    browser_executable_path=r"E:\Pasta (R)\Programas\chrome110\GoogleChromePortable64\App\Chrome-bin\chrome.exe",
    options=options
)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()
