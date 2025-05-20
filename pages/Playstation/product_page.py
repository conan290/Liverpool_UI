from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_title = (By.CSS_SELECTOR, ".a-product__information--title")
        self.product_price = (By.CLASS_NAME, "a-product__paragraphDiscountPrice")


    def get_product_title(self):
        wait = WebDriverWait(self.driver, 15)
        title_element = wait.until(EC.presence_of_element_located(self.product_title))
        return title_element.text

    def get_product_price(self):
        wait = WebDriverWait(self.driver, 10)
        price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-product__paragraphDiscountPrice")))
        return price_element.text


