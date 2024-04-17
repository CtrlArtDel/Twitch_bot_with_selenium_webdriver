import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_mobile_driver():
    mobile_emulation = {"deviceName": "Nexus 5"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Determine the operating system
    if platform.system() == 'Linux':
        chrome_driver_path = '../drivers/chromedriver-linux64/chromedriver'
    elif platform.system() == 'Windows':
        chrome_driver_path = '../drivers/chromedriver-win64/chromedriver.exe'
    else:
        raise Exception("Unsupported operating system.")

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver
