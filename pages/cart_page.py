from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import step

from base.base_class import Base


class CartPage(Base):
    laptop_name_cart = None
    laptop_price_cart = None
    additional_price = None
    sum_price = None
    amount_of_product = None

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    go_to_checkout_button = '//button[@title="Перейти к оформлению"]'
    laptop_name = '//span[@class="e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0"]'
    laptop_price = '//span[@class="css-0 eb8dq160"]'
    sum_price_locator = '//span[@class="e1j9birj0 e106ikdt0 css-zmmgir e1gjr6xo0"]'
    additional_service = '//span[@class="e11v1gn60 css-389ojc elcxude0"][1]'
    additional_service_price = '//span[@class="e1j9birj0 e106ikdt0 css-xbfpj5 e1gjr6xo0"][1]'
    amount_of_product_locator = '//input[@type="number"]'

    # Getters

    def get_go_to_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_checkout_button)))

    def get_laptop_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop_name)))

    def get_additional_service(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.additional_service)))

    def get_additional_service_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.additional_service_price)))

    def get_laptop_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop_price)))

    def get_sum_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sum_price_locator)))

    def get_amount_of_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.amount_of_product_locator)))

    def get_product_name_value(self):
        return self.laptop_name_cart

    def get_product_price_value(self):
        return self.laptop_price_cart

    def get_additional_price_value(self):
        return self.additional_price

    def get_amount_product_value(self):
        return self.amount_of_product

    def get_sum_price_value(self):
        return self.sum_price

    # Actions

    def go_to_checkout_click(self):
        self.get_go_to_checkout().click()

    def choose_additional_service(self):
        self.get_additional_service().click()

    def save_additional_service_price(self):
        self.additional_price = self.get_additional_service_price().text
        self.additional_price = self.additional_price.replace(" ", "")
        self.additional_price = int(self.additional_price.replace("от", ""))

    def save_laptop_name(self):
        self.laptop_name_cart = self.get_laptop_name().text

    def save_laptop_price(self):
        self.laptop_price_cart = self.get_laptop_price().text
        self.laptop_price_cart = self.laptop_price_cart.replace("₽", "")
        self.laptop_price_cart = int(self.laptop_price_cart.replace(" ", ""))

    def save_sum_price(self):
        self.sum_price = self.get_sum_price().text
        self.sum_price = self.sum_price.replace("₽", "")
        self.sum_price = int(self.sum_price.replace(" ", ""))

    def save_amount_of_product(self):
        self.amount_of_product = int(self.get_amount_of_product().get_attribute('value'))

    def set_amount_of_product(self, amount):
        self.get_amount_of_product().clear()
        self.get_amount_of_product().send_keys(amount)
        self.get_laptop_price().click()

    # Methods

    def go_to_checkout(self):
        with step("Go to checkout"):
            self.go_to_checkout_click()
