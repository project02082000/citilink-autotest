from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import step

from base.base_class import Base


class ShopChoicePage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    shop = '//div[@class="OrderDeliveryCard__change"][1]'
    shop_2 = '//button[@class="e1tiqnd20 css-1oq0lvh e4mggex0"]'

    # Getters

    def get_shop(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.shop)))

    def get_shop_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_2)))

    # Actions

    def shop_click(self):
        self.get_shop().click()

    def shop_click_2(self):
        self.get_shop_2().click()

    # Methods

    def choose_shop(self):
        with step("Choose shop"):
            try:
                self.shop_click()
            except exceptions.TimeoutException:
                self.shop_click_2()
