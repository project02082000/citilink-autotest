from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import step

from base.base_class import Base


class CheckoutPage(Base):
    laptop_name_checkout = None
    laptop_price_checkout = None
    sum_price = None

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    first_name = '//input[@name="firstName"]'
    last_name = '//input[@name="lastName"]'
    phone = '//input[@name="phone"]'
    additional_phone = '//input[@name="additionalPhone"]'
    pickup_point = '//div[@class="TooltipCheckout"]'
    sum_price_locator = '//span[@class="e1j9birj0 e106ikdt0 css-1nj39i9 e1gjr6xo0"]'
    laptop_name = '//*[@id="app-check-out"]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div[' \
                  '1]/div/span[1]'
    laptop_price = '//*[@id="app-check-out"]/div/div/div/div[2]/div/div[2]/div/div/span/span/span[1]'

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_additional_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.additional_phone)))

    def get_pickup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_point)))

    def get_sum_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sum_price_locator)))

    def get_laptop_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_name)))

    def get_laptop_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_price)))

    def get_product_name_value(self):
        return self.laptop_name_checkout

    def get_product_price_value(self):
        return self.laptop_price_checkout

    def get_sum_price_value(self):
        return self.sum_price

    # Actions

    def input_first_name(self):
        self.get_first_name().send_keys("Илья")

    def input_last_name(self):
        self.get_last_name().send_keys("Бутковский")

    def input_phone(self):
        self.get_phone().send_keys("9161494793")

    def input_additional_phone(self):
        self.get_additional_phone().send_keys("88005553535")

    def click_pickup_point(self):
        self.get_pickup_point().click()

    def save_laptop_name(self):
        self.laptop_name_checkout = self.get_laptop_name().text

    def save_laptop_price(self):
        self.laptop_price_checkout = self.get_laptop_price().text
        self.laptop_price_checkout = int(self.laptop_price_checkout.replace(" ", ""))

    def save_sum_price(self):
        self.sum_price = self.get_sum_price().text
        self.sum_price = int(self.sum_price.replace(" ", ""))

    # Methods

    def input_personal_info(self):
        with step("Input personal info"):
            self.input_first_name()
            self.input_last_name()
            self.input_phone()
            self.input_additional_phone()
            self.click_pickup_point()
