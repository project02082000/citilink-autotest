from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import step

from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    catalog_locator = '//button[@data-meta-name="DesktopHeaderFixed__catalog-menu"]'
    laptops_and_pc_locator = '//div[@class="PopupScrollContainer"]//span[contains(text(), \'Ноутбуки и компьютеры\')]'
    laptops_locator = '//span[@class="e1ys5m360 e106ikdt0 css-1bu1ack e1gjr6xo0"][1]'

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
        with step("Choose section with laptops"):
            self.catalog_click()
            self.laptops_and_pc_move_to()
            self.laptops_click()
