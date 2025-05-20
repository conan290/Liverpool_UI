import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PerfumesResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.ver_mas_marcas = (By.ID, "Marcas")
        self.checkbox_dior = (By.ID, "brand-DIOR")


    def expand_brands(self):
        ver_mas_elem = self.driver.find_element(*self.ver_mas_marcas)
        ver_mas_elem.click()
        time.sleep(4)

    def select_dior_brand(self):
        wait = WebDriverWait(self.driver, 20)
        dior_checkbox = wait.until(EC.presence_of_element_located(self.checkbox_dior))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dior_checkbox)
        time.sleep(7)
        dior_checkbox.click()




