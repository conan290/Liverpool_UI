import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.console_verification = (By.XPATH, "//img[contains(@alt, 'Consola Playstation Liverpool')]")
        self.juegos_verification = (By.XPATH, "//img[contains(@alt, 'Juegos Playstation Liverpool')]")
        self.wait = WebDriverWait(self.driver, 20)

    def verify_consola_section_present(self):
        consola_banner = self.wait.until(EC.presence_of_element_located(self.console_verification))
        return consola_banner is not None #couldnt verify the text "playstation5" because its an image
                                          #couldnt use .is_displayed, for some reason it kept on failing

    def verify_juegos_section_present(self):
        juegos_banner = self.wait.until(EC.presence_of_element_located(self.juegos_verification))
        return juegos_banner.is_displayed()

    def select_consola_ps5(self):
        consola_banner = self.wait.until(EC.element_to_be_clickable(self.console_verification))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", consola_banner)
        time.sleep(1)
        consola_banner.click()

