from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def find_and_wait_element_to_be_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def choose_search_box_and_fill_in_with_text(driver, text):
    search_element = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
    search_element.send_keys(text)
    search_element.send_keys(Keys.ENTER)

def scroll_down(driver, scrolls=1):
    for _ in range(scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

def find_element_by_locator_and_store_elements_in_list(driver, locator, timeout=60):
    elements = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located(locator)
    )
    return elements


def take_screenshot(driver, filename):
    driver.save_screenshot(filename)

def wait_for_element_to_load(driver, element_selector, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
