import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from allure import step

from base.base_class import Base


class LaptopsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    min_price = '//div[@data-meta-name="FilterListGroupsLayout"]//input[@name="input-min"]'

    max_price = '//div[@data-meta-name="FilterListGroupsLayout"]//input[@name="input-max"]'

    accept_cookie = '//button[@class="e4uhfkv0 css-1jfe691 e4mggex0"]'

    reviews_button = '//div[@data-meta-value="4,5 и выше"]'

    processor_1 = '//div[@data-meta-value=\'Core i7\']'

    processor_2 = '//div[@data-meta-value=\'Core i9\']'

    processor_3 = '//div[@data-meta-value=\'Ryzen 7\']'

    screen_size = '//div[@data-meta-value=\'15.6 "\']'

    ram_size = '//div[@data-meta-value=\'16 ГБ\']'

    show_products_button = '//div[@class="app-catalog-v4lp2l eetttp30"]'

    sorted_by_reviews = '//button[@class="app-catalog-ud4v0n esgsbwb0"][2]'

    laptop = '//a[@class="app-catalog-fjtfe3 e1lhaibo0"][1]'

    # Getters

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_reviews_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reviews_button)))

    def get_accept_cookies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookie)))

    def get_processor_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor_1)))

    def get_processor_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor_2)))

    def get_processor_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor_3)))

    def get_screen_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_size)))

    def get_ram_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram_size)))

    def get_show_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_products_button)))

    def get_sorted_by_reviews(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorted_by_reviews)))

    def get_laptop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop)))

    # Actions

    def clear_min_price(self):
        self.get_min_price().clear()

    def clear_max_price(self):
        self.get_max_price().clear()

    def input_min_price(self, value):
        self.get_min_price().send_keys(value)

    def input_max_price(self, value):
        self.get_max_price().send_keys(value)

    def click_enter_min_price(self):
        self.get_min_price().send_keys(Keys.RETURN)

    def click_enter_max_price(self):
        self.get_max_price().send_keys(Keys.RETURN)

    def click_reviews_button(self):
        self.get_reviews_button().click()

    def click_accept_cookies(self):
        self.get_accept_cookies().click()

    def click_processor_1(self):
        self.get_processor_1().click()

    def click_processor_2(self):
        self.get_processor_2().click()

    def click_processor_3(self):
        self.get_processor_3().click()

    def click_screen_size(self):
        self.get_screen_size().click()

    def click_ram_size(self):
        self.get_ram_size().click()

    def click_show_products(self):
        self.get_show_products().click()

    def click_sort_by_reviews(self):
        self.get_sorted_by_reviews().click()

    def click_laptop(self):
        self.get_laptop().click()

    def get_laptop_url(self):
        laptop_url = self.get_laptop().get_attribute('href')
        self.driver.get(laptop_url)

    # Methods

    def enter_price(self):
        self.clear_min_price()
        self.input_min_price("100000")
        self.click_enter_min_price()
        time.sleep(0.5)
        self.clear_max_price()
        time.sleep(0.5)
        self.input_max_price("200000")
        self.click_enter_max_price()

    def accept_cookies(self):
        with step("Accept cookies"):
            self.click_accept_cookies()

    def choose_good_reviews(self):
        self.click_reviews_button()

    def choose_processor(self):
        self.click_processor_1()
        self.click_processor_2()
        self.click_processor_3()

    def choose_screen_size(self):
        self.click_screen_size()

    def choose_ram_size(self):
        self.click_ram_size()

    def show_products(self):
        self.click_show_products()

    def sort_by_reviews(self):
        with step("Choose sorting by reviews"):
            self.click_sort_by_reviews()

    def choose_laptop(self):
        with step("Choose first laptop"):
            self.get_laptop_url()

    def add_laptop_filters(self):
        with step("Add laptop's filters"):
            self.enter_price()
            self.choose_good_reviews()
            self.choose_processor()
            self.choose_screen_size()
            self.choose_ram_size()
            self.show_products()
