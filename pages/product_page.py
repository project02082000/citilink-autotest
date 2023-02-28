from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import exceptions
from allure import step

from base.base_class import Base


class ProductPage(Base):
    laptop_name_product_page = None
    laptop_price_product_page = None

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    add_to_cart_button = '//div[@class="ProductPageCTAButtonsSection__buttons-row"]'
    add_to_cart_button_0 = '//button[@data-meta-name=\'BasketDesktopButton\']'
    go_to_cart_button = '//button[@data-label="Перейти в корзину"]'
    go_to_cart_button_0 = '//button[@class=\'e4uhfkv0 css-10je9jt e4mggex0\']'
    laptop_name = '//h1[@class="Heading Heading_level_1 ProductPageTitleSection__text"]'
    laptop_name_0 = '//h1[@class="e1ubbx7u0 eml1k9j0 app-catalog-tn2wxd e1gjr6xo0"]'
    laptop_price = '//span[@class="ProductPagePriceSection__default-price_current-price ' \
                   'js--ProductPagePriceSection__default-price_current-price ' \
                   'ProductPagePriceSection__default-price-value"][1]'
    laptop_price_0 = '//span[@class="e1j9birj0 e106ikdt0 app-catalog-1f8xctp e1gjr6xo0"]'

    # Getters

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_add_to_cart_button_0(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_0)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

    def get_go_to_cart_button_0(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button_0)))

    def get_laptop_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_name)))

    def get_laptop_name_0(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_name_0)))

    def get_laptop_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_price)))

    def get_laptop_price_0(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_price_0)))

    def get_product_name_value(self):
        return self.laptop_name_product_page

    def get_product_price_value(self):
        return self.laptop_price_product_page

    # Actions

    def add_to_cart_click(self):
        self.get_add_to_cart_button().click()

    def add_to_cart_click_0(self):
        self.get_add_to_cart_button_0().click()

    def go_to_cart_click(self):
        self.get_go_to_cart_button().click()

    def go_to_cart_click_0(self):
        self.get_go_to_cart_button_0().click()

    def save_laptop_name(self):
        try:
            self.laptop_name_product_page = self.get_laptop_name_0().text
        except exceptions.NoSuchElementException:
            self.laptop_name_product_page = self.get_laptop_name().text

    def save_laptop_price(self):
        try:
            self.laptop_price_product_page = self.get_laptop_price_0().text
            self.laptop_price_product_page = int(self.laptop_price_product_page.replace(" ", ""))
        except exceptions.NoSuchElementException:
            self.laptop_price_product_page = self.get_laptop_price().text
            self.laptop_price_product_page = int(self.laptop_price_product_page.replace(" ", ""))

    # Methods

    def add_and_go_to_cart(self):
        with step("Add product and go to cart"):
            try:
                self.add_to_cart_click_0()
                self.go_to_cart_click_0()
            except exceptions.NoSuchElementException:
                self.add_to_cart_click()
                self.go_to_cart_click()
