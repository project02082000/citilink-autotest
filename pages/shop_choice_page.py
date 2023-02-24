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

    # Getters

    def get_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop)))

    # Actions

    def shop_click(self):
        self.get_shop().click()

    # Methods

    def choose_shop(self):
        with step("Choose shop"):
            self.shop_click()
