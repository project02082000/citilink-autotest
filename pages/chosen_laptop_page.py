from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import exceptions
import allure

from base.base_class import Base


class ChosenLaptopPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    laptop_name_1 = None
    laptop_price_1 = None

    # Locators

    add_to_cart_button = '//div[@class="ProductPageCTAButtonsSection__buttons-row"]'
    add_to_cart_button_0 = '//button[@data-meta-name=\'BasketDesktopButton\']'
    go_to_cart_button = '//button[@data-label="Перейти в корзину"]'
    go_to_cart_button_0 = '//button[@class=\'e4uhfkv0 css-10je9jt e4mggex0\']'
    laptop_name = '//h1[@class="Heading Heading_level_1 ProductPageTitleSection__text"]'
    laptop_name_0 = '//span[@class="e1ubbx7u0 e106ikdt0 app-catalog-1f1r2mz e1gjr6xo0"]'
    laptop_price = '//span[@class="ProductPagePriceSection__default-price_current-price ' \
                   'js--ProductPagePriceSection__default-price_current-price ' \
                   'ProductPagePriceSection__default-price-value"]'
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
        return self.driver.find_element(By.XPATH, self.laptop_name)

    def get_laptop_name_0(self):
        return self.driver.find_element(By.XPATH, self.laptop_name_0)

    def get_laptop_price(self):
        price = self.driver.find_elements(By.XPATH, self.laptop_price)
        return price[1]

    def get_laptop_price_0(self):
        return self.driver.find_element(By.XPATH, self.laptop_price_0)

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
        self.laptop_name_1 = self.get_laptop_name().text
        print("laptop_name_1:", self.laptop_name_1)

    def save_laptop_name_0(self):
        self.laptop_name_1 = self.get_laptop_name_0().text
        print("laptop_name_1:", self.laptop_name_1)

    def save_laptop_price(self):
        self.laptop_price_1 = self.get_laptop_price().text
        self.laptop_price_1 = int(self.laptop_price_1.replace(" ", ""))
        print("laptop_price_1:", self.laptop_price_1)

    def save_laptop_price_0(self):
        self.laptop_price_1 = self.get_laptop_price_0().text
        self.laptop_price_1 = int(self.laptop_price_1.replace(" ", ""))
        print("laptop_price_1:", self.laptop_price_1)

    # Methods

    def add_and_go_to_cart(self):
        with allure.step("Add product and go to cart"):
            try:
                self.save_laptop_name()
                self.save_laptop_price()
                self.add_to_cart_click()
                self.go_to_cart_click()
            except exceptions.NoSuchElementException:
                self.save_laptop_name_0()
                self.save_laptop_price_0()
                self.add_to_cart_click_0()
                self.go_to_cart_click_0()