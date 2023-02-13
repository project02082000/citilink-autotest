import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    laptop_name_2 = None
    laptop_price_2 = None
    additional_price = None
    sum_price = None
    amount_of_product = None

    # Locators

    go_to_checkout_button = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[2]/div/div[1]/div[1]/div[1]/div[' \
                            '5]/button'
    laptop_name = '//span[@class="e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0"]'
    laptop_price = '//span[@class="css-0 eb8dq160"]'
    sum_price_locator = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[2]/div/div[1]/div[1]/div[1]/div[' \
                        '4]/div/span/span'
    additional_service = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[6]/div[2]/div/div[' \
                         '2]/div/div[1]/div[1]/span'
    additional_service_price = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[6]/div[' \
                               '2]/div/div[2]/div/div[1]/div[3]/span/span/span[1]'
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
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.amount_of_product_locator)))

    # Actions

    def go_to_checkout_click(self):
        self.get_go_to_checkout().click()

    def choose_additional_service(self):
        self.get_additional_service().click()

    def save_additional_service_price(self):
        self.additional_price = self.get_additional_service_price().text
        self.additional_price = self.additional_price.replace(" ", "")
        self.additional_price = int(self.additional_price.replace("от", ""))
        print("additional_price:", self.additional_price)

    def save_laptop_name(self):
        self.laptop_name_2 = self.get_laptop_name().text
        print("laptop_name_2:", self.laptop_name_2)

    def save_laptop_price(self):
        self.laptop_price_2 = self.get_laptop_price().text
        self.laptop_price_2 = self.laptop_price_2.replace("₽", "")
        self.laptop_price_2 = int(self.laptop_price_2.replace(" ", ""))
        print("laptop_price_2:", self.laptop_price_2)

    def save_sum_price(self):
        self.sum_price = self.get_sum_price().text
        self.sum_price = self.sum_price.replace("₽", "")
        self.sum_price = int(self.sum_price.replace(" ", ""))
        print("sum_price:", self.sum_price)

    def save_amount_of_product(self):
        self.amount_of_product = int(self.get_amount_of_product().get_attribute('value'))
        print("amount_of_product:", self.amount_of_product)

    def set_amount_of_product(self, amount):
        self.get_amount_of_product().clear()
        self.get_amount_of_product().send_keys(amount)
        self.get_laptop_price().click()

    # Methods

    def go_to_checkout(self):
        with allure.step("Go to checkout"):
            self.save_laptop_name()
            self.save_laptop_price()
            self.go_to_checkout_click()
