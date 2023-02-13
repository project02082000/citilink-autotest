import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopChoicePage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    shop = '//*[@id="app-check-out"]/div/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[' \
           '1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div[2]/button[1]'

    # Getters

    def get_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop)))

    # Actions

    def shop_click(self):
        self.get_shop().click()

    # Methods

    def choose_shop(self):
        with allure.step("Choose shop"):
            self.shop_click()
