from selenium.webdriver.common.by import By
from driver_setup import get_mobile_driver
import selenium_tools as st
import time
import logging
import os

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TwitchTest:
    search_icon = (By.CSS_SELECTOR, "a[href='/search']")
    streamer = (By.XPATH, "//*/div[contains(@class, 'cVOzFI')]")
    cookies_button = (By.CLASS_NAME, "lnaTdO")

    def __init__(self, context):
        self.driver = get_mobile_driver()
        self.context = context
        logging.info("WebDriver initialized.")

    def navigate_to_twitch(self):
        """Open the Twitch homepage."""
        self.driver.get("https://www.twitch.tv")
        logging.info("Navigated to Twitch.")

    def handle_cookies(self):
        """Attempt to find and click the cookies acceptance button."""
        try:
            button = st.find_and_wait_element_to_be_clickable(self.driver, self.cookies_button)
            button.click()
            logging.info("Cookies consent accepted.")
        except Exception as e:
            logging.info("No cookies consent button found, continuing with the test.")

    def search_for_game(self, game_name):
        search_button = st.find_and_wait_element_to_be_clickable(self.driver, self.search_icon)
        search_button.click()
        st.choose_search_box_and_fill_in_with_text(self.driver, game_name)
        logging.info(f"Search performed for {game_name}.")

    def scroll_down_and_select_streamer(self):
        """Scroll down the page and select the first available streamer."""
        st.scroll_down(self.driver, 2)
        streamers = st.find_element_by_locator_and_store_elements_in_list(self.driver, self.streamer)
        if streamers:
            streamers[0].click()
            logging.info("Streamer selected.")
        else:
            logging.info("No streamers found.")

    def capture_screenshot(self, filename):
        screenshot_directory = os.path.join('..', 'screenshots')
        os.makedirs(screenshot_directory, exist_ok=True)  # Create the directory if it doesn't exist
        full_path = os.path.join(screenshot_directory, filename)
        st.take_screenshot(self.driver, full_path)
        logging.info(f"Screenshot taken and saved as {full_path}.")

    def run_test(self):
        try:
            self.navigate_to_twitch()
            self.handle_cookies()
            self.search_for_game("StarCraft II")
            self.scroll_down_and_select_streamer()
            time.sleep(5)  # Wait for everything to load
            self.capture_screenshot("screenshot.png")
        finally:
            self.driver.quit()
            logging.info("WebDriver session ended.")

if __name__ == "__main__":
    test = TwitchTest(context={})
    test.run_test()
