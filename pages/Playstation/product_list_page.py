from selenium.webdriver.common.by import By

class ProductListPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.CLASS_NAME, "section_img_size")

    def select_first_product(self):
        products = self.driver.find_elements(*self.product_cards)
        products[0].click()

