import time
import assertpy
import allure

from pages.laptops_page import LaptopsPage
from pages.chosen_laptop_page import ChosenLaptopPage
from pages.cart_page import CartPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@allure.description("Test amount of product")
def test_amount_of_product(set_up):
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
    cart_page.save_amount_of_product()
    cart_page.save_laptop_price()
    product_price_amount_1 = cart_page.laptop_price_2
    cart_page.set_amount_of_product(6)
    time.sleep(1)
    cart_page.save_amount_of_product()
    amount_of_product = cart_page.amount_of_product
    cart_page.save_laptop_price()
    product_price_amount_several = cart_page.laptop_price_2

    assertpy.assert_that(product_price_amount_1 * amount_of_product).described_as(
        "idk what to write").is_equal_to(product_price_amount_several)
