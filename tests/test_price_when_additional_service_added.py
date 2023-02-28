import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from allure import description, step, severity, severity_level
from assertpy import assert_that

from pages.laptops_page import LaptopsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@description("Calculate total order cost when additional service is added")
@severity(severity_level.NORMAL)
def test_price_when_additional_service_added(set_up):
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
    cart_page.save_laptop_price()
    print("product_price:", cart_page.get_product_price_value())
    cart_page.choose_additional_service()
    cart_page.save_additional_service_price()
    print("additional_service_price:", cart_page.get_additional_price_value())
    time.sleep(3)
    cart_page.save_sum_price()
    print("total_cost:", cart_page.get_sum_price_value())

    with step("Check that total order cost matches the expected one"):
        assert_that(cart_page.laptop_price_cart + cart_page.additional_price) \
            .described_as("Total order cost doesn't match the expected one") \
            .is_equal_to(cart_page.sum_price)

    driver.close()
