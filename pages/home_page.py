from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "mainSearchbar")
        self.categories_button = (By.CSS_SELECTOR, ".a-header__strongLink.nav-desktop-menu-action")
        self.belleza_menu = (By.XPATH, "//a[contains(@href, '/tienda/belleza/cat5020010')]")
        self.perfumes_hombre_option = (By.XPATH, "//a[contains(@href, '/tienda/perfumes-hombre/catst44258581')]")

    def search_product(self, product_name):
        search_input = self.driver.find_element(*self.search_box)
        search_input.clear()
        search_input.send_keys(product_name + Keys.ENTER)

    def open_categories_menu(self):
        categories = self.driver.find_element(*self.categories_button)
        categories.click()
        time.sleep(2)

    def hover_over_belleza_and_select_perfumes_hombre(self):
        belleza = self.driver.find_element(*self.belleza_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(belleza).perform()
        time.sleep(2)
        perfumes_hombre = self.driver.find_element(*self.perfumes_hombre_option)
        perfumes_hombre.click()
        time.sleep(3)
