import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SmartTVResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.size_filter = (By.XPATH, "//label[@title='Tamaño']")
        self.price_filter = (By.XPATH, "//label[@title='Precios']")
        self.ver_mas_marcas = (By.ID, "Marcas")
        self.ver_mas_tamanos = (By.ID, "Tamao")
        self.checkbox_sony = (By.ID, "brand-SONY")
        self.checkbox_55_pulgadas = (By.ID, "variants.normalizedSize-55 pulgadas")
        self.radio_precio_mayor_10000 = (By.ID, "variants.prices.sortPrice-10000-700000")

    def verify_size_filter_present(self):
        wait = WebDriverWait(self.driver, 20)
        size_element = wait.until(EC.presence_of_element_located(self.size_filter))
        return size_element is not None

    def verify_price_filter_present(self):
        price_element = self.driver.find_element(*self.price_filter)
        return price_element is not None

    def select_price_filter(self):
        price_radio = self.driver.find_element(*self.radio_precio_mayor_10000)
        price_radio.click()
        time.sleep(12)

    def expand_brands(self):
        ver_mas_marcas = self.driver.find_element(*self.ver_mas_marcas)
        ver_mas_marcas.click()
        time.sleep(12)

    def select_brand_sony(self):
        sony_checkbox = self.driver.find_element(*self.checkbox_sony)
        sony_checkbox.click()
        time.sleep(12)


    def select_size_55_inches(self):
        pulgadas_checkbox = self.driver.find_element(*self.checkbox_55_pulgadas)
        pulgadas_checkbox.click()
        time.sleep(12)

    def get_results_count(self):
        product_cards = self.driver.find_elements(By.CLASS_NAME, "m-product__card")
        return len(product_cards)



