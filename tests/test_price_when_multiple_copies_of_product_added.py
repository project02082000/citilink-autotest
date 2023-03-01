import time
import os

from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from allure import description, step, severity, severity_level
from assertpy import assert_that

from pages.laptops_page import LaptopsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@description("Calculate total order cost when several copies of product are added")
@severity(severity_level.NORMAL)
def test_price_when_multiple_copies_of_product_added(set_up):
    url = "https://www.citilink.ru/catalog/noutbuki/"
    dir_name = os.path.dirname(__file__)
    service = Service(os.path.join(dir_name, "chromedriver.exe"))
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(url)
    driver.maximize_window()

    laptops_page = LaptopsPage(driver)
    laptops_page.accept_cookies()
    laptops_page.choose_laptop()

    product_page = ProductPage(driver)
    product_page.add_and_go_to_cart()

    cart_page = CartPage(driver)
    cart_page.save_amount_of_product()
    cart_page.save_laptop_price()
    print("product_price:", cart_page.get_product_price_value())

    product_price = cart_page.laptop_price_cart
    cart_page.set_amount_of_product(randint(2, 10))
    time.sleep(5)

    cart_page.save_amount_of_product()
    print("amount_of_product:", cart_page.get_amount_product_value())
    amount_of_product = cart_page.amount_of_product
    cart_page.save_laptop_price()
    print("total_cost:", cart_page.get_product_price_value())
    expected_result = cart_page.laptop_price_cart

    with step("Check that total order cost matches the expected one"):
        assert_that(product_price * amount_of_product) \
            .described_as("Total order cost doesn't match the expected one") \
            .is_equal_to(expected_result)

    driver.close()
