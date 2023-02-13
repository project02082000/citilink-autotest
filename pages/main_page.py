import allure

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    catalog_locator = '//*[@id="__next"]/div/div[3]/div/div[2]/div/div/div[1]/div/button'
    laptops_and_pc_locator = '/html/body/div[5]/div/div/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div[' \
                             '2]/div/div[1]/div/a[2]/div/span'
    laptops_locator = '/html/body/div[5]/div/div/div/div/div[2]/div/div/div/div[7]/div/div[2]/div/div[2]/div/div/div[' \
                      '1]/a'

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_locator)))

    def get_laptops_and_pc(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptops_and_pc_locator)))

    def get_laptops(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptops_locator)))

    # Actions

    def catalog_click(self):
        self.get_catalog().click()

    def laptops_and_pc_move_to(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_laptops_and_pc()).perform()

    def laptops_click(self):
        self.get_laptops().click()

    # Methods

    def choose_laptops(self):
        with allure.step("Choose selection with laptops"):
            self.catalog_click()
            self.laptops_and_pc_move_to()
            self.laptops_click()
