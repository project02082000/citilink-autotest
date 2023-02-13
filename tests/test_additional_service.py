import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import assertpy
import allure

from pages.laptops_page import LaptopsPage
from pages.chosen_laptop_page import ChosenLaptopPage
from pages.cart_page import CartPage


@allure.description("Test additional price")
def test_additional_price(set_up):
    url = "https://www.citilink.ru/catalog/noutbuki/"

    service = Service("C:\\Users\\MSI GF75\\PycharmProjects\\resource\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(url)
    driver.maximize_window()

    laptops_page = LaptopsPage(driver)
    laptops_page.accept_cookies()
    laptops_page.choose_laptop()

    chosen_laptop_page = ChosenLaptopPage(driver)
    chosen_laptop_page.add_and_go_to_cart()

    cart_page = CartPage(driver)
    cart_page.save_laptop_price()
    cart_page.choose_additional_service()
    cart_page.save_additional_service_price()
    time.sleep(1)
    cart_page.save_sum_price()

    assertpy.assert_that(cart_page.laptop_price_2 + cart_page.additional_price).described_as(
        "idk what to write").is_equal_to(cart_page.sum_price)
